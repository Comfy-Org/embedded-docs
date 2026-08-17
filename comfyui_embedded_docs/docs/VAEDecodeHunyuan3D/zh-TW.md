# VAE 解碼 Hunyuan3D

The VAEDecodeHunyuan3D 節點使用 VAE 解碼器將潛在表示轉換為 3D 體素資料。此節點透過可設定的區塊數與解析度設定，將潛在樣本經由 VAE 模型處理，產生適用於 3D 應用的體積資料。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `samples` | 要解碼為 3D 體素資料的潛在表示 | LATENT | 是 | - |
| `vae` | 用於解碼潛在樣本的 VAE 模型 | VAE | 是 | - |
| `num_chunks` | 為記憶體管理而將處理分割成的區塊數量（預設值：8000） | INT | 是 | 1000-500000 |
| `octree_resolution` | 用於 3D 體素生成的八叉樹結構解析度（預設值：256） | INT | 是 | 16-512 |

注意：`num_chunks` 和 `octree_resolution` 為進階參數。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `voxels` | 從解碼後的潛在表示所產生的 3D 體素資料 | VOXEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEDecodeHunyuan3D/zh-TW.md)

---
**Source fingerprint (SHA-256):** `740e328e9e7817aa1a029c5fadddf5457c91bbb5ac12c7e8af2cd81bee6184a7`
