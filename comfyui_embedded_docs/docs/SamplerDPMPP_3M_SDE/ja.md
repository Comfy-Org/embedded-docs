# サンプラーDPMPP_3M_SDE

SamplerDPMPP_3M_SDE ノードは、サンプリングプロセスで使用する DPM++ 3M SDE サンプラーを作成します。このサンプラーは、ノイズパラメータを設定可能な3次マルチステップ確率微分方程式法を使用します。このノードでは、ノイズ計算を GPU と CPU のどちらで実行するかを選択できます。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `eta` | サンプリングプロセスの確率性を制御します（デフォルト: 1.0） | FLOAT | はい | 0.0 - 100.0 |
| `s_noise` | サンプリング中に追加されるノイズの量を制御します（デフォルト: 1.0） | FLOAT | はい | 0.0 - 100.0 |
| `noise_device` | ノイズ計算を行うデバイスを選択します（GPU または CPU、デフォルト: "gpu"） | COMBO | はい | "gpu"<br>"cpu" |

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `sampler` | サンプリングワークフローで使用する設定済みサンプラーオブジェクトを返します | SAMPLER |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDPMPP_3M_SDE/ja.md)

---
**Source fingerprint (SHA-256):** `0f624398c67e50639fc41384b50b91bab93797bd785dda25f1f5fc649e46825b`
