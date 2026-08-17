# VOIDInpaintConditioning

VOIDInpaintConditioning ノードは、CogVideoX モデルでインペイントを行うために必要な conditioning データを準備します。ソースビデオと前処理済みのクワッドマスクを VAE でエンコードし、それらを 32 チャンネルの conditioning 信号（16 チャンネルのマスク＋16 チャンネルのマスク済みビデオ）に結合します。この信号をモデルが使用して、マスクされた領域を補完します。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `positive` | インペイント用の潜在情報で拡張されるポジティブ conditioning | CONDITIONING | はい | - |
| `negative` | インペイント用の潜在情報で拡張されるネガティブ conditioning | CONDITIONING | はい | - |
| `vae` | マスクとマスク済みビデオを潜在空間にエンコードするために使用される VAE モデル | VAE | はい | - |
| `video` | ソースビデオのフレーム [T, H, W, 3] | IMAGE | はい | - |
| `quadmask` | VOIDQuadmaskPreprocess から出力される前処理済みクワッドマスク [T, H, W] | MASK | はい | - |
| `width` | ビデオとマスクをリサイズする幅（デフォルト: 672） | INT | はい | 16 to MAX_RESOLUTION (step: 8) |
| `height` | ビデオとマスクをリサイズする高さ（デフォルト: 384） | INT | はい | 16 to MAX_RESOLUTION (step: 8) |
| `length` | 処理するピクセルフレーム数。CogVideoX-Fun-V1.5（patch_size_t=2）では latent_t が偶数である必要があり、latent_t が奇数になる長さは切り捨てられます（例: 49 → 45）（デフォルト: 45） | INT | はい | 1 to MAX_RESOLUTION (step: 1) |
| `batch_size` | 出力ノイズ潜在変数のバッチサイズ（デフォルト: 1） | INT | はい | 1 to 64 |

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `positive` | インペイント用の潜在情報が追加されたポジティブ conditioning | CONDITIONING |
| `negative` | インペイント用の潜在情報が追加されたネガティブ conditioning | CONDITIONING |
| `latent` | 形状 [batch_size, 16, latent_t, latent_h, latent_w] のゼロ埋めされたノイズ潜在テンソル | LATENT |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDInpaintConditioning/ja.md)

---
**Source fingerprint (SHA-256):** `885e462c0f17a3e9610146a05ba3b9c879db0112d3961c95a83f63ba2cd511f1`
