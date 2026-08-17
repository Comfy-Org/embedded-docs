# VAEでControlNetを適用

このノードは、Stable Diffusion 3のコンディショニングにControlNetガイダンスを適用します。ポジティブおよびネガティブのコンディショニング入力を、ControlNetモデルと画像とともに受け取り、調整可能な強度とタイミングパラメータでコントロールガイダンスを適用して、生成プロセスに影響を与えます。

**注記:** このノードは非推奨としてマークされており、将来のバージョンで削除される可能性があります。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `positive` | ControlNetガイダンスを適用するポジティブなコンディショニング | CONDITIONING | はい | - |
| `negative` | ControlNetガイダンスを適用するネガティブなコンディショニング | CONDITIONING | はい | - |
| `control_net` | ガイダンスに使用するControlNetモデル | CONTROL_NET | はい | - |
| `vae` | プロセスで使用されるVAEモデル | VAE | はい | - |
| `image` | ControlNetがガイダンスとして使用する入力画像 | IMAGE | はい | - |
| `strength` | ControlNet効果の強さ（デフォルト: 1.0） | FLOAT | はい | 0.0 - 10.0 |
| `start_percent` | ControlNetが適用され始める生成プロセスの開始点（デフォルト: 0.0） | FLOAT | はい | 0.0 - 1.0 |
| `end_percent` | ControlNetの適用が終了する生成プロセスの終了点（デフォルト: 1.0） | FLOAT | はい | 0.0 - 1.0 |

**注記:** `strength`が0に設定されている場合、このノードはControlNetを適用せず、ポジティブおよびネガティブのコンディショニングを変更せずに返します。

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `positive` | ControlNetガイダンスが適用された変更後のポジティブなコンディショニング | CONDITIONING |
| `negative` | ControlNetガイダンスが適用された変更後のネガティブなコンディショニング | CONDITIONING |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ControlNetApplySD3/ja.md)

---
**Source fingerprint (SHA-256):** `b76b0683c05e38102280ca8b0bd23f39a9b9b1b4f52125c77c95686c0a06f398`
