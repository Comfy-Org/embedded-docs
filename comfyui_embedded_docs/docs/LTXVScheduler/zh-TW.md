# LTXV 排程器

LTXVScheduler 節點會為自訂取樣流程產生 sigma 值。它會根據所提供 `latent` 中的 token 數量計算雜訊排程，或在未連接 `latent` 時使用預設的 4096 個 token，並可選擇性地拉伸 sigma 值，使最終值符合指定的 `terminal` 值。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `步驟數` | 取樣步數（預設：20） | INT | 是 | 1-10000 |
| `最大偏移` | sigma 計算中使用的最大偏移值（預設：2.05） | FLOAT | 是 | 0.0-100.0 （步進值：0.01） |
| `基礎偏移` | sigma 計算中使用的基礎偏移值（預設：0.95） | FLOAT | 是 | 0.0-100.0 （步進值：0.01） |
| `拉伸` | 將 sigma 拉伸至範圍 [terminal, 1]（預設：True） | BOOLEAN | 是 | True/False |
| `終值` | 拉伸後 sigma 的終端值（預設：0.1）。僅在啟用 `stretch` 時使用。 | FLOAT | 是 | 0.0-0.99 （步進值：0.01） |
| `潛在空間` | 用於計算 sigma 調整所需 token 數量的可選 latent 輸入。未提供時，會使用預設 token 數量 4096。 | LATENT | 否 | - |

**注意：** 當啟用 `stretch` 時，非零 sigma 值會重新縮放，使最後一個非零 sigma 等於 `terminal` 值。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `sigmas` | 為取樣流程產生的 sigma 值 | SIGMAS |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVScheduler/zh-TW.md)

---
**Source fingerprint (SHA-256):** `5b4907e905e27a951c332c400e24023ef089df7a5f4a17b1fc8ba42a41302399`
