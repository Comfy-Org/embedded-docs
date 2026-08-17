# CLIPTextEncodeHiDream

CLIPTextEncodeHiDream ノードは、異なる言語モデル（CLIP-L、CLIP-G、T5-XXL、LLaMA）を使用して4つの個別のテキスト入力を処理し、それらを単一のconditioning出力に結合します。各テキスト入力を対応するモデルでトークン化し、スケジュールされたエンコーディング方式を使用して一緒にエンコードすることで、複数の言語モデルを同時に活用し、より高度なテキストconditioningを可能にします。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `clip` | トークン化とエンコーディングに使用されるCLIPモデル | CLIP | はい | - |
| `clip_l` | CLIP-Lモデル処理用のテキスト入力。複数行テキストと動的プロンプトに対応しています。 | STRING | はい | - |
| `clip_g` | CLIP-Gモデル処理用のテキスト入力。複数行テキストと動的プロンプトに対応しています。 | STRING | はい | - |
| `t5xxl` | T5-XXLモデル処理用のテキスト入力。複数行テキストと動的プロンプトに対応しています。 | STRING | はい | - |
| `llama` | LLaMAモデル処理用のテキスト入力。複数行テキストと動的プロンプトに対応しています。 | STRING | はい | - |

**注記:** 4つのテキスト入力（`clip_l`、`clip_g`、`t5xxl`、`llama`）はすべて、スケジュールされたエンコーディングプロセスを通じて最終的なconditioning出力に寄与するため、正しく機能するために必要です。

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `CONDITIONING` | スケジュールされたエンコーディング方式でエンコードされた、処理済みのすべてのテキスト入力から得られる結合conditioning出力 | CONDITIONING |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeHiDream/ja.md)

---
**Source fingerprint (SHA-256):** `c5e269c17bd2dd7d7171c02598a87983a988d953dd7df285978fc25a9c896e46`
