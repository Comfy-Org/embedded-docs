> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ExtendIntermediateSigmas/zh-TW.md)

ExtendIntermediateSigmas 節點接收現有的 sigma 值序列，並在它們之間插入額外的中間 sigma 值。它允許您指定要添加多少額外步驟、用於插值的間距方法，以及可選的起始和結束 sigma 邊界，以控制擴展在 sigma 序列中的發生位置。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `sigmas` | SIGMAS | 是 | - | 要插入中間值進行擴展的輸入 sigma 序列 |
| `步驟數` | INT | 是 | 1-100 | 在現有 sigma 值之間插入的中間步驟數量（預設值：2） |
| `起始 sigma` | FLOAT | 是 | -1.0 至 20000.0 | 擴展的上限 sigma 邊界 - 僅擴展低於此值的 sigma（預設值：-1.0，表示無限大） |
| `結束 sigma` | FLOAT | 是 | 0.0 至 20000.0 | 擴展的下限 sigma 邊界 - 僅擴展高於此值的 sigma（預設值：12.0） |
| `間距` | COMBO | 是 | "linear"<br>"cosine"<br>"sine" | 用於間隔中間 sigma 值的插值方法 |

**注意：** 此節點僅在現有 sigma 對之間插入中間 sigma，且需同時滿足當前 sigma 小於或等於 `start_at_sigma` 且大於或等於 `end_at_sigma`。當 `start_at_sigma` 設為 -1.0 時，它被視為無限大，這意味著僅適用 `end_at_sigma` 下限邊界。

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `sigmas` | SIGMAS | 已插入額外中間值的擴展 sigma 序列 |