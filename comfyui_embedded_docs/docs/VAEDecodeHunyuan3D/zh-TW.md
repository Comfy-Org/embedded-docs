> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEDecodeHunyuan3D/zh-TW.md)

# VAEDecodeHunyuan3D 節點

VAEDecodeHunyuan3D 節點使用 VAE 解碼器將潛在表示轉換為 3D 體素資料。它透過可設定的區塊處理和解析度設定，將潛在樣本經由 VAE 模型處理，以生成適用於 3D 應用的體積資料。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|----------|------|-------|-------------|
| `samples` | LATENT | 是 | - | 要解碼為 3D 體素資料的潛在表示 |
| `vae` | VAE | 是 | - | 用於解碼潛在樣本的 VAE 模型 |
| `num_chunks` | INT | 是 | 1000-500000 | 為記憶體管理而將處理過程分割的區塊數量（預設值：8000） |
| `octree_resolution` | INT | 是 | 16-512 | 用於 3D 體素生成的八叉樹結構解析度（預設值：256） |

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `voxels` | VOXEL | 從解碼後的潛在表示生成的 3D 體素資料 |

---
**Source fingerprint (SHA-256):** `a53ad8e14a2ffca6278866753046d5959f057a4c3fdba5623b37545cee27d557`
