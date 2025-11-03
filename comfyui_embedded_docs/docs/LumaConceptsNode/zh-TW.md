> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaConceptsNode/zh-TW.md)

儲存一個或多個攝影機概念，供 Luma 文字轉影片和 Luma 圖片轉影片節點使用。此節點允許您選擇最多四個攝影機概念，並可選擇將它們與現有的概念鏈結合。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `concept1` | STRING | 是 | 提供多個選項<br>包含「None」選項 | 從可用的 Luma 概念中選擇第一個攝影機概念 |
| `concept2` | STRING | 是 | 提供多個選項<br>包含「None」選項 | 從可用的 Luma 概念中選擇第二個攝影機概念 |
| `concept3` | STRING | 是 | 提供多個選項<br>包含「None」選項 | 從可用的 Luma 概念中選擇第三個攝影機概念 |
| `concept4` | STRING | 是 | 提供多個選項<br>包含「None」選項 | 從可用的 Luma 概念中選擇第四個攝影機概念 |
| `luma_concepts` | LUMA_CONCEPTS | 否 | 不適用 | 可選的攝影機概念，將與此處選擇的概念合併 |

**注意：** 如果您不想使用全部四個概念插槽，所有概念參數（`concept1` 至 `concept4`）都可以設為「None」。此節點會將任何提供的 `luma_concepts` 與選定的概念合併，以建立一個組合的概念鏈。

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `luma_concepts` | LUMA_CONCEPTS | 包含所有選定概念的組合攝影機概念鏈 |