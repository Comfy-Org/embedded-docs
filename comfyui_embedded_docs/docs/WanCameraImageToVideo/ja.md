> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanCameraImageToVideo/ja.md)

WanCameraImageToVideoノードは、画像をビデオシーケンスに変換するために、ビデオ生成用の潜在表現を生成します。このノードは、コンディショニング入力とオプションの開始画像を処理し、ビデオモデルで使用できるビデオ潜在表現を作成します。ノードは、カメラ条件とCLIP vision出力をサポートしており、ビデオ生成の制御を強化します。

## 入力

| パラメータ | データ型 | 必須 | 範囲 | 説明 |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | はい | - | ビデオ生成用のポジティブなコンディショニングプロンプト |
| `negative` | CONDITIONING | はい | - | ビデオ生成で避けたいネガティブなコンディショニングプロンプト |
| `vae` | VAE | はい | - | 画像を潜在空間にエンコードするためのVAEモデル |
| `width` | INT | はい | 16 から MAX_RESOLUTION | 出力ビデオの幅（ピクセル単位）（デフォルト: 832, ステップ: 16） |
| `height` | INT | はい | 16 から MAX_RESOLUTION | 出力ビデオの高さ（ピクセル単位）（デフォルト: 480, ステップ: 16） |
| `length` | INT | はい | 1 から MAX_RESOLUTION | ビデオシーケンスのフレーム数（デフォルト: 81, ステップ: 4） |
| `batch_size` | INT | はい | 1 から 4096 | 同時に生成するビデオの数（デフォルト: 1） |
| `clip_vision_output` | CLIP_VISION_OUTPUT | いいえ | - | 追加のコンディショニング用のオプションのCLIP vision出力 |
| `start_image` | IMAGE | いいえ | - | ビデオシーケンスを初期化するためのオプションの開始画像 |
| `camera_conditions` | WAN_CAMERA_EMBEDDING | いいえ | - | ビデオ生成用のオプションのカメラ埋め込み条件 |

**注記:** `start_image`が提供された場合、ノードはそれを使用してビデオシーケンスを初期化し、マスキングを適用して開始フレームと生成されたコンテンツをブレンドします。`camera_conditions`と`clip_vision_output`パラメータはオプションですが、提供された場合、これらはポジティブとネガティブの両方のプロンプトのコンディショニングを変更します。

## 出力

| 出力名 | データ型 | 説明 |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | カメラ条件とCLIP vision出力が適用された修正済みポジティブコンディショニング |
| `negative` | CONDITIONING | カメラ条件とCLIP vision出力が適用された修正済みネガティブコンディショニング |
| `latent` | LATENT | ビデオモデルで使用するための生成されたビデオ潜在表現 |
