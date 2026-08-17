# TripoSplatコンディショニング

このノードは、DINOv3ビジョンエンコーダーとFlux2 VAEを使用して入力画像をエンコードし、TripoSplatモデル用のポジティブおよびネガティブなコンディショニングデータを生成します。また、KSamplerの開始点となる固定サイズのノイズターゲット（潜在シーケンスとカメラトークン）も生成します。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
|-----------|-------------|-----------|----------|-------|
| `clip_vision` | DINOv3 ViT-H/16+ 画像エンコーダー | CLIP_VISION | はい | - |
| `vae` | Flux2 VAE | VAE | はい | - |
| `image` | エンコードする入力画像 | IMAGE | はい | - |

## 出力

| 出力名 | 説明 | データ型 |
|-------------|-------------|-----------|
| `positive` | DINOv3画像特徴量と入力画像のFlux2 VAE潜在変数を含むポジティブコンディショニングデータ | CONDITIONING |
| `negative` | ゼロ埋めされたDINOv3特徴量とゼロ埋めされたFlux2 VAE潜在変数を含むネガティブコンディショニングデータ | CONDITIONING |
| `latent` | KSampler用の固定サイズのノイズターゲット（潜在変数+カメラ） | LATENT |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoSplatConditioning/ja.md)

---
**Source fingerprint (SHA-256):** `59ebeef272d125a2cc2045f4ff54f99268b1273d0a1fd46f7462e6d312f3a805`
