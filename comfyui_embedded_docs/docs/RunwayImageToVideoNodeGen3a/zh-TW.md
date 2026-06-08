# Runway 影像轉影片 (Gen3a Turbo) 節點

Runway 影像轉影片 (Gen3a Turbo) 節點使用 Runway 的 Gen3a Turbo 模型，從單一起始影格生成影片。它接收文字提示和初始影像影格，然後根據指定的持續時間和長寬比建立影片序列。此節點連接到 Runway 的 API 以遠端處理生成作業。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `提示詞` | 生成用的文字提示（預設值：""） | STRING | 是 | N/A |
| `起始幀` | 用於影片的起始影格 | IMAGE | 是 | N/A |
| `持續時間` | 影片持續時間（秒）（預設值："5"） | COMBO | 是 | `"5"`<br>`"10"` |
| `比例` | 生成影片的長寬比（預設值："1280x720"） | COMBO | 是 | `"1280x720"`<br>`"720x1280"`<br>`"1920x1080"`<br>`"1080x1920"`<br>`"1080x1080"` |
| `種子值` | 生成用的隨機種子（預設值：0） | INT | 否 | 0 至 4294967295 |

**參數限制：**

- `start_frame` 的尺寸不得超過 7999x7999 像素。
- `start_frame` 的長寬比必須介於 0.5 到 2.0 之間。
- `prompt` 必須包含至少一個字元（不能為空）。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `output` | 生成的影片序列 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RunwayImageToVideoNodeGen3a/zh-TW.md)

---
**Source fingerprint (SHA-256):** `4f3270ce070ce50580699292e21c5f9e3b1a56dd8ac981f67a9026ef6fc8ed76`
