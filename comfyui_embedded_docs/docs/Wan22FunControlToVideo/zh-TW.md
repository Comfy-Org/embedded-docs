# Wan22FunControlToVideo

Wan22FunControlToVideo 節點會為 Wan 影片模型準備條件資料和空的潛在張量，以進行影片生成。它會將可選的參考圖片和控制影片編碼至潛在空間，將其附加到正、負條件中，並建立一個填滿零、且具備請求影片所需空間與時間維度的潛在張量。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `正面提示詞` | 用於引導影片生成的正向條件輸入 | CONDITIONING | 是 | - |
| `負面提示詞` | 用於引導影片生成的負向條件輸入 | CONDITIONING | 是 | - |
| `VAE` | 用於將圖片編碼至潛在空間的 VAE 模型 | VAE | 是 | - |
| `寬度` | 輸出影片的寬度（像素）（預設值：832，步進：16） | INT | 是 | 16 至 MAX_RESOLUTION |
| `高度` | 輸出影片的高度（像素）（預設值：480，步進：16） | INT | 是 | 16 至 MAX_RESOLUTION |
| `長度` | 影片序列中的幀數（預設值：81，步進：4） | INT | 是 | 1 至 MAX_RESOLUTION |
| `批次大小` | 要生成的影片序列數量（預設值：1） | INT | 是 | 1 至 4096 |
| `參考圖像` | 可選的參考圖片，可為生成提供視覺引導 | IMAGE | 否 | - |
| `控制影片` | 可選的控制影片，可引導生成過程 | IMAGE | 否 | - |

**注意：** `length` 參數以 4 幀為步進處理，節點在建立潛在空間時會自動套用時間縮放。當提供 `ref_image` 時，只會編碼其第一幀，並作為參考潛在附加至條件中。當提供 `control_video` 時，會將其裁剪至 `length` 幀、進行編碼，然後放入條件所使用的 concat 潛在（concat latent）中。`start_image` 參數會在執行邏輯中被引用，但不會顯示在節點的輸入模式中。

## 輸出

| 輸出名 | 說明 | 資料類型 |
| --- | --- | --- |
| `正面提示詞` | 已添加影片特定潛在數據的正向條件，包括 concat 潛在、遮罩及可選的參考潛在 | CONDITIONING |
| `負面提示詞` | 已添加影片特定潛在數據的負向條件，包括 concat 潛在、遮罩及可選的參考潛在 | CONDITIONING |
| `潛在空間` | 已準備用於影片生成的空潛在張量，會根據批次大小、潛在通道數、長度、高度與寬度調整大小 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan22FunControlToVideo/zh-TW.md)

---
**Source fingerprint (SHA-256):** `731b848f15c13ddc662f19230acb55d195f934bad7d9ae516a288e0ed8f8d899`
