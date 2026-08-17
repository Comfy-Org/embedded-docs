# LTXV 排程器

LTXVScheduler 節點會為自訂取樣過程產生 sigma 值。它根據輸入 latent 中的 token 數量計算雜訊排程參數，並套用 sigmoid 轉換來建立取樣排程。此節點可選擇性地將產生的 sigma 值拉伸以符合指定的終端值。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `steps` | 取樣步驟數量（預設值：20） | INT | 是 | 1-10000 |
| `max_shift` | sigma 計算的最大位移值（預設值：2.05） | FLOAT | 是 | 0.0-100.0 |
| `base_shift` | sigma 計算的基礎位移值（預設值：0.95） | FLOAT | 是 | 0.0-100.0 |
| `stretch` | 將 sigma 值拉伸至 [terminal, 1] 範圍內（預設值：True） | BOOLEAN | 是 | True/False |
| `terminal` | 拉伸後 sigma 值的終端值（預設值：0.1） | FLOAT | 是 | 0.0-0.99 |
| `latent` | 用於計算 sigma 調整所需 token 數量的選用 latent 輸入 | LATENT | 否 | - |

**注意：** `latent` 參數為選用。若未提供，節點會使用預設的 token 數量 4096 進行計算。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `sigmas` | 為取樣過程產生的 sigma 值 | SIGMAS |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVScheduler/zh-TW.md)

---
**Source fingerprint (SHA-256):** `5b4907e905e27a951c332c400e24023ef089df7a5f4a17b1fc8ba42a41302399`
