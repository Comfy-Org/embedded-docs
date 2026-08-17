# MaskPreview

以下に、英語ドキュメントを日本語に翻訳しました。

---

MaskPreview ノードは、マスクデータの視覚的なプレビューを ComfyUI インターフェース上に直接表示するため、ワークフロー中にマスクを確認できます。このノードは、ComfyUI の出力ディレクトリに保存せずにプレビューを表示し、マスクをそのまま出力として渡します。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
|-----------|-------------|-----------|----------|-------|
| `mask` | プレビューするマスクデータ | MASK | はい | - |
| `filename_prefix` | 出力ファイル名のプレフィックス（デフォルト: "ComfyUI"） | STRING | いいえ | - |
| `prompt` | メタデータ用のプロンプト情報（自動的に提供されます） | PROMPT | いいえ | - |
| `extra_pnginfo` | メタデータ用の追加 PNG 情報（自動的に提供されます） | EXTRA_PNGINFO | いいえ | - |

## 出力

| 出力名 | 説明 | データ型 |
|-------------|-------------|-----------|
| `mask` | プレビューされたマスクデータがそのまま渡されます | MASK |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MaskPreview/ja.md)

---
**Source fingerprint (SHA-256):** `3d4ecb8cd90c3ecbe9d3cff8f782062c582c7190d9f0e0ed069cba114d4beac5`
