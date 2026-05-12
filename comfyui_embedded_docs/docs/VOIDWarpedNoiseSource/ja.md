> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDWarpedNoiseSource/ja.md)

以下が翻訳結果です。

## 概要

このノードは、LATENT（例：VOIDWarpedNoiseノードの出力）をNOISEソースに変換します。これにより、歪みノイズをSamplerCustomAdvancedノードで使用し、より制御された画像生成が可能になります。

## 入力

| パラメータ | データ型 | 必須 | 範囲 | 説明 |
|-----------|-----------|----------|-------|-------------|
| `warped_noise` | LATENT | はい | なし | VOIDWarpedNoiseからの歪みノイズの潜在表現 |

## 出力

| 出力名 | データ型 | 説明 |
|-------------|-----------|-------------|
| `NOISE` | NOISE | SamplerCustomAdvancedで使用可能なノイズソース |