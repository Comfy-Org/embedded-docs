## 概述

OpenAIVideoSora2 節點使用 OpenAI 的 Sora 模型生成影片。它根據文字提示和可選的輸入圖片建立影片內容，然後回傳生成的影片輸出。此節點支援不同的影片長度和解析度，具體取決於所選的模型。

**棄用通知：** OpenAI 將於 2026 年 9 月停止提供 Sora v2 API。屆時此節點將從 ComfyUI 中移除。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 用於影片生成的 OpenAI Sora 模型（預設值："sora-2"） | COMBO | 是 | "sora-2"<br>"sora-2-pro" |
| `prompt` | 引導文字；若提供輸入圖片則可為空（預設值：空） | STRING | 是 | - |
| `size` | 生成影片的解析度（預設值："1280x720"） | COMBO | 是 | "720x1280"<br>"1280x720"<br>"1024x1792"<br>"1792x1024" |
| `duration` | 生成影片的長度，單位為秒（預設值：8） | COMBO | 是 | 4<br>8<br>12 |
| `image` | 用於影片生成的可選輸入圖片 | IMAGE | 否 | - |
| `seed` | 決定節點是否應重新執行的種子值；無論種子值為何，實際結果皆為非確定性（預設值：0） | INT | 否 | 0 到 2147483647 |

**限制與約束：**

- "sora-2" 模型僅支援 "720x1280" 和 "1280x720" 解析度
- 使用 `image` 參數時僅支援一張輸入圖片
- 無論種子值為何，結果皆為非確定性

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `output` | 生成的影片輸出 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIVideoSora2/zh-TW.md)

---
**Source fingerprint (SHA-256):** `c87b696dd92c6a6a929f49d189a375b1ebed80bf47f24667ee17c0b210330e55`
