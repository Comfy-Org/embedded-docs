> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ViduImageToVideoNode/zh-TW.md)

## 概述

Vidu 影像轉影片生成節點可從起始影像與選用的文字描述建立短影片。此節點使用 AI 模型根據提供的影像畫面生成影片內容，並回傳產生的影片。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | 是 | `viduq1` | 模型名稱（預設值：viduq1） |
| `image` | IMAGE | 是 | - | 作為生成影片起始畫面的影像 |
| `prompt` | STRING | 否 | - | 用於影片生成的文字描述（預設值：空白） |
| `duration` | INT | 否 | 5-5 | 輸出影片的長度（秒）（預設值：5，固定為 5 秒） |
| `seed` | INT | 否 | 0-2147483647 | 影片生成的隨機種子（0 表示隨機）（預設值：0） |
| `resolution` | COMBO | 否 | `1080p` | 支援的解析度可能因模型與長度而異（預設值：1080p） |
| `movement_amplitude` | COMBO | 否 | `auto`<br>`small`<br>`medium`<br>`large` | 畫面中物體的移動幅度（預設值：auto） |

**限制條件：**

- 僅允許輸入單張影像（無法處理多張影像）。
- 輸入影像的長寬比必須介於 1:4 至 4:1 之間。

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `output` | VIDEO | 生成的影片輸出 |

---
**Source fingerprint (SHA-256):** `064b3efba8219770595e68a6607a6f8113d1be7c9f3863a4740ee5c3a146d91e`
