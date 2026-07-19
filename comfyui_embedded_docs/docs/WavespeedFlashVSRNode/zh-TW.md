# FlashVSR 影片升頻

## 概述

WavespeedFlashVSRNode 是一個快速、高品質的影片放大節點，可提升解析度並還原低解析度或模糊影片的清晰度。它會處理輸入的影片，並輸出使用者選擇的更高解析度影片。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `影片` | 要進行放大的輸入影片檔案。必須為 MP4 容器格式，且時長介於 5 秒至 10 分鐘之間。 | VIDEO | 是 | 不適用 |
| `目標解析度` | 放大後輸出影片的目標解析度。 | STRING | 是 | `"720p"`<br>`"1080p"`<br>`"2K"`<br>`"4K"` |

**輸入限制：**

* 輸入的 `video` 檔案必須為 MP4 容器格式。
* 輸入 `video` 的時長必須介於 5 秒至 10 分鐘（600 秒）之間。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `output` | 以選定目標解析度輸出的放大後影片檔案。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WavespeedFlashVSRNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `9a495889753ac866177921727228846d8ef9516c54ccd9aa425350b87237c397`
