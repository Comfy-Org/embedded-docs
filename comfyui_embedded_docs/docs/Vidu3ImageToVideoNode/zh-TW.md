## 概述

Vidu Q3 影像轉影片生成節點可從輸入影像建立影片序列。它使用 Vidu Q3 模型將影像動畫化，可選擇性地透過文字提示引導，並輸出影片檔案。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 用於影片生成的模型。 | COMBO | 是 | `"viduq3-pro"`<br>`"viduq3-turbo"` |
| `model.resolution` | 輸出影片的解析度。可用選項取決於所選模型。 | COMBO | 是 | `"720p"`<br>`"1080p"`<br>`"2K"` (僅限 viduq3-pro) |
| `model.duration` | 輸出影片的長度（秒）（預設值：5）。 | INT | 是 | 1 到 16 |
| `model.audio` | 啟用時，輸出包含聲音（包括對話和音效）的影片（預設值：False）。 | BOOLEAN | 是 | `True` / `False` |
| `image` | 用作生成影片起始幀的影像。 | IMAGE | 是 | - |
| `prompt` | 用於影片生成的可選文字提示（最多 2000 個字元）（預設值：空白）。 | STRING | 否 | - |
| `seed` | 用於控制生成隨機性的種子值（預設值：1）。 | INT | 否 | 0 到 2147483647 |

**注意：** `image` 必須具有介於 1:4 和 4:1（直向到橫向）之間的外觀比例。`prompt` 為可選，但不得超過 2000 個字元。`model.resolution` 選項取決於所選的 `model`：`"viduq3-pro"` 支援 `"720p"`、`"1080p"` 和 `"2K"`；`"viduq3-turbo"` 支援 `"720p"` 和 `"1080p"`。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `output` | 生成的影片檔案。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu3ImageToVideoNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `1dd3929860ee4a04b761014fd2cf7e9e32f9171d8b18fe1e93f27d0905ca04ee`
