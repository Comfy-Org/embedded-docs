# Runway 圖片轉影片 (Gen3a Turbo)

Runway Image to Video (Gen3a Turbo) 節點會使用 Runway 的 Gen3a Turbo 模型，從單一起始影格生成影片。它接受文字提示與初始影像影格，然後根據指定的持續時間與長寬比建立影片序列。生成作業會透過 Runway 的 API 遠端處理。此節點已標記為已棄用。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `提示詞` | 用於生成的文字提示（預設值：""） | STRING | 是 | N/A |
| `起始幀` | 用於影片的起始影格 | IMAGE | 是 | N/A |
| `持續時間` | 生成影片的持續時間，以秒為單位（預設值："5"） | COMBO | 是 | `"5"`<br>`"10"` |
| `比例` | 生成影片的長寬比（預設值："768:1280"） | COMBO | 是 | `"768:1280"`<br>`"1280:768"` |
| `種子值` | 生成用的隨機種子（預設值：0） | INT | 是 | 0 至 4294967295 |

**參數限制：**

- `prompt` 必須至少包含一個字元（不能為空）。
- `start_frame` 接受單一影像（最多 1 張）。
- `start_frame` 的尺寸不得超過 7999 x 7999 像素。
- `start_frame` 的長寬比必須介於 1:2 與 2:1 之間（0.5 到 2.0）。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `output` | 生成的影片序列 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RunwayImageToVideoNodeGen3a/zh-TW.md)

---
**Source fingerprint (SHA-256):** `ff66cbdfa80aabeaf96d43e7822dd0c700ee027d13fb430a9dc2079e1a23f38e`
