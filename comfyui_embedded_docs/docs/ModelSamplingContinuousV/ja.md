# モデルサンプリング連続V

以下に、英語ドキュメントを日本語に翻訳しました。

---

ModelSamplingContinuousV ノードは、連続的な V-prediction サンプリングパラメータを適用することで、モデルのサンプリング動作を変更します。入力モデルのクローンを作成し、高度なサンプリング制御のためのカスタムシグマ範囲設定を構成します。これにより、ユーザーは特定の最小・最大シグマ値でサンプリングプロセスを微調整できます。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `model` | 連続 V-prediction サンプリングで変更する入力モデル | MODEL | はい | - |
| `sampling` | 適用するサンプリング方法。現在は V-prediction のみがサポートされています。 | COMBO | はい | `"v_prediction"` |
| `sigma_max` | サンプリングの最大シグマ値（デフォルト：500.0） | FLOAT | はい | 0.0 – 1000.0（ステップ 0.001） |
| `sigma_min` | サンプリングの最小シグマ値（デフォルト：0.03） | FLOAT | はい | 0.0 – 1000.0（ステップ 0.001） |

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `model` | 連続 V-prediction サンプリングが適用された変更済みモデル | MODEL |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingContinuousV/ja.md)

---
**Source fingerprint (SHA-256):** `8549be9dd2375374c20da7c74a756a90285716db0e52fed8a1a2b753cd6d75fe`
