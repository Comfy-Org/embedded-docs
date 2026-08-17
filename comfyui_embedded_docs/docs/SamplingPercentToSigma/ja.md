# SamplingPercentToSigma

The SamplingPercentToSigma ノードは、モデルのサンプリングパラメータを使用して、サンプリングパーセント値を対応するシグマ値に変換します。0.0 から 1.0 の間のパーセント値を受け取り、モデルのノイズスケジュール内の適切なシグマ値にマッピングします。計算されたシグマ値、または境界における実際の最大/最小シグマ値のいずれかを返すオプションがあります。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `model` | 変換に使用するサンプリングパラメータを含むモデル | MODEL | はい | - |
| `sampling_percent` | シグマに変換するサンプリングパーセント（デフォルト: 0.0） | FLOAT | はい | 0.0 から 1.0（ステップ: 0.0001） |
| `return_actual_sigma` | 間隔チェックに使用される値ではなく、実際のシグマ値を返します。これは 0.0 と 1.0 の結果にのみ影響します（デフォルト: False） | BOOLEAN | はい | - |

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `sigma_value` | 入力されたサンプリングパーセントに対応する変換済みのシグマ値 | FLOAT |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplingPercentToSigma/ja.md)

---
**Source fingerprint (SHA-256):** `30decf1d4804accbdf2a70eba1a773b41ef0e09cfb74f2a9388044dadf0a1ac1`
