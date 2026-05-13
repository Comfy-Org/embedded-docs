> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIDalle3/zh-TW.md)

## 概述

透過 OpenAI 的 DALL·E 3 端點同步生成圖像。此節點接受文字提示，並使用 OpenAI 的 DALL·E 3 模型建立對應的圖像，讓您可以指定圖像品質、風格和尺寸。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `提示詞` | STRING | 是 | - | 提供給 DALL·E 的文字提示（預設值：""） |
| `種子` | INT | 否 | 0 至 2147483647 | 後端尚未實作此功能（預設值：0） |
| `畫質` | COMBO | 否 | "standard"<br>"hd" | 圖像品質（預設值："standard"） |
| `風格` | COMBO | 否 | "natural"<br>"vivid" | Vivid 會使模型傾向於生成超寫實且戲劇化的圖像。Natural 則使模型產生更自然、較不超寫實的圖像。（預設值："natural"） |
| `尺寸` | COMBO | 否 | "1024x1024"<br>"1024x1792"<br>"1792x1024" | 圖像尺寸（預設值："1024x1024"） |

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `IMAGE` | IMAGE | 從 DALL·E 3 生成的圖像 |

---
**Source fingerprint (SHA-256):** `e36bfe2a6ecec050906f220de3a3edf06eff0bfd6e21f08ce90579172a07d7eb`
