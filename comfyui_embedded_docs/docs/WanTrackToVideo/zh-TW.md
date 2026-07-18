# WanTrackToVideo 節點

WanTrackToVideo 節點透過處理軌跡點並生成對應的視訊幀，將運動追蹤資料轉換為視訊序列。它接收追蹤座標作為輸入，並產生可用於視訊生成的視訊條件化與潛在表示。當未提供任何軌跡時，它會回退為標準的影像轉視訊轉換。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `正向` | 用於視訊生成的正向條件化 | CONDITIONING | 是 | - |
| `負向` | 用於視訊生成的負向條件化 | CONDITIONING | 是 | - |
| `VAE` | 用於編碼與解碼的 VAE 模型 | VAE | 是 | - |
| `追蹤` | JSON 格式的追蹤資料，以多行字串表示（預設值："[]"） | STRING | 是 | - |
| `寬度` | 輸出視訊的寬度（像素）（預設值：832，步進值：16） | INT | 是 | 16 至 MAX_RESOLUTION |
| `高度` | 輸出視訊的高度（像素）（預設值：480，步進值：16） | INT | 是 | 16 至 MAX_RESOLUTION |
| `長度` | 輸出視訊的幀數（預設值：81，步進值：4） | INT | 是 | 1 至 MAX_RESOLUTION |
| `批次大小` | 同時生成的視訊數量（預設值：1） | INT | 是 | 1 至 4096 |
| `溫度` | 運動修補的溫度參數（預設值：220.0，步進值：0.1） | FLOAT | 是 | 1.0 至 1000.0 |
| `TopK` | 運動修補的 top-k 值（預設值：2） | INT | 是 | 1 至 10 |
| `起始影像` | 用於視訊生成的起始影像 | IMAGE | 否 | - |
| `CLIP 視覺輸出` | 用於額外條件化的 CLIP 視覺輸出 | CLIPVISIONOUTPUT | 否 | - |

**注意：** 當 `tracks` 包含有效的追蹤資料時，節點會處理運動軌跡以生成視訊。當 `tracks` 為空時，則切換為標準的影像轉視訊模式。如果提供了 `start_image`，它會初始化視訊序列的第一幀。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `正向` | 已套用運動軌跡資訊的正向條件化 | CONDITIONING |
| `負向` | 已套用運動軌跡資訊的負向條件化 | CONDITIONING |
| `潛在變數` | 生成的視訊潛在表示 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanTrackToVideo/zh-TW.md)

---
**Source fingerprint (SHA-256):** `b3e12492d3dafa100266f6be8fe05e4d62b827f1a2bdb4029f804b107dc691ed`
