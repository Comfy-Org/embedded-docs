# LTXV 排程器

LTXVScheduler 節點會為自訂取樣過程產生 sigma 值。它根據輸入 latent 中的 token 數量計算雜訊排程參數，並套用 sigmoid 轉換來建立取樣排程。此節點可以選擇性地拉伸產生的 sigma，以符合指定的終端值。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `步驟數` | 取樣步數（預設值：20） | INT | 是 | 1-10000 |
| `最大偏移` | sigma 計算的最大偏移值（預設值：2.05） | FLOAT | 是 | 0.0-100.0 |
| `基礎偏移` | sigma 計算的基礎偏移值（預設值：0.95） | FLOAT | 是 | 0.0-100.0 |
| `拉伸` | 將 sigmas 拉伸至 [`terminal`, 1] 範圍內（預設值：True） | BOOLEAN | 是 | True/False |
| `終值` | 拉伸後 sigmas 的終端值（預設值：0.1） | FLOAT | 是 | 0.0-0.99 |
| `潛在空間` | 用於計算 token 數量以調整 sigma 的選用 latent 輸入 | LATENT | 否 | - |

**注意：** `latent` 參數為選用。若未提供，節點會使用預設的 token 數量 4096 進行計算。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `sigmas` | 為取樣過程產生的 sigma 值 | SIGMAS |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVScheduler/zh-TW.md)

---
**Source fingerprint (SHA-256):** `5b4907e905e27a951c332c400e24023ef089df7a5f4a17b1fc8ba42a41302399`
