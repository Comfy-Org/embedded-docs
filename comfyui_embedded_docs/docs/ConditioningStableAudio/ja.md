# ConditioningStableAudio

ConditioningStableAudioノードは、オーディオ生成用のポジティブおよびネガティブなconditioning入力にタイミング情報を追加します。このノードは、オーディオコンテンツをいつ、どのくらいの長さで生成するかを制御する開始時間と合計期間のパラメータを設定します。既存のconditioningデータにオーディオ固有のタイミングメタデータを追加することで、conditioningデータを変更します。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `positive` | オーディオタイミング情報で変更されるポジティブなconditioning入力です。 | CONDITIONING | はい | - |
| `negative` | オーディオタイミング情報で変更されるネガティブなconditioning入力です。 | CONDITIONING | はい | - |
| `seconds_start` | オーディオ生成の開始時間（秒）です（デフォルト: 0.0）。 | FLOAT | はい | 0.0 to 1000.0 |
| `seconds_total` | オーディオ生成の合計時間（秒）です（デフォルト: 47.0）。 | FLOAT | はい | 0.0 to 1000.0 |

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `positive` | オーディオタイミング情報が適用された、変更済みのポジティブなconditioningです。 | CONDITIONING |
| `negative` | オーディオタイミング情報が適用された、変更済みのネガティブなconditioningです。 | CONDITIONING |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningStableAudio/ja.md)

---
**Source fingerprint (SHA-256):** `8bdf29514002837090c549b9921e8cb19c07d385881fe09a58885fcbfe968261`
