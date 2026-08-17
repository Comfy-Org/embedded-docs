# ModelComputeDtype

ModelComputeDtype ノードは、処理中にモデルで使用される計算データ型（精度）を変更します。入力モデルのコピーを作成し、選択した精度設定を適用します。これにより、ハードウェアに応じてメモリ使用量とパフォーマンスを最適化できます。さまざまな精度構成のデバッグやテストに役立ちます。

## 入力

| パラメーター | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `model` | 新しい計算データ型を適用する入力モデル | MODEL | はい | - |
| `dtype` | モデルに適用する計算データ型（デフォルト："default"）。このパラメーターは、UI では詳細設定としてマークされています。 | COMBO | はい | "default"<br>"fp32"<br>"fp16"<br>"bf16" |

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `model` | 新しい計算データ型が適用された変更済みモデル | MODEL |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelComputeDtype/ja.md)

---
**Source fingerprint (SHA-256):** `ad9c39e1217fd2e343ad4f49df9d1acabbc4708966dadec5340bb975adb59854`
