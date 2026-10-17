#!/usr/bin/env python3
"""Unit tests for scripts.sync_to_comfy_docs normalization helpers.

Covers the CodeRabbit review fixes: inline-code stashing, curly-brace
escaping, whitespace-preserving < escaping, description extraction
(image/table skipping, e.g. protection), acronym-preserving labels,
and non-destructive nav purge.
"""

import os
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))
sys.path.insert(0, str(REPO_ROOT / "scripts"))

os.environ.setdefault("TARGET_DOCS", str(REPO_ROOT / ".." / "docs"))
os.environ.setdefault("COMFYUI_PATH", "")

from scripts import sync_to_comfy_docs as sc  # noqa: E402


class SegToLabelTests(unittest.TestCase):
    def test_title_cases_underscores(self):
        self.assertEqual(sc._seg_to_label("custom_sampling"), "Custom Sampling")

    def test_preserves_acronyms(self):
        self.assertEqual(sc._seg_to_label("SDXL"), "SDXL")
        self.assertEqual(sc._seg_to_label("API_node"), "API Node")
        self.assertEqual(sc._seg_to_label("bfl_flux"), "Bfl Flux")


class NormalizeMdxTests(unittest.TestCase):
    def test_inline_code_preserved(self):
        out = sc._normalize_mdx_content("Use `x <= 10` for limits.")
        self.assertIn("`x <= 10`", out)
        self.assertNotIn("&lt;=", out.split("`")[1])

    def test_fenced_code_preserved_verbatim(self):
        out = sc._normalize_mdx_content("```python\nif x <= 10: print({1})\n```")
        self.assertIn("if x <= 10: print({1})", out)

    def test_curly_braces_escaped_in_prose(self):
        out = sc._normalize_mdx_content("The bbox {x, y} syntax.")
        self.assertIn("&#123;x, y&#125;", out)

    def test_curly_braces_not_escaped_in_code(self):
        out = sc._normalize_mdx_content("```json\n{\"a\": 1}\n```")
        self.assertIn('{"a": 1}', out)

    def test_whitespace_after_lt_preserved(self):
        out = sc._normalize_mdx_content("text < more")
        self.assertIn("text &lt; more", out)

    def test_paired_mintlify_component_kept(self):
        out = sc._normalize_mdx_content("<Note>\nHeads up.\n</Note>")
        self.assertIn("<Note>", out)
        self.assertIn("</Note>", out)

    def test_orphaned_closing_tag_escaped(self):
        out = sc._normalize_mdx_content("text </Note> more")
        self.assertIn("&lt;/Note>", out)


class DescriptionExtractionTests(unittest.TestCase):
    def test_skips_image_and_table_lines(self):
        content = "![img](x.png)\n\n| A | B |\n|---|---|\n\nThis is the first sentence. Second sentence."
        desc = sc.get_description_from_content(content)
        self.assertTrue(desc.startswith("This is the first sentence."))

    def test_does_not_cut_abbreviations(self):
        desc = sc.get_description_from_content("This is a test e.g. with abbreviations. Second sentence.")
        self.assertTrue(desc.startswith("This is a test e.g."))

    def test_cjk_sentence_break(self):
        # One short sentence stays under the 40-char floor, so the next
        # sentence from the same paragraph is appended without a space.
        desc = sc.get_description_from_content("这是第一句话。第二句话。")
        self.assertEqual(desc, "这是第一句话。第二句话。")

    def test_cjk_floor_join_does_not_insert_a_space(self):
        desc = sc.get_description_from_content(
            "调整图像的亮度。它把每个像素的颜色值乘以系数。结果被限制在 0 到 1 之间，因此高光不会溢出。"
        )
        self.assertNotIn("。 ", desc)
        self.assertGreaterEqual(len(desc), sc._MIN_DESCRIPTION_CHARS)

    def test_truncation_stays_within_the_160_char_window(self):
        long = "Word " * 100
        desc = sc.get_description_from_content(long)
        self.assertLessEqual(len(desc), sc.MAX_DESCRIPTION_CHARS)
        self.assertTrue(desc.endswith("Word"))

    def test_truncation_does_not_end_mid_word(self):
        # A single long sentence: the cut must land on a word boundary instead
        # of slicing "Latent Apply Operation or La".
        sentence = (
            "This node creates a latent operation that blends a latent toward a reference latent, "
            "and returns that operation so it can be plugged into the Latent Apply Operation node."
        )
        desc = sc.get_description_from_content(sentence)
        self.assertLessEqual(len(desc), sc.MAX_DESCRIPTION_CHARS)
        # The cut must land between words/clauses, never inside one.
        self.assertFalse(sentence[len(desc)].isalnum())

    def test_localized_sentence_break_without_ascii_uppercase(self):
        # Korean starts the next sentence with a non-ASCII letter, which the
        # uppercase lookahead never matched: the page fell through to a hard
        # 180-char cut and lost the summary mid-sentence. The short first
        # sentence is then grown to the 40-char floor, still on a boundary.
        content = (
            "이 노드는 레이턴트를 참조 레이턴트 쪽으로 블렌딩합니다. "
            + "참조가 다른 공간 크기를 가질 경우 크기가 조정됩니다. " * 6
        )
        desc = sc.get_description_from_content(content)
        self.assertTrue(desc.startswith("이 노드는 레이턴트를 참조 레이턴트 쪽으로 블렌딩합니다."))
        self.assertTrue(desc.endswith("."))
        self.assertLessEqual(len(desc), sc.MAX_DESCRIPTION_CHARS)

    def test_korean_disclaimer_is_skipped(self):
        content = "> 이 문서는 AI가 생성했습니다.\n\n이 노드는 이미지의 밝기를 조정합니다."
        self.assertEqual(
            sc.get_description_from_content(content), "이 노드는 이미지의 밝기를 조정합니다."
        )

    def test_japanese_plain_paragraph_disclaimer_is_skipped(self):
        # ja pages open with the disclaimer as a plain paragraph, not a
        # blockquote, so it used to become the whole meta description (and the
        # "edit on GitHub" link after it grew into the 160-char window).
        content = (
            "# ケースコンバーター\n\n"
            "このドキュメントはAIによって生成されました。誤りを見つけた場合や改善の提案がある場合は、"
            "ぜひご協力ください！[GitHubで編集する](https://github.com/Comfy-Org/embedded-docs/blob/main/en.md)\n\n"
            "Case Converterノードは、テキスト文字列を異なる文字ケース形式に変換します。\n"
        )
        desc = sc.get_description_from_content(content)
        self.assertTrue(desc.startswith("Case Converterノードは"))
        self.assertNotIn("AI", desc)
        self.assertNotIn("github.com", desc)

    def test_chinese_plain_paragraph_disclaimer_is_skipped(self):
        content = (
            "此文档由AI生成。如发现任何错误或有改进建议，欢迎贡献！"
            "[在GitHub上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/en.md)\n\n"
            "此节点把文本转换为指定的大小写格式，支持四种转换模式。\n"
        )
        desc = sc.get_description_from_content(content)
        self.assertTrue(desc.startswith("此节点把文本转换为"))

    def test_plain_ai_generated_overview_is_not_skipped(self):
        # A real overview may legitimately mention AI-generated content.
        content = "This node applies AI-generated textures to an existing 3D model."
        self.assertEqual(sc.get_description_from_content(content), content)

    def test_overview_written_under_an_h2_is_used(self):
        # 30 nodes put the overview under "## 概述"/"## 개요"/"## 概要" instead of
        # directly under the H1; the extractor used to stop at the heading and
        # leave the page on the English template fallback.
        for heading, sentence in (
            ("## 概述", "这是概述的第一句话。它补充了足够多的细节。"),
            ("## 概要", "これは概要の最初の文です。十分な詳細を追加します。"),
            ("## 개요", "이것은 개요의 첫 번째 문장입니다. 충분한 세부 정보를 추가합니다."),
            ("## Overview", "This is the overview sentence. It adds enough detail to pass."),
        ):
            with self.subTest(heading=heading):
                content = f"# Title\n\n{heading}\n\n{sentence}\n\n## Inputs\n\n| A | B |\n| --- | --- |\n"
                desc = sc.get_description_from_content(content)
                self.assertTrue(desc.startswith(sentence.split("。")[0].split(". ")[0][:12]))

    def test_doubled_hash_overview_heading_is_recognised(self):
        # Historical translation bug: "## ## 概述". Treated as the overview
        # heading so the page keeps a real description.
        content = "# 节点\n\n## ## 概述\n\n这个节点把输入的文本转换成不同的大小写形式。\n\n## 输入\n"
        self.assertTrue(sc.get_description_from_content(content).startswith("这个节点把输入的文本"))

    def test_non_overview_first_section_is_not_used_as_description(self):
        content = "# Node\n\n## Inputs\n\n| Parameter | Description |\n| --- | --- |\n| `a` | b |\n"
        self.assertEqual(sc.get_description_from_content(content), "")

    def test_truncation_keeps_versions_intact(self):
        # A period inside "2.5" is not a sentence ender, even when the text is
        # long enough to be truncated.
        content = (
            "It supports Seedance 2.5, 2.5 Draft, 2.0 and 2.1 with reference images "
            * 4
        ).strip()
        desc = sc.get_description_from_content(content)
        self.assertLessEqual(len(desc), sc.MAX_DESCRIPTION_CHARS)
        self.assertGreater(len(content), len(desc))
        self.assertFalse(desc.endswith("2."))

    def test_latest_clause_separator_wins(self):
        # A semicolon later than the last comma must win the clause cut.
        content = "A, " + "B" * 100 + "; " + "C" * 60
        self.assertEqual(sc.get_description_from_content(content), "A, " + "B" * 100)

    def test_earliest_sentence_boundary_wins(self):
        # A localized sentence boundary must not lose to a later English one.
        # The first sentence already clears the floor, so it is not grown.
        first = "첫 번째 문장은 이 노드가 레이턴트를 어떻게 처리하는지 자세히 설명합니다."
        self.assertEqual(
            sc.get_description_from_content(f"{first} 두 번째 문장입니다. Third sentence follows."),
            first,
        )

    def test_limit_inside_a_version_is_not_a_sentence_end(self):
        # The period of "ver2." sits exactly on the limit boundary; the
        # lookahead has to see the following digit to reject it.
        content = "x" * 154 + " ver2.5 next words here"
        desc = sc.get_description_from_content(content)
        self.assertLessEqual(len(desc), sc.MAX_DESCRIPTION_CHARS)
        self.assertFalse(desc.endswith("."))


class DescriptionFloorTests(unittest.TestCase):
    """The generator must not emit descriptions below the 40-char guideline."""

    def test_short_first_sentence_is_grown(self):
        content = "Adjusts image brightness. It multiplies the colour values by a factor and clamps the result."
        desc = sc.get_description_from_content(content)
        self.assertEqual(desc, content)
        self.assertGreaterEqual(len(desc), sc._MIN_DESCRIPTION_CHARS)

    def test_growth_stops_at_the_paragraph_end(self):
        # Nothing to append: the description stays short instead of inventing text.
        content = "Adjusts brightness."
        desc = sc.get_description_from_content(content)
        self.assertEqual(desc, "Adjusts brightness.")

    def test_growth_never_exceeds_the_ceiling(self):
        content = (
            "Adjusts brightness. "
            "It multiplies the colour values of every pixel by a per-image factor and clamps "
            "the result so highlights do not clip, while optional per-channel offsets keep "
            "neutral greys from drifting between the input and output tensors of the node."
        )
        desc = sc.get_description_from_content(content)
        self.assertLessEqual(len(desc), sc.MAX_DESCRIPTION_CHARS)
        # Too long to append whole: as much of it as fits is kept, never a
        # fragment of a word.
        self.assertGreaterEqual(len(desc), sc._MIN_DESCRIPTION_CHARS)
        self.assertTrue(desc.startswith("Adjusts brightness."))
        self.assertFalse(content[len(desc)].isalnum())

    def test_long_first_sentence_is_not_grown(self):
        content = (
            "This node blends a latent toward a reference latent and returns the "
            "operation for the Latent Apply Operation node. Second sentence."
        )
        desc = sc.get_description_from_content(content)
        self.assertEqual(desc, "This node blends a latent toward a reference latent and returns the operation for the Latent Apply Operation node.")

    def test_growth_skips_the_ai_disclaimer(self):
        content = "> This document was AI-generated.\n\nAdjusts image brightness. It clamps the result to 0-1."
        desc = sc.get_description_from_content(content)
        self.assertNotIn("AI-generated", desc)
        self.assertTrue(desc.startswith("Adjusts image brightness."))


class PurgeNavTests(unittest.TestCase):
    def _fake_locale(self):
        """Point the en locale's builtin_dir at a temp dir with a real .mdx file."""
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        builtin_dir = Path(tmp.name) / "built-in-nodes"
        builtin_dir.mkdir()
        (builtin_dir / "CLIPTextEncodeControlnet.mdx").write_text("---\n---\n", encoding="utf-8")
        orig = sc.LOCALE_CONFIGS[0]["builtin_dir"]
        sc.LOCALE_CONFIGS[0]["builtin_dir"] = builtin_dir
        self.addCleanup(lambda: sc.LOCALE_CONFIGS[0].__setitem__("builtin_dir", orig))
        # Drop any cached listing for the original dir so the fake dir is used
        sc._locale_mdx_names.cache_clear()
        return builtin_dir

    def test_replaces_canonical_when_mdx_exists(self):
        self._fake_locale()
        nav = [{
            "group": "Nodes",
            "pages": [
                "built-in-nodes/ClipTextEncodeControlnet",
                "built-in-nodes/KSampler",
            ],
        }]
        sc._purge_noncanonical_nav_pages(nav)
        keys = sc.collect_page_keys(nav)
        self.assertIn("built-in-nodes/CLIPTextEncodeControlnet", keys)
        self.assertNotIn("built-in-nodes/ClipTextEncodeControlnet", keys)
        self.assertIn("built-in-nodes/KSampler", keys)

    def test_keeps_unknown_key_without_mdx(self):
        self._fake_locale()
        nav = [{"group": "Nodes", "pages": ["built-in-nodes/NonexistentNodeXYZ"]}]
        sc._purge_noncanonical_nav_pages(nav)
        keys = sc.collect_page_keys(nav)
        self.assertIn("built-in-nodes/NonexistentNodeXYZ", keys)


class FrontmatterTests(unittest.TestCase):
    def test_concrete_description_used(self):
        fm = sc.build_frontmatter("Canny", "Extract all edge lines from photos.")
        self.assertIn("Extract all edge lines from photos.", fm)
        self.assertNotIn("Complete documentation for the Canny node", fm)

    def test_template_fallback_when_empty(self):
        fm = sc.build_frontmatter("Canny", "")
        self.assertIn("Complete documentation for the Canny node", fm)


class CrossDirAssetCollisionTests(unittest.TestCase):
    """Regression: three distinct external assets sharing one basename must not
    overwrite each other (CodeRabbit PR #120 review)."""

    def _copy_assets(self, abs_paths):
        """Run copy_assets_and_rewrite against temp dirs; return (out_names, errors)."""
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            doc_dir = root / "docs" / "SomeNode"
            doc_dir.mkdir(parents=True)
            out_dir = root / "images_out"
            content_lines = []
            for i, src in enumerate(abs_paths):
                src.parent.mkdir(parents=True, exist_ok=True)
                src.write_bytes(bytes([i + 1]))  # distinct bytes per source
                rel = os.path.relpath(src, doc_dir)
                content_lines.append(f"![img{i}]({rel})")
            content = "\n".join(content_lines)
            # All refs resolve outside doc_dir -> cross-directory path
            sc.copy_assets_and_rewrite(content, doc_dir, "SomeNode", out_dir, dry_run=False)
            return sorted(p.name for p in out_dir.iterdir()), sorted(
                p.read_bytes() for p in out_dir.iterdir()
            )

    def test_three_external_assets_same_basename_no_overwrite(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            abs_paths = [
                root / "one" / "assets" / "icon.webp",
                root / "two" / "assets" / "icon.webp",
                root / "three" / "assets" / "icon.webp",
            ]
            names, blobs = self._copy_assets(abs_paths)
            # Three distinct destination names (collision suffixes applied)
            self.assertEqual(len(names), 3)
            # Distinct bytes means no overwrite (each source written its own data)
            self.assertEqual(len(set(blobs)), 3)
            self.assertIn("icon.webp", names)

    def test_cross_dir_uses_parent_name_prefix(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            a = root / "one" / "assets" / "icon.webp"
            b = root / "two" / "assets" / "icon.webp"
            names, _ = self._copy_assets([a, b])
            self.assertEqual(len(names), 2)
            # Second file must get a parent-name prefix, not a bare collision name
            self.assertIn("assets_icon.webp", names)


if __name__ == "__main__":
    unittest.main()
