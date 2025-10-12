> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_SuperResolutionControlnet/ja.md)

StableCascade_SuperResolutionControlnetノードは、Stable Cascadeの超解像処理のための入力を準備します。入力画像を受け取り、VAEを使用してエンコードし、コントロールネットの入力を作成すると同時に、Stable CascadeパイプラインのステージCとステージBのプレースホルダー潜在表現を生成します。

## 入力

| パラメータ | データ型 | 必須 | 範囲 | 説明 |
|-----------|-----------|----------|-------|-------------|
| `画像` | IMAGE | はい | - | 超解像処理のために処理される入力画像 |
| `vae` | VAE | はい | - | 入力画像のエンコードに使用されるVAEモデル |

## 出力

| 出力名 | データ型 | 説明 |
|-------------|-----------|-------------|
| `ステージC` | IMAGE | コントロールネット入力に適したエンコードされた画像表現 |
| `ステージB` | LATENT | Stable Cascade処理のステージC用のプレースホルダー潜在表現 |
| `stage_b` | LATENT | Stable Cascade処理のステージB用のプレースホルダー潜在表現 |