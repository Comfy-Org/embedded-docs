# SamplerLCM

SamplerLCM ノードは、調整可能なステップごとのノイズ設定を備えた LCM（Latent Consistency Model）サンプラーを提供します。`s_noise` パラメータは、モデルのトレーニング時のノイズスケールに対する乗数として機能し、各サンプリングステップで適用されるノイズを細かく制御できます。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `s_noise` | 最初のステップにおけるステップごとのノイズ乗数（1.0 = トレーニングに一致）。デフォルト: 1.0。 | FLOAT | はい | 0.0 to 64.0 (step: 0.01) |
| `s_noise_end` | 最後のステップにおけるステップごとのノイズ乗数。一定のスケジュールにするには `s_noise` と同じ値を設定します。デフォルト: 1.0。 | FLOAT | はい | 0.0 to 64.0 (step: 0.01) |
| `noise_clip_std` | ステップごとのノイズを +/- N*std にクランプします。0 で無効になります。デフォルト: 0.0。 | FLOAT | はい | 0.0 to 10.0 (step: 0.01) |

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `SAMPLER` | 設定済みの LCM サンプラーオブジェクト。サンプリングワークフローで使用する準備ができています。 | SAMPLER |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerLCM/ja.md)

---
**Source fingerprint (SHA-256):** `0d18f2f977ddadeedcd7807233b48ebcc4e94c6213f8540b9037a45a9c70c6cf`
