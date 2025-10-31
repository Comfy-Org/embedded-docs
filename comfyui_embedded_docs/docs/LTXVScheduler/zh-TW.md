> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVScheduler/zh-TW.md)

LTXVScheduler 節點為自定義採樣過程生成 sigma 值。它根據輸入潛空間中的 token 數量計算噪聲調度參數，並應用 sigmoid 轉換來創建採樣調度。該節點可以選擇性地拉伸生成的 sigma 值以匹配指定的終端值。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `步驟數` | INT | 是 | 1-10000 | 採樣步數（預設值：20） |
| `最大偏移` | FLOAT | 是 | 0.0-100.0 | 用於 sigma 計算的最大偏移值（預設值：2.05） |
| `基礎偏移` | FLOAT | 是 | 0.0-100.0 | 用於 sigma 計算的基礎偏移值（預設值：0.95） |
| `拉伸` | BOOLEAN | 是 | True/False | 將 sigma 拉伸至 [terminal, 1] 範圍內（預設值：True） |
| `終值` | FLOAT | 是 | 0.0-0.99 | 拉伸後 sigma 的終端值（預設值：0.1） |
| `潛在空間` | LATENT | 否 | - | 可選的潛空間輸入，用於計算 token 數量以進行 sigma 調整 |

**注意：** `latent` 參數是可選的。當未提供時，節點將使用預設的 4096 個 token 數量進行計算。

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `sigmas` | SIGMAS | 為採樣過程生成的 sigma 值 |