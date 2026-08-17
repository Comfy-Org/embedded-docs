# モデルサンプリングSD3

ModelSamplingSD3 ノードは、Stable Diffusion 3 のサンプリングパラメータをモデルに適用します。shift パラメータを調整することでモデルのサンプリング動作を変更し、サンプリング分布の特性を制御します。このノードは、指定されたサンプリング設定が適用された入力モデルの変更済みコピーを作成します。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `model` | SD3 サンプリングパラメータを適用する入力モデル | MODEL | はい | - |
| `shift` | サンプリングの shift パラメータを制御します（デフォルト: 3.0） | FLOAT | はい | 0.0 - 100.0 |

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `model` | SD3 サンプリングパラメータが適用された変更済みモデル | MODEL |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingSD3/ja.md)

---
**Source fingerprint (SHA-256):** `46d44786422c2efea78c1fe7e1183cebc9bf51d4f13861da04d5a974b5b6da7d`
