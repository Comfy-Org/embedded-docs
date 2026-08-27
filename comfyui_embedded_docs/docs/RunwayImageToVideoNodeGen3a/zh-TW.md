# Runway 圖片轉影片 (Gen3a Turbo)

Runway Image to Video (Gen3a Turbo) 節點使用 Runway 的 Gen3a Turbo 模型，從單一起始畫面產生影片。它接收文字提示和初始影像畫面，然後根據指定的持續時間和長寬比建立影片序列。此節點連接 Runway 的 API 來遠端處理產生作業。Runway 建議在產生前先檢閱其最佳實務指南：https://help.runwayml.com/hc/en-us/articles/33927968552339-Creating-with-Act-One-on-Gen-3-Alpha-and-Turbo。此節點已標記為已棄用。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `提示詞` | 用於產生的文字提示（預設：""） | STRING | 是 | N/A |
| `起始幀` | 用於影片的起始畫面 | IMAGE | 是 | N/A |
| `持續時間` | 影片持續時間（秒）（預設："5"） | COMBO | 是 | `"5"`<br>`"10"` |
| `比例` | 產生影片的長寬比（預設："768:1280"） | COMBO | 是 | `"768:1280"`<br>`"1280:768"` |
| `種子值` | 用於產生的隨機種子（預設：0） | INT | 是 | 0 至 4294967295 |

**參數限制：**

- `start_frame` 的尺寸不得超過 7999x7999 像素。
- `start_frame` 的長寬比必須介於 0.5 與 2.0 之間。
- `start_frame` 接受單一影像（最多 1 張）。
- `prompt` 必須包含至少一個字元（不能為空）。

## 輸出

| 輸出名 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `output` | 產生的影片序列 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RunwayImageToVideoNodeGen3a/zh-TW.md)

---
**Source fingerprint (SHA-256):** `ff66cbdfa80aabeaf96d43e7822dd0c700ee027d13fb430a9dc2079e1a23f38e`
