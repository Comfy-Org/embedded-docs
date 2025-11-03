> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/USOStyleReference/zh-TW.md)

此節點使用來自 CLIP 視覺輸出的編碼圖像特徵，將風格參考修補程式應用至模型。它透過整合從視覺輸入中提取的風格資訊，創建輸入模型的修改版本，從而實現風格轉換或基於參考的生成功能。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | 是 | - | 要應用風格參考修補程式的基礎模型 |
| `model_patch` | MODEL_PATCH | 是 | - | 包含風格參考資訊的模型修補程式 |
| `clip_vision_output` | CLIP_VISION_OUTPUT | 是 | - | 從 CLIP 視覺處理中提取的編碼視覺特徵 |

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `model` | MODEL | 已應用風格參考修補程式的修改後模型 |