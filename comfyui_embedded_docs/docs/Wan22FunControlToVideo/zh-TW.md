# Wan22FunControlToVideo

Wan22FunControlToVideo 節點會為 Wan 影片模型準備條件資料與空的 latent 張量，以進行影片生成。它會將選用的參考影像與控制影片編碼至 latent 空間，並將它們附加到正向與負向條件，同時建立一個填充為零的 latent 張量，其空間與時間維度符合所請求的影片。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `正面提示詞` | 用於引導影片生成的正向條件輸入 | CONDITIONING | 是 | - |
| `負面提示詞` | 用於引導影片生成的負向條件輸入 | CONDITIONING | 是 | - |
| `VAE` | 用於將影像編碼至 latent 空間的 VAE 模型 | VAE | 是 | - |
| `寬度` | 輸出影片的寬度，單位為像素（預設值：832，步長：16） | INT | 是 | 16 to MAX_RESOLUTION |
| `高度` | 輸出影片的高度，單位為像素（預設值：480，步長：16） | INT | 是 | 16 to MAX_RESOLUTION |
| `長度` | 影片序列的幀數（預設值：81，步長：4） | INT | 是 | 1 to MAX_RESOLUTION |
| `批次大小` | 要生成的影片序列數量（預設值：1） | INT | 是 | 1 至 4096 |
| `參考圖像` | 選用的參考影像，為生成提供視覺引導 | IMAGE | 否 | - |
| `控制影片` | 選用的控制影片，用於引導生成過程 | IMAGE | 否 | - |

**注意：** `length` 參數以 4 幀為步長處理，節點在建立 latent 空間時會自動套用時間縮放。提供 `ref_image` 時，只會編碼其第一幀（調整大小為 `width` x `height`），並作為參考 latent 附加至條件。提供 `control_video` 時，會將其修剪為 `length` 幀、調整大小、編碼，並放入條件所使用的 concat latent。串接後的 latent 會沿通道維度複製，其通道配置取決於 VAE 的 latent 通道數（48 通道使用 Wan 2.2 格式，否則使用 Wan 2.1 格式）。`start_image` 參數在執行邏輯中被引用，但未在節點的輸入 schema 中公開，因此無法從節點介面設定。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `positive` | 已加入影片專用 latent 資料的正向條件，包含 concat latent、遮罩及選用的參考 latent | CONDITIONING |
| `negative` | 已加入影片專用 latent 資料的負向條件，包含 concat latent、遮罩及選用的參考 latent | CONDITIONING |
| `latent` | 為影片生成準備的空 latent 張量，大小依批次大小、latent 通道數、長度、高度與寬度而定 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan22FunControlToVideo/zh-TW.md)

---
**Source fingerprint (SHA-256):** `731b848f15c13ddc662f19230acb55d195f934bad7d9ae516a288e0ed8f8d899`
