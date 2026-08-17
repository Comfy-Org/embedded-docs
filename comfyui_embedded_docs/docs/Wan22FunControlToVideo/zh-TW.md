# Wan22FunControlToVideo

Wan22FunControlToVideo 節點使用 Wan 視訊模型架構，準備用於視訊生成的條件化（conditioning）與潛在（latent）表示。它會處理正向與負向條件輸入，以及選用的參考影像和控制視訊，以建立視訊合成所需的潛在空間表示。此節點會處理空間縮放與時間維度，以產生適合視訊模型的條件化資料。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `positive` | 用於引導視訊生成的正向條件輸入 | CONDITIONING | 是 | - |
| `negative` | 用於引導視訊生成的負向條件輸入 | CONDITIONING | 是 | - |
| `vae` | 用於將影像編碼至潛在空間的 VAE 模型 | VAE | 是 | - |
| `width` | 輸出視訊寬度（像素）（預設：832，步長：16） | INT | 是 | 16 to MAX_RESOLUTION |
| `height` | 輸出視訊高度（像素）（預設：480，步長：16） | INT | 是 | 16 to MAX_RESOLUTION |
| `length` | 視訊序列中的影格數（預設：81，步長：4） | INT | 是 | 1 to MAX_RESOLUTION |
| `batch_size` | 要生成的視訊序列數量（預設：1） | INT | 是 | 1 to 4096 |
| `ref_image` | 用於提供視覺引導的選用參考影像 | IMAGE | 否 | - |
| `control_video` | 用於引導生成過程的選用控制視訊 | IMAGE | 否 | - |

**注意：** `length` 參數會以 4 個影格為一個區塊進行處理，且此節點會自動處理潛在空間的時間縮放。當提供 `ref_image` 時，它會透過參考潛在資料影響條件化過程。當提供 `control_video` 時，它會直接影響用於條件化的 concat 潛在表示。`start_image` 參數並未公開為此節點 schema 中的輸入，但在執行邏輯中會被引用。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `positive` | 修改後的正向條件，包含視訊專用的潛在資料，包括 concat 潛在、遮罩及選用的參考潛在 | CONDITIONING |
| `negative` | 修改後的負向條件，包含視訊專用的潛在資料，包括 concat 潛在、遮罩及選用的參考潛在 | CONDITIONING |
| `latent` | 空白的潛在張量，具有根據批次大小、潛在通道數以及空間/時間縮放而定的適當維度，適用於視訊生成 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan22FunControlToVideo/zh-TW.md)

---
**Source fingerprint (SHA-256):** `731b848f15c13ddc662f19230acb55d195f934bad7d9ae516a288e0ed8f8d899`
