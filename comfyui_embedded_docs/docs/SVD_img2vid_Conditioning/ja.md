> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SVD_img2vid_Conditioning/ja.md)

SVD_img2vid_Conditioning ノードは、Stable Video Diffusion を使用した動画生成のための条件付けデータを準備します。初期画像を受け取り、CLIP vision エンコーダーと VAE エンコーダーを通して処理し、ポジティブおよびネガティブな条件付けペアと、動画生成用の空の潜在空間を作成します。このノードは、生成される動画における動き、フレームレート、および拡張レベルの制御に必要なパラメーターを設定します。

## 入力

| パラメータ | データ型 | 必須 | 範囲 | 説明 |
|-----------|-----------|----------|-------|-------------|
| `clip_vision` | CLIP_VISION | はい | - | 入力画像をエンコードするためのCLIP visionモデル |
| `init_image` | IMAGE | はい | - | 動画生成の開始点として使用する初期画像 |
| `vae` | VAE | はい | - | 画像を潜在空間にエンコードするためのVAEモデル |
| `width` | INT | はい | 16 ～ MAX_RESOLUTION | 出力動画の幅（デフォルト：1024、ステップ：8） |
| `height` | INT | はい | 16 ～ MAX_RESOLUTION | 出力動画の高さ（デフォルト：576、ステップ：8） |
| `video_frames` | INT | はい | 1 ～ 4096 | 動画内で生成するフレーム数（デフォルト：14） |
| `motion_bucket_id` | INT | はい | 1 ～ 1023 | 生成される動画の動きの量を制御します（デフォルト：127） |
| `fps` | INT | はい | 1 ～ 1024 | 生成される動画のフレームレート（デフォルト：6） |
| `augmentation_level` | FLOAT | はい | 0.0 ～ 10.0 | 入力画像に適用するノイズ拡張のレベル（デフォルト：0.0、ステップ：0.01） |

## 出力

| 出力名 | データ型 | 説明 |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | 画像埋め込みと動画パラメーターを含むポジティブ条件付けデータ |
| `negative` | CONDITIONING | ゼロ埋めされた埋め込みと動画パラメーターを含むネガティブ条件付けデータ |
| `latent` | LATENT | 動画生成の準備が整った空の潜在空間テンソル |

---
**Source fingerprint (SHA-256):** `33b295b6f2e459852aaa95d9dca26c724aa2e9ad0f884a1c7760766530a00a09`
