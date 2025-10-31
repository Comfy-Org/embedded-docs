> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ControlNetInpaintingAliMamaApply/zh-TW.md)

ControlNetInpaintingAliMamaApply 節點透過結合正負向條件與控制圖像和遮罩，為修補任務應用 ControlNet 條件控制。它處理輸入圖像和遮罩以建立修改後的條件，引導生成過程，從而精確控制圖像中需要修補的區域。該節點支援強度調整和時序控制，可在生成過程的不同階段微調 ControlNet 的影響力。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 參數說明 |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | 是 | - | 引導生成朝向期望內容的正向條件 |
| `negative` | CONDITIONING | 是 | - | 引導生成遠離非期望內容的負向條件 |
| `control_net` | CONTROL_NET | 是 | - | 提供生成過程額外控制的 ControlNet 模型 |
| `vae` | VAE | 是 | - | 用於圖像編碼與解碼的變分自編碼器 |
| `image` | IMAGE | 是 | - | 作為 ControlNet 控制引導的輸入圖像 |
| `mask` | MASK | 是 | - | 定義圖像中哪些區域需要進行修補的遮罩 |
| `strength` | FLOAT | 是 | 0.0 至 10.0 | ControlNet 效果的強度（預設值：1.0） |
| `start_percent` | FLOAT | 是 | 0.0 至 1.0 | ControlNet 影響在生成過程中開始的起始點百分比（預設值：0.0） |
| `end_percent` | FLOAT | 是 | 0.0 至 1.0 | ControlNet 影響在生成過程中結束的終點百分比（預設值：1.0） |

**注意事項：** 當 ControlNet 啟用 `concat_mask` 功能時，遮罩會經過反轉處理並應用至圖像後再進行處理，同時遮罩會包含在傳送給 ControlNet 的額外串接資料中。

## 輸出結果

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | 應用於修補任務並帶有 ControlNet 的修改後正向條件 |
| `negative` | CONDITIONING | 應用於修補任務並帶有 ControlNet 的修改後負向條件 |