# Hunyuan3Dv2ConditioningMultiView

Hunyuan3Dv2ConditioningMultiViewノードは、3Dビデオ生成のためのマルチビューCLIPビジョン埋め込みを処理します。このノードは、任意のフロント、レフト、バック、ライトの各ビュー埋め込みを受け取り、提供された各ビューに位置エンコーディングを追加してから、それらを単一のコンディショニングシーケンスに結合します。ノードは、結合された埋め込みからポジティブコンディショニングと、ゼロ値を持つネガティブコンディショニングの両方を出力します。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `front` | フロントビューのCLIPビジョン出力 | CLIP_VISION_OUTPUT | いいえ | - |
| `left` | レフトビューのCLIPビジョン出力 | CLIP_VISION_OUTPUT | いいえ | - |
| `back` | バックビューのCLIPビジョン出力 | CLIP_VISION_OUTPUT | いいえ | - |
| `right` | ライトビューのCLIPビジョン出力 | CLIP_VISION_OUTPUT | いいえ | - |

**注:** ノードが機能するには、少なくとも1つのビュー入力が必要です。ノードは、有効なCLIPビジョン出力データを含むビューのみを処理します。提供された各ビューは、そのビュー位置（front、left、back、right）に基づいて位置エンコーディングを受け取り、エンコードされたビューは同じ順序で連結されます。

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `positive` | 位置エンコーディングを含む結合されたマルチビュー埋め込みを含むポジティブコンディショニング | CONDITIONING |
| `negative` | ポジティブコンディショニングと同じ形状のゼロ値を含むネガティブコンディショニング | CONDITIONING |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Hunyuan3Dv2ConditioningMultiView/ja.md)

---
**Source fingerprint (SHA-256):** `1492b51661d0bb8f2c142c1b1e8ef104beed1b9dae532a970e2928e27ad71d69`
