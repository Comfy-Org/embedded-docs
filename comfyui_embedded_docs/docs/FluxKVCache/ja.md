> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxKVCache/ja.md)

このドキュメントは AI が生成しました。誤りを見つけた場合や改善の提案がある場合は、ぜひご協力ください！ [GitHub で編集する](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxKVCache/en.md)

Flux KV Cache ノードは、Flux ファミリーモデルに Key-Value (KV) キャッシュ最適化を適用します。この最適化は、特定の計算をキャッシュすることで参照画像を使用する際のパフォーマンスを向上させるために特別に設計されており、生成プロセスを高速化できます。

## 入力

| パラメータ | データ型 | 必須 | 範囲 | 説明 |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | はい | | KV キャッシュを適用するモデル。 |

## 出力

| 出力名 | データ型 | 説明 |
|-------------|-----------|-------------|
| `model` | MODEL | KV キャッシュが有効になったパッチ適用済みモデル。 |