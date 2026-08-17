# AV Latentを分離

LTXVSeparateAVLatent ノードは、結合された音声・映像の潜在表現を受け取り、それを映像用と音声用の2つの別々の潜在表現に分割します。LTXV や MiniMax H3 など、あらゆる音声・映像モデルで動作します。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `av_latent` | 分割対象の結合された音声・映像の潜在表現です。 | LATENT | はい | N/A |

**注意:** 入力潜在表現の `samples` テンソルは、最初の次元（バッチ次元）に少なくとも2つの要素を持つことが期待されます。最初の要素は映像潜在表現に使用され、2番目の要素は音声潜在表現に使用されます。`noise_mask` が存在する場合、同じ方法で分割されます。

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `video_latent` | 分割された映像データを含む潜在表現です。 | LATENT |
| `audio_latent` | 分割された音声データを含む潜在表現です。 | LATENT |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVSeparateAVLatent/ja.md)

---
**Source fingerprint (SHA-256):** `22ed38bbc1b5716cee380c35c50455810f79c273f51bbe6a535c9ae33192afe6`
