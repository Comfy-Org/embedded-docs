# 安定ゼロ123条件付け

StableZero123_Conditioning ノードは、入力画像とカメラ角度を処理して、3D モデル生成用のコンディショニングデータと潜在表現を生成します。CLIP ビジョンモデルを使用して画像特徴をエンコードし、仰角と方位角に基づくカメラ埋め込み情報と組み合わせて、下流の 3D 生成タスク向けのポジティブおよびネガティブコンディショニングと潜在表現を生成します。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `clip_vision` | 画像特徴をエンコードするために使用される CLIP ビジョンモデル | CLIP_VISION | はい | - |
| `init_image` | 処理およびエンコードされる入力画像 | IMAGE | はい | - |
| `vae` | ピクセルを潜在空間にエンコードするために使用される VAE モデル | VAE | はい | - |
| `width` | 潜在表現の出力幅（デフォルト: 256、8 で割り切れる必要があります） | INT | はい | 16 から MAX_RESOLUTION |
| `height` | 潜在表現の出力高さ（デフォルト: 256、8 で割り切れる必要があります） | INT | はい | 16 から MAX_RESOLUTION |
| `batch_size` | バッチ内で生成するサンプル数（デフォルト: 1） | INT | はい | 1 から 4096 |
| `elevation` | カメラの仰角（度）（デフォルト: 0.0） | FLOAT | はい | -180.0 から 180.0 |
| `azimuth` | カメラの方位角（度）（デフォルト: 0.0） | FLOAT | はい | -180.0 から 180.0 |

**注:** `width` および `height` パラメータは 8 で割り切れる必要があります。ノードはこれらを自動的に 8 で割って潜在表現の次元を作成するためです。

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `positive` | 画像特徴とカメラ埋め込みを組み合わせたポジティブコンディショニング | CONDITIONING |
| `negative` | ゼロ初期化された特徴を持つネガティブコンディショニング | CONDITIONING |
| `latent` | 次元が [batch_size, 4, height//8, width//8] の潜在表現 | LATENT |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableZero123_Conditioning/ja.md)

---
**Source fingerprint (SHA-256):** `a694610c9f22fe0dab3ae02f4aabb33e3de8e5031c82dff5e8ba232c098f4a1d`
