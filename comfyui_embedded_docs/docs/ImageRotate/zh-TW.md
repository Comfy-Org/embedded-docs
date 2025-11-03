> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageRotate/zh-TW.md)

ImageRotate 節點可將輸入圖像旋轉指定角度。它支援四種旋轉選項：不旋轉、順時針 90 度、180 度以及順時針 270 度。旋轉操作採用高效的張量運算來執行，能保持圖像資料的完整性。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | 是 | - | 需要進行旋轉的輸入圖像 |
| `rotation` | STRING | 是 | "none"<br>"90 degrees"<br>"180 degrees"<br>"270 degrees" | 要應用於圖像的旋轉角度 |

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `image` | IMAGE | 經過旋轉處理後的輸出圖像 |