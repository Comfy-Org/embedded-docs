#!/usr/bin/env python3
"""Regression tests for leaked translation preambles under the H1.

PR #189 removed this Japanese lead, which the docs site had used as the
meta description:

    これはComfyUIノードドキュメントの技術翻訳です。以下が日本語訳になります。

``以下が日本語訳`` was only matched at line start, so the clause after ``。``
slipped through. These tests lock that sentence, the same mid-line shape
without the ``技術翻訳`` opener, and ordinary overview prose that merely
mentions translation or docs.
"""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from scripts import fix_translation_preamble as ftp  # noqa: E402


def _page(title: str, lead: str, heading: str, body: str) -> str:
    return f"# {title}\n\n{lead}\n\n## {heading}\n\n{body}\n"


class StripLeakPreambleTests(unittest.TestCase):
    PR189 = "これはComfyUIノードドキュメントの技術翻訳です。以下が日本語訳になります。"
    OVERVIEW = (
        "SAM3トラッキングセッションから、インデックス番号によって特定の追跡オブジェクトを"
        "選択し、それらを1つの出力マスクに結合します。"
    )

    def test_pr189_japanese_sentence_is_stripped(self):
        text = _page("SAM3トラックからマスク", self.PR189, "概要", self.OVERVIEW)
        cleaned, removed = ftp.strip_leak(text, "ja")
        self.assertGreater(removed, 0)
        self.assertNotIn(self.PR189, cleaned)
        self.assertNotIn("技術翻訳", cleaned)
        self.assertIn(self.OVERVIEW, cleaned)
        self.assertIn("## 概要", cleaned)
        self.assertTrue(cleaned.startswith("# SAM3トラックからマスク\n"))

    def test_japanese_clause_after_period_is_stripped(self):
        """The ``以下が日本語訳`` clause alone, after 。, is still a preamble."""
        lead = "指定された英文の要点を先にまとめます。以下が日本語訳になります。"
        text = _page("ノード", lead, "概要", self.OVERVIEW)
        cleaned, removed = ftp.strip_leak(text, "ja")
        self.assertGreater(removed, 0)
        self.assertNotIn("以下が日本語訳", cleaned)
        self.assertIn(self.OVERVIEW, cleaned)

    def test_line_start_japanese_clause_still_stripped(self):
        lead = "以下が日本語訳になります。"
        text = _page("ノード", lead, "概要", self.OVERVIEW)
        cleaned, removed = ftp.strip_leak(text, "ja")
        self.assertGreater(removed, 0)
        self.assertNotIn(lead, cleaned)
        self.assertIn(self.OVERVIEW, cleaned)

    def test_legitimate_overview_mentioning_translation_is_kept(self):
        lead = (
            "このノードは追跡結果から残す対象を選び、ドキュメントの手順どおり"
            "1枚のマスクにまとめます。翻訳設定は使いません。"
        )
        text = _page("ノード", lead, "概要", self.OVERVIEW)
        cleaned, removed = ftp.strip_leak(text, "ja")
        self.assertEqual(removed, 0)
        self.assertEqual(cleaned, text)

    def test_incidental_mid_sentence_japanese_clause_is_kept(self):
        """``以下が日本語訳`` that is not its own sentence must stay."""
        lead = "図の注釈では以下が日本語訳の見本を示し、ドキュメントの読み方を補います。"
        text = _page("ノード", lead, "概要", self.OVERVIEW)
        cleaned, removed = ftp.strip_leak(text, "ja")
        self.assertEqual(removed, 0)
        self.assertEqual(cleaned, text)

    def test_negated_technical_translation_is_kept(self):
        for lead in (
            "これは技術翻訳ではありません。追跡結果をドキュメントどおりマスクにします。",
            "これは技術翻訳じゃない。追跡結果をドキュメントどおりマスクにします。",
        ):
            with self.subTest(lead=lead):
                text = _page("ノード", lead, "概要", self.OVERVIEW)
                cleaned, removed = ftp.strip_leak(text, "ja")
                self.assertEqual(removed, 0)
                self.assertEqual(cleaned, text)

    def test_preamble_after_real_lead_is_kept(self):
        """A strong marker only counts directly under the H1."""
        text = (
            "# ノード\n\n"
            "追跡した物体を1枚のマスクにまとめます。\n\n"
            "## 概要\n\n"
            f"{self.PR189}\n"
        )
        cleaned, removed = ftp.strip_leak(text, "ja")
        self.assertEqual(removed, 0)
        self.assertEqual(cleaned, text)

    def test_zh_technical_translation_preamble_is_stripped(self):
        lead = "这是ComfyUI节点文档的技术翻译。以下是中文译文。"
        body = "这个节点会把跟踪结果合成一张遮罩。"
        text = _page("测试节点", lead, "概述", body)
        cleaned, removed = ftp.strip_leak(text, "zh")
        self.assertGreater(removed, 0)
        self.assertNotIn("技术翻译", cleaned)
        self.assertIn(body, cleaned)

    def test_zh_clause_after_period_is_stripped(self):
        lead = "先给出结论。以下是中文译文。"
        body = "这个节点会按照文档把结果合成一张遮罩。"
        text = _page("测试节点", lead, "概述", body)
        cleaned, removed = ftp.strip_leak(text, "zh")
        self.assertGreater(removed, 0)
        self.assertNotIn("以下是中文译文", cleaned)
        self.assertIn(body, cleaned)

    def test_zh_legitimate_overview_is_kept(self):
        lead = "这个节点会按照文档把跟踪结果合成一张遮罩，不需要额外的翻译步骤。"
        text = _page("测试节点", lead, "概述", lead)
        cleaned, removed = ftp.strip_leak(text, "zh")
        self.assertEqual(removed, 0)
        self.assertEqual(cleaned, text)

    def test_zh_tw_technical_translation_preamble_is_stripped(self):
        lead = "這是ComfyUI節點文件的技術翻譯。以下是中文譯文。"
        body = "這個節點會把追蹤結果合成一張遮罩。"
        text = _page("測試節點", lead, "概述", body)
        cleaned, removed = ftp.strip_leak(text, "zh-TW")
        self.assertGreater(removed, 0)
        self.assertNotIn("技術翻譯", cleaned)
        self.assertIn(body, cleaned)

    def test_zh_tw_translation_result_opener_is_stripped(self):
        """Live leak: Magnific Image Relight (zh-TW) opened with this line."""
        lead = "以下是繁體中文翻譯結果："
        body = "Magnific Image Relight 節點可調整輸入影像的光線。"
        text = _page("Magnific 圖像重光", lead, "概述", body)
        cleaned, removed = ftp.strip_leak(text, "zh-TW")
        self.assertGreater(removed, 0)
        self.assertNotIn(lead, cleaned)
        self.assertIn(body, cleaned)

    def test_ko_technical_translation_preamble_is_stripped(self):
        lead = "이것은 ComfyUI 노드 문서의 기술 번역입니다. 다음은 한국어 번역입니다."
        body = "이 노드는 추적 결과를 하나의 마스크로 합칩니다."
        text = _page("테스트 노드", lead, "개요", body)
        cleaned, removed = ftp.strip_leak(text, "ko")
        self.assertGreater(removed, 0)
        self.assertNotIn("기술 번역", cleaned)
        self.assertIn(body, cleaned)

    def test_ko_clause_after_period_is_stripped(self):
        lead = "요청한 내용을 먼저 정리했습니다. 다음은 한국어 번역입니다."
        body = "이 노드는 문서에 적힌 대로 마스크를 만듭니다."
        text = _page("테스트 노드", lead, "개요", body)
        cleaned, removed = ftp.strip_leak(text, "ko")
        self.assertGreater(removed, 0)
        self.assertNotIn("다음은 한국어 번역", cleaned)
        self.assertIn(body, cleaned)

    def test_ko_legitimate_overview_is_kept(self):
        lead = "이 노드는 문서에 적힌 대로 마스크를 만듭니다. 번역 설정은 필요 없습니다."
        text = _page("테스트 노드", lead, "개요", lead)
        cleaned, removed = ftp.strip_leak(text, "ko")
        self.assertEqual(removed, 0)
        self.assertEqual(cleaned, text)


if __name__ == "__main__":
    unittest.main()
