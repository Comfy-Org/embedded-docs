> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu2StartEndToVideoNode/zh-TW.md)

## 概述

此節點透過在提供的起始影格與結束影格之間進行插值，並依據文字提示引導，來生成一段影片。它使用指定的 Vidu 模型，在設定的時長內於兩張圖片之間建立平滑的過渡效果。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | 是 | `"viduq2-pro-fast"`<br>`"viduq2-pro"`<br>`"viduq2-turbo"` | 用於影片生成的 Vidu 模型。 |
| `first_frame` | IMAGE | 是 | - | 影片序列的起始圖片。僅允許單張圖片。 |
| `end_frame` | IMAGE | 是 | - | 影片序列的結束圖片。僅允許單張圖片。 |
| `prompt` | STRING | 是 | - | 引導影片生成的一段文字描述（最多 2000 個字元）。 |
| `duration` | INT | 否 | 2 至 8 | 生成影片的長度，單位為秒（預設值：5）。 |
| `seed` | INT | 否 | 0 至 2147483647 | 用於初始化隨機生成的數字，以獲得可重現的結果（預設值：1）。 |
| `resolution` | COMBO | 否 | `"720p"`<br>`"1080p"` | 生成影片的輸出解析度。 |
| `movement_amplitude` | COMBO | 否 | `"auto"`<br>`"small"`<br>`"medium"`<br>`"large"` | 畫面中物體的移動幅度。 |

**注意：** `first_frame` 與 `end_frame` 圖片必須具有相似的長寬比。節點會驗證它們的長寬比是否在 0.8 至 1.25 的相對範圍內。

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `output` | VIDEO | 生成的影片檔案。 |

---
**Source fingerprint (SHA-256):** `0a2a125fcb0a519e3aa98ed846f0c7bdc14644a27aaaab3953d55945f787de2a`
