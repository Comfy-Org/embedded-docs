> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAELoader/zh-TW.md)

此節點會偵測位於 `ComfyUI/models/vae` 資料夾中的模型，同時也會從 extra_model_paths.yaml 檔案中設定的其他路徑讀取模型。有時您可能需要**重新整理 ComfyUI 介面**，才能讓它從相應的資料夾讀取模型檔案。

VAELoader 節點專為載入變分自編碼器 (VAE) 模型而設計，特別針對標準和近似 VAE 進行了優化處理。它支援按名稱載入 VAE，包含對 'taesd' 和 'taesdxl' 模型的特殊處理，並會根據 VAE 的具體配置進行動態調整。

## 輸入參數

| 欄位名稱 | Comfy 資料類型 | 描述 |
|---------|----------------|------|
| `vae_name` | `COMBO[STRING]` | 指定要載入的 VAE 名稱，決定要獲取和載入哪個 VAE 模型，支援一系列預定義的 VAE 名稱，包含 'taesd' 和 'taesdxl'。 |

## 輸出參數

| 欄位名稱 | 資料類型 | 描述 |
|---------|----------|------|
| `vae` | `VAE` | 返回已載入的 VAE 模型，準備用於後續操作如編碼或解碼。輸出是一個封裝了已載入模型狀態的模型物件。 |