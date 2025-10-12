> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxKontextMultiReferenceLatentMethod/ja.md)

FluxKontextMultiReferenceLatentMethodノードは、特定の参照潜在表現メソッドを設定することで条件付けデータを変更します。このノードは選択されたメソッドを条件付け入力に追加し、後続の生成ステップにおける参照潜在表現の処理方法に影響を与えます。このノードは実験的としてマークされており、Flux条件付けシステムの一部です。

## 入力

| パラメータ | データ型 | 必須 | 範囲 | 説明 |
|-----------|-----------|----------|-------|-------------|
| `conditioning` | CONDITIONING | はい | - | 参照潜在表現メソッドで修正される条件付けデータ |
| `reference_latents_method` | STRING | はい | `"offset"`<br>`"index"`<br>`"uxo/uno"` | 参照潜在表現処理に使用するメソッド。"uxo"または"uso"が選択された場合、"uxo"に変換されます |

## 出力

| 出力名 | データ型 | 説明 |
|-------------|-----------|-------------|
| `conditioning` | CONDITIONING | 参照潜在表現メソッドが適用された修正済み条件付けデータ |
