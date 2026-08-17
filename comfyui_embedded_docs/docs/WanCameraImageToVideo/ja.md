# WanCameraImageToVideo

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `positive` | ビデオ生成のための正のコンディショニングプロンプト | CONDITIONING | 必須 | - |
| `negative` | ビデオ生成で回避するための負のコンディショニングプロンプト | CONDITIONING | 必須 | - |
| `vae` | 画像を潜在空間にエンコードするためのVAEモデル | VAE | 必須 | - |
| `width` | 出力ビデオの幅（ピクセル単位）（デフォルト: 832、ステップ: 16） | INT | 必須 | 16 to MAX_RESOLUTION |
| `height` | 出力ビデオの高さ（ピクセル単位）（デフォルト: 480、ステップ: 16） | INT | 必須 | 16 to MAX_RESOLUTION |
| `length` | ビデオシーケンスのフレーム数（デフォルト: 81、ステップ: 4） | INT | 必須 | 1 to MAX_RESOLUTION |
| `batch_size` | 同時に生成するビデオの数（デフォルト: 1） | INT | 必須 | 1 to 4096 |
| `clip_vision_output` | 追加のコンディショニング用のオプションのCLIPビジョン出力 | CLIP_VISION_OUTPUT | 任意 | - |
| `start_image` | ビデオシーケンスを初期化するためのオプションの開始画像。指定すると、ビデオの最初のフレームがこの画像に基づき、開始フレームと生成コンテンツをブレンドするマスクが適用されます。画像は指定された幅と高さにリサイズされます。 | IMAGE | 任意 | - |
| `camera_conditions` | ビデオ生成用のオプションのカメラ埋め込み条件。指定すると、これらの条件は正と負の両方のコンディショニングに適用されます。 | WAN_CAMERA_EMBEDDING | 任意 | - |

**注:** `start_image` を指定すると、ノードはそれを使用してビデオシーケンスを初期化し、開始フレームと生成コンテンツをブレンドするマスクを適用します。`camera_conditions` と `clip_vision_output` はオプションですが、指定すると正と負の両方のプロンプトのコンディショニングを変更します。

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `positive` | カメラ条件、CLIPビジョン出力、および/または開始画像データが適用された、変更後の正のコンディショニング | CONDITIONING |
| `negative` | カメラ条件、CLIPビジョン出力、および/または開始画像データが適用された、変更後の負のコンディショニング | CONDITIONING |
| `latent` | ビデオモデルで使用するために生成された空のビデオ潜在表現。潜在テンソルの次元は [batch_size, 16, frames, height/8, width/8] で、frames は ((length - 1) // 4) + 1 として計算されます。 | LATENT |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanCameraImageToVideo/ja.md)

---
**Source fingerprint (SHA-256):** `467a82be0dfd6ac1c3b2dd2a6cb02e0d0749de4536a7fbdb000456b817b20ebb`
