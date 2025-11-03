> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CheckpointLoaderSimple/zh-TW.md)

這是一個模型載入節點，用於從指定位置載入模型檔案並將其分解為三個核心組件：主模型、文字編碼器和圖像編碼器/解碼器。

此節點會自動偵測 `ComfyUI/models/checkpoints` 資料夾中的所有模型檔案，以及您在 `extra_model_paths.yaml` 檔案中配置的額外路徑。

1. **模型相容性**：確保所選模型與您的工作流程相容。不同模型類型（如 SD1.5、SDXL、Flux 等）需要搭配相應的取樣器和其他節點
2. **檔案管理**：將模型檔案放置在 `ComfyUI/models/checkpoints` 資料夾中，或透過 extra_model_paths.yaml 配置其他路徑
3. **介面重新整理**：如果在 ComfyUI 運行時新增了模型檔案，您需要重新整理瀏覽器（Ctrl+R）才能在下拉清單中看到新檔案

## 輸入參數

| 參數名稱       | 資料類型   | 輸入類型    | 預設值 | 範圍 | 描述 |
|----------------|-----------|------------|---------|-------|-------------|
| `ckpt_name`    | STRING    | 小工具     | null    | checkpoints 資料夾中的所有模型檔案 | 選擇要載入的檢查點模型檔案名稱，這決定了後續圖像生成所使用的 AI 模型 |

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `MODEL`     | MODEL     | 用於圖像去噪生成的主要擴散模型，是 AI 圖像創作的核心組件 |
| `CLIP`      | CLIP      | 用於編碼文字提示的模型，將文字描述轉換為 AI 能夠理解的資訊 |
| `VAE`       | VAE       | 用於圖像編碼和解碼的模型，負責在像素空間和潛在空間之間進行轉換 |