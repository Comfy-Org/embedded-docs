> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SD_4XUpscale_Conditioning/zh-TW.md)

SD_4XUpscale_Conditioning 節點用於為使用擴散模型的圖像放大過程準備條件數據。它接收輸入圖像和條件數據，然後應用縮放和噪聲增強來創建經過修改的條件數據，以指導放大過程。該節點輸出正向和負向條件數據，以及放大尺寸的潛在表示。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 參數說明 |
|-----------|-----------|----------|-------|-------------|
| `images` | IMAGE | 是 | - | 需要進行放大的輸入圖像 |
| `positive` | CONDITIONING | 是 | - | 正向條件數據，用於引導生成過程朝向期望的內容 |
| `negative` | CONDITIONING | 是 | - | 負向條件數據，用於使生成過程遠離不需要的內容 |
| `scale_ratio` | FLOAT | 否 | 0.0 - 10.0 | 應用於輸入圖像的縮放比例係數（預設值：4.0） |
| `noise_augmentation` | FLOAT | 否 | 0.0 - 1.0 | 在放大過程中添加的噪聲量（預設值：0.0） |

## 輸出結果

| 輸出名稱 | 資料類型 | 輸出說明 |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | 應用放大資訊後的修改正向條件數據 |
| `negative` | CONDITIONING | 應用放大資訊後的修改負向條件數據 |
| `latent` | LATENT | 符合放大尺寸的空潛在表示 |