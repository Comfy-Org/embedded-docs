# Vidu2 起始/結束影格轉影片生成

## 概述

此節點透過在提供的起始影格與結束影格之間進行插值，並依據文字提示引導，來生成一段影片。它使用指定的 Vidu 模型，在設定的時長內於兩張圖片之間建立平滑的過渡效果。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 用於影片生成的 Vidu 模型。 | COMBO | 是 | `"viduq2-pro-fast"`<br>`"viduq2-pro"`<br>`"viduq2-turbo"` |
| `first_frame` | 影片序列的起始圖片。僅允許單張圖片。 | IMAGE | 是 | - |
| `end_frame` | 影片序列的結束圖片。僅允許單張圖片。 | IMAGE | 是 | - |
| `prompt` | 引導影片生成的一段文字描述（最多 2000 個字元）。 | STRING | 是 | - |
| `duration` | 生成影片的長度，單位為秒（預設值：5）。 | INT | 否 | 2 至 8 |
| `seed` | 用於初始化隨機生成的數字，以獲得可重現的結果（預設值：1）。 | INT | 否 | 0 至 2147483647 |
| `resolution` | 生成影片的輸出解析度。 | COMBO | 否 | `"720p"`<br>`"1080p"` |
| `movement_amplitude` | 畫面中物體的移動幅度。 | COMBO | 否 | `"auto"`<br>`"small"`<br>`"medium"`<br>`"large"` |

**注意：** `first_frame` 與 `end_frame` 圖片必須具有相似的長寬比。節點會驗證它們的長寬比是否在 0.8 至 1.25 的相對範圍內。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `output` | 生成的影片檔案。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu2StartEndToVideoNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `0a2a125fcb0a519e3aa98ed846f0c7bdc14644a27aaaab3953d55945f787de2a`
