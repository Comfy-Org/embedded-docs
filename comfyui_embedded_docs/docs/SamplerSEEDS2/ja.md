# SamplerSEEDS2

このノードは、画像生成用の設定可能なサンプラーを提供します。これは、確率微分方程式（SDE）ソルバーであるSEEDS-2アルゴリズムを実装しています。パラメータを調整することで、`seeds_2`、`exp_heun_2_x0`、`exp_heun_2_x0_sde` などの特定のサンプラーとして動作するように設定できます。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `solver_type` | サンプラーの基盤となるソルバーアルゴリズムを選択します。 | COMBO | はい | `"phi_1"`<br>`"phi_2"` |
| `eta` | 確率的な強度（デフォルト: 1.0）。 | FLOAT | いいえ | 0.0 - 100.0 |
| `s_noise` | SDEノイズ乗数（デフォルト: 1.0）。 | FLOAT | いいえ | 0.0 - 100.0 |
| `r` | 中間ステージ（c2ノード）の相対ステップサイズ（デフォルト: 0.5）。 | FLOAT | いいえ | 0.01 - 1.0 |

パラメータの設定に応じて、このサンプラーは次のサンプラーを表現できます：

- `seeds_2` — デフォルト設定
- `exp_heun_2_x0` — `solver_type`=`phi_2`, `r`=1.0, `eta`=0.0
- `exp_heun_2_x0_sde` — `solver_type`=`phi_2`, `r`=1.0, `eta`=1.0, `s_noise`=1.0

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `sampler` | 他のサンプリングノードに渡すことができる、設定済みのサンプラーオブジェクト。 | SAMPLER |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerSEEDS2/ja.md)

---
**Source fingerprint (SHA-256):** `f48744a706a49ef93d41845bf8c308af971853f6150afd00ded45f0317ffc4f9`
