# FluxKontextMultiReferenceLatentMethod

The FluxKontextMultiReferenceLatentMethod ノードは、特定の参照ラテント手法を設定することで条件付けデータを変更します。選択された手法を条件付け入力に追加し、その後の生成ステップで参照ラテントが処理される方法に影響を与えます。このノードは実験的としてマークされており、Flux 条件付けシステムの一部です。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `conditioning` | 参照ラテント手法で変更される条件付けデータです。 | CONDITIONING | はい | - |
| `reference_latents_method` | 参照ラテント処理に使用する手法です。「uxo」または「uso」が選択された場合は「uxo」に変換されます。このパラメータは上級者向けです。 | COMBO | はい | `"offset"`<br>`"index"`<br>`"uxo/uno"`<br>`"index_timestep_zero"` |

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `conditioning` | 参照ラテント手法が適用された変更後の条件付けデータです。 | CONDITIONING |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxKontextMultiReferenceLatentMethod/ja.md)

---
**Source fingerprint (SHA-256):** `cbe069d0c9f8adbf7f8c909b1cd644d9cd3730e934f0e5856213ff06fa8ecc56`
