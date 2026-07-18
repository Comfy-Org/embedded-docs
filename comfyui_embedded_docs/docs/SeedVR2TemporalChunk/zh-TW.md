# SeedVR2TemporalChunk

此節點將 SeedVR2 影片潛在變量分割成較小的重疊時間區塊，以便在可用 VRAM 內逐一處理。這些區塊設計用於同時傳遞給 Apply SeedVR2 Conditioning 節點和取樣器潛在變量輸入，之後再使用 Merge SeedVR2 Latents 節點重新組合。

## 輸入
| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `latent` | 要分割的 VAE 編碼 SeedVR2 潛在變量 | LATENT | 是 | - |
| `temporal_overlap` | 相鄰區塊之間共享並在合併時交叉淡化的潛在幀數；0 表示無重疊（預設值：0） | INT | 否 | 0 至 16384 |
| `chunking_mode` | manual = 精確使用 frames_per_chunk；auto = 預測適合可用 VRAM 的最大區塊 | COMBO | 是 | "auto"<br>"manual" |

當 `chunking_mode` 設定為 "manual" 時，以下參數將變為可用：

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `frames_per_chunk` | 每個時間區塊的像素幀數（必須為 4n+1：1, 5, 9, 13, ...）（預設值：21） | INT | 是 | 1 至 16384，步長 4 |

**參數約束說明：**
- 輸入 `latent` 必須是形狀為 (B, C, T, H, W) 且恰好有 4 個潛在通道的五維影片潛在變量
- 使用 "manual" 模式時，`frames_per_chunk` 必須為 4n+1 的值（1, 5, 9, 13, 17, 21, ...）
- `temporal_overlap` 會自動限制為小於區塊大小
- 在 "auto" 模式下，節點會根據可用空閒 VRAM 計算最佳區塊大小

## 輸出
| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `latents` | 按順序排列的時間區塊 | LATENT |
| `temporal_overlap` | 相鄰區塊之間的有效潛在幀重疊量，供 Merge SeedVR2 Latents 使用 | INT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedVR2TemporalChunk/zh-TW.md)

---
**Source fingerprint (SHA-256):** `40af2b690f74555efbe38f4cf76825417f52735ce90296a9ad662f78cfe4c6bf`
