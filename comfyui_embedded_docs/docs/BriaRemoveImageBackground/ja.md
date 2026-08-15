# Bria 画像背景除去

このノードは、Bria RMBG 2.0 サービスを使用して画像から背景を除去します。画像を外部 API に送信して処理し、背景が除去された結果を返します。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
|-----------|-------------|-----------|----------|-------|
| `image` | 背景を除去する対象の入力画像です。 | IMAGE | はい | - |
| `moderation` | モデレーション設定です。`"true"` に設定すると、追加のモデレーションオプションが利用可能になります。 | COMBO | いいえ | `"false"`<br>`"true"` |
| `visual_input_moderation` | 入力画像に対して視覚的なコンテンツモデレーションを有効にします。このパラメータは、`moderation` が `"true"` に設定されている場合にのみ利用可能です。デフォルト: `False`。 | BOOLEAN | いいえ | - |
| `visual_output_moderation` | 出力画像に対して視覚的なコンテンツモデレーションを有効にします。このパラメータは、`moderation` が `"true"` に設定されている場合にのみ利用可能です。デフォルト: `True`。 | BOOLEAN | いいえ | - |
| `seed` | シードはノードを再実行するかどうかを制御します。シードに関係なく結果は非決定的です。デフォルト: `0`。 | INT | いいえ | 0 ～ 2147483647 |

**注:** `visual_input_moderation` と `visual_output_moderation` の各パラメータは、`moderation` パラメータに依存します。これらは、`moderation` が `"true"` に設定されている場合にのみ有効です。

## 出力

| 出力名 | 説明 | データ型 |
|-------------|-------------|-----------|
| `image` | 背景が除去された処理済み画像です。 | IMAGE |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaRemoveImageBackground/ja.md)

---
**Source fingerprint (SHA-256):** `f62dcd5c9406ec09f5aab44585dd7f25ae0f7d9a934faa10a58e46ef116df110`
