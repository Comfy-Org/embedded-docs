# Runway 圖片轉影片 (Gen3a Turbo)

此節點使用 Runway 的 Gen3a Turbo 模型，從單一起始幀生成影片。它接受文字提示詞和初始影像幀，然後根據指定的時長和長寬比建立影片序列。此節點會連線至 Runway 的 API 以遠端處理生成作業。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 生成作業的文字提示詞（預設值：""） | STRING | 是 | N/A |
| `start_frame` | 用於影片的起始幀 | IMAGE | 是 | N/A |
| `duration` | 影片時長（秒）（預設值："5"） | COMBO | 是 | `"5"`<br>`"10"` |
| `ratio` | 生成影片的長寬比（預設值："768:1280"） | COMBO | 是 | `"768:1280"`<br>`"1280:768"` |
| `seed` | 生成作業的隨機種子（預設值：0） | INT | 否 | 0 至 4294967295 |

**參數約束：**

- `start_frame` 的尺寸不得超過 7999x7999 像素。
- `start_frame` 的長寬比必須介於 0.5 至 2.0 之間。
- `prompt` 必須包含至少一個字元（不可為空）。

**備註：**

- 此節點已棄用。
- 生成之前，Runway 建議參閱其最佳實務指南：https://help.runwayml.com/hc/en-us/articles/33927968552339-Creating-with-Act-One-on-Gen-3-Alpha-and-Turbo

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `output` | 生成的影片序列 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RunwayImageToVideoNodeGen3a/zh-TW.md)

---
**Source fingerprint (SHA-256):** `ff66cbdfa80aabeaf96d43e7822dd0c700ee027d13fb430a9dc2079e1a23f38e`
