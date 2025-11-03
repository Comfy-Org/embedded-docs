> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WebcamCapture/zh-TW.md)

WebcamCapture 節點從網路攝影機裝置擷取影像，並將其轉換為可在 ComfyUI 工作流程中使用的格式。它繼承自 LoadImage 節點，並提供控制擷取尺寸和時機的選項。啟用後，該節點可以在每次處理工作流程佇列時擷取新的影像。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `image` | WEBCAM | 是 | - | 用於擷取影像的網路攝影機輸入來源 |
| `width` | INT | 否 | 0 至 MAX_RESOLUTION | 擷取影像的期望寬度（預設值：0，使用網路攝影機的原生解析度） |
| `height` | INT | 否 | 0 至 MAX_RESOLUTION | 擷取影像的期望高度（預設值：0，使用網路攝影機的原生解析度） |
| `capture_on_queue` | BOOLEAN | 否 | - | 啟用時，每次處理工作流程佇列時都會擷取新影像（預設值：True） |

**注意：** 當 `width` 和 `height` 都設定為 0 時，節點會使用網路攝影機的原生解析度。將任一維度設定為非零值將相應地調整擷取影像的尺寸。

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `IMAGE` | IMAGE | 已轉換為 ComfyUI 影像格式的擷取網路攝影機影像 |