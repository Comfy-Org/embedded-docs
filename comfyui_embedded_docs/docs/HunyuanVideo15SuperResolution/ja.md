> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanVideo15SuperResolution/ja.md)

HunyuanVideo15SuperResolutionノードは、動画の超解像処理のための条件付けデータを準備します。動画の潜在表現と、オプションで開始画像を受け取り、それらをノイズ増強とCLIP visionデータと共にパッケージ化し、モデルが高解像度の出力を生成するために使用できる形式に変換します。

## 入力

| パラメータ | データ型 | 必須 | 範囲 | 説明 |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | はい | N/A | 潜在データと増強データで修正される、ポジティブな条件付け入力です。 |
| `negative` | CONDITIONING | はい | N/A | 潜在データと増強データで修正される、ネガティブな条件付け入力です。 |
| `vae` | VAE | いいえ | N/A | オプションの`start_image`をエンコードするために使用するVAEです。`start_image`が提供される場合は必須です。 |
| `start_image` | IMAGE | いいえ | N/A | 超解像をガイドするためのオプションの開始画像です。提供された場合、アップスケールされて条件付けの潜在表現にエンコードされます。 |
| `clip_vision_output` | CLIP_VISION_OUTPUT | いいえ | N/A | 条件付けに追加するためのオプションのCLIP vision埋め込みです。 |
| `latent` | LATENT | はい | N/A | 条件付けに組み込まれる、入力となる潜在動画表現です。 |
| `noise_augmentation` | FLOAT | いいえ | 0.0 - 1.0 | 条件付けに適用するノイズ増強の強度です（デフォルト: 0.70）。 |

**注意:** `start_image`を提供する場合は、それをエンコードするために`vae`も接続する必要があります。`start_image`は、入力`latent`が示す寸法に一致するように自動的にアップスケールされます。

## 出力

| 出力名 | データ型 | 説明 |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | 修正されたポジティブな条件付けです。連結された潜在表現、ノイズ増強、およびオプションのCLIP visionデータが含まれています。 |
| `negative` | CONDITIONING | 修正されたネガティブな条件付けです。連結された潜在表現、ノイズ増強、およびオプションのCLIP visionデータが含まれています。 |
| `latent` | LATENT | 入力された潜在表現が変更されずに通過します。 |
