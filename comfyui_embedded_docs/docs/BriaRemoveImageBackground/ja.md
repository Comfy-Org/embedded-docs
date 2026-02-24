> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaRemoveImageBackground/ja.md)

このノードは、Bria RMBG 2.0 サービスを使用して画像から背景を除去します。画像を外部APIに送信して処理を行い、背景が除去された結果を返します。

## 入力

| パラメータ | データ型 | 必須 | 範囲 | 説明 |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | はい | - | 背景を除去する対象の入力画像です。 |
| `moderation` | COMBO | いいえ | `"false"`<br>`"true"` | モデレーション設定です。`"true"`に設定すると、追加のモデレーションオプションが利用可能になります。 |
| `visual_input_moderation` | BOOLEAN | いいえ | - | 入力画像に対して視覚的コンテンツのモデレーションを有効にします。このパラメータは`moderation`が`"true"`に設定されている場合のみ利用可能です。デフォルト: `False`。 |
| `visual_output_moderation` | BOOLEAN | いいえ | - | 出力画像に対して視覚的コンテンツのモデレーションを有効にします。このパラメータは`moderation`が`"true"`に設定されている場合のみ利用可能です。デフォルト: `True`。 |
| `seed` | INT | いいえ | 0 から 2147483647 | ノードを再実行するかどうかを制御するシード値です。シード値に関わらず、結果は非決定的です。デフォルト: `0`。 |

**注意:** `visual_input_moderation`および`visual_output_moderation`パラメータは、`moderation`パラメータに依存しています。これらのパラメータは、`moderation`が`"true"`に設定されている場合にのみ有効かつ必須となります。

## 出力

| 出力名 | データ型 | 説明 |
|-------------|-----------|-------------|
| `image` | IMAGE | 背景が除去された処理済み画像です。 |