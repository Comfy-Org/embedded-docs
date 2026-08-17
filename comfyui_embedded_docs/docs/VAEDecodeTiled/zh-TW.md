# VAE 解碼（分割區塊）

The VAEDecodeTiled 節點使用分塊（tile）方法將潛在表示解碼為影像，以有效處理大型影像。它會將輸入切成較小的區塊進行處理，以管理記憶體使用量，同時維持影像品質。此節點也支援影片 VAE，透過以重疊方式分批處理時間幀，實現平滑過渡。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `samples` | 要解碼為影像的潛在表示 | LATENT | 是 | - |
| `vae` | 用於解碼潛在樣本的 VAE 模型 | VAE | 是 | - |
| `tile_size` | 處理時每個區塊的大小（預設：512） | INT | 是 | 64-4096 (step: 32) |
| `overlap` | 相鄰區塊之間的重疊量（預設：64） | INT | 是 | 0-4096 (step: 32) |
| `temporal_size` | 僅用於影片 VAE：每次解碼的幀數（預設：64） | INT | 是 | 8-4096 (step: 4) |
| `temporal_overlap` | 僅用於影片 VAE：重疊的幀數（預設：8） | INT | 是 | 4-4096 (step: 4) |

**注意：** 此節點會在重疊值超出實際限制時自動調整。如果 `tile_size` 小於 `overlap` 的 4 倍，則重疊會減少為區塊大小的四分之一。同樣地，如果 `temporal_size` 小於 `temporal_overlap` 的 2 倍，時間重疊會減半。此節點在計算空間與時間維度的區塊及重疊大小時，也會考量 VAE 的內部壓縮比率。對於沒有時間壓縮的 VAE（非影片 VAE），`temporal_size` 和 `temporal_overlap` 參數會被忽略。

## 輸出

| 輸出名 | 描述 | 資料類型 |
| --- | --- | --- |
| `IMAGE` | 從潛在表示解碼而出的影像或影像群組。解碼影片潛在時，所有解碼後的幀會組合成單一影像列表。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEDecodeTiled/zh-TW.md)

---
**Source fingerprint (SHA-256):** `04136ba1abd0c74e780dc405f916a08b809630ae4f41c183049535488b40fd96`
