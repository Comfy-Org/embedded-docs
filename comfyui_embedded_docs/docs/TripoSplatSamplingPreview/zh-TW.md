# TripoSplat 採樣預覽

此節點修補 TripoSplat 模型，使其與標準 KSampler 節點搭配使用時，在每個取樣步驟顯示解碼高斯潑濺的即時預覽。其運作方式是包裝取樣器的回呼函式，在每個步驟後將模型的輸出解碼為預覽圖像。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | 要修補以進行即時預覽的 TripoSplat 模型 | MODEL | 是 | |
| `vae` | TripoSplat VAE 解碼器 | VAE | 是 | |
| `octree_level` | 預覽解碼的八叉樹深度（較低 = 更便宜/更粗糙）。預設值：5 | INT | 否 | 2 至 8 |
| `num_gaussians` | 為預覽產生的高斯數量（四捨五入為 32 的倍數）。預設值：16384 | INT | 否 | 1024 至 262144（步階：32） |
| `yaw` | 預覽相機的偏航角（度）。預設值：90.0 | FLOAT | 否 | -360.0 至 360.0（步階：1.0） |
| `pitch` | 預覽相機的俯仰角（度）。預設值：15.0 | FLOAT | 否 | -89.0 至 89.0（步階：1.0） |
| `point_size` | 最大潑濺半徑（像素）。每個高斯的大小由其尺度決定，並在此處設上限；較低 = 更精細/更尖細，較高 = 更厚實。預設值：3 | INT | 否 | 1 至 16 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `MODEL` | 已修補並加入即時預覽功能的 TripoSplat 模型 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoSplatSamplingPreview/zh-TW.md)

---
**Source fingerprint (SHA-256):** `78678b65df325da964cfd3e8cd0dc07fa25b92d26bb2057117db413a205e9535`
