# サンプラーDPMPP_2M_SDE

SamplerDPMPP_2M_SDE ノードは、拡散モデル用の DPM++ 2M SDE サンプラーを作成します。このサンプラーは、2次マルチステップソルバーと確率微分方程式（SDE）ノイズを組み合わせてサンプルを生成します。サンプリングプロセスを制御するために、さまざまなソルバータイプとノイズ処理オプションを提供します。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `solver_type` | サンプリング中に使用する微分方程式ソルバーのタイプ："midpoint" または "heun"（デフォルト: "midpoint"） | COMBO | はい | "midpoint"<br>"heun" |
| `eta` | サンプリングプロセスにおける確率性（ランダム性）の量を制御します（デフォルト: 1.0） | FLOAT | はい | 0.0 - 100.0 |
| `s_noise` | サンプリング中に追加されるノイズの量を制御します（デフォルト: 1.0） | FLOAT | はい | 0.0 - 100.0 |
| `noise_device` | ノイズ計算に使用するデバイス。"gpu" は GPU 上でノイズ生成を行い、場合によってはより高速なパフォーマンスを実現します。"cpu" は CPU を使用します（デフォルト: "gpu"） | COMBO | はい | "gpu"<br>"cpu" |

注意：`noise_device` が "cpu" に設定されている場合、ノードは `dpmpp_2m_sde` サンプラーを作成します。"gpu" に設定されている場合は、GPU 上でノイズ関連の計算を実行する `dpmpp_2m_sde_gpu` バリアントを作成します。

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `sampler` | サンプリングパイプラインで使用できる状態に設定されたサンプラーオブジェクト | SAMPLER |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDPMPP_2M_SDE/ja.md)

---
**Source fingerprint (SHA-256):** `42f5f098fa7573ca8a1a6085b72675ee6cb0ae8e7865c5793a815a6ef2495f82`
