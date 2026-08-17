# 條件設定（Stable Audio）

ConditioningStableAudio 節點會為正向與負向 conditioning 輸入加入時間資訊，以用於音訊生成。它設定開始時間與總持續時間參數，協助控制應生成音訊內容的時機與長度。此節點透過附加音訊專用的時間元資料來修改現有的 conditioning 資料。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `positive` | 要使用音訊時間資訊修改的正向 conditioning 輸入 | CONDITIONING | 是 | - |
| `negative` | 要使用音訊時間資訊修改的負向 conditioning 輸入 | CONDITIONING | 是 | - |
| `seconds_start` | 音訊生成的起始時間（秒）（預設值：0.0） | FLOAT | 是 | 0.0 to 1000.0 |
| `seconds_total` | 音訊生成的總持續時間（秒）（預設值：47.0） | FLOAT | 是 | 0.0 to 1000.0 |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `positive` | 已套用音訊時間資訊的修改後正向 conditioning | CONDITIONING |
| `negative` | 已套用音訊時間資訊的修改後負向 conditioning | CONDITIONING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningStableAudio/zh-TW.md)

---
**Source fingerprint (SHA-256):** `8bdf29514002837090c549b9921e8cb19c07d385881fe09a58885fcbfe968261`
