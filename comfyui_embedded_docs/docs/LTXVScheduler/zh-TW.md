> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVScheduler/zh-TW.md)

## 概述

LTXVScheduler 節點用於生成自訂取樣過程的 sigma 值。它根據輸入潛在空間中的 token 數量計算噪聲排程參數，並應用 sigmoid 轉換來建立取樣排程。此節點可以選擇性地拉伸生成的 sigma 值，以匹配指定的終端值。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `步驟數` | INT | 是 | 1-10000 | 取樣步數（預設值：20） |
| `最大偏移` | FLOAT | 是 | 0.0-100.0 | sigma 計算的最大偏移值（預設值：2.05） |
| `基礎偏移` | FLOAT | 是 | 0.0-100.0 | sigma 計算的基礎偏移值（預設值：0.95） |
| `拉伸` | BOOLEAN | 是 | True/False | 拉伸 sigma 值使其落在 [terminal, 1] 範圍內（預設值：True） |
| `終值` | FLOAT | 是 | 0.0-0.99 | 拉伸後 sigma 值的終端值（預設值：0.1） |
| `潛在空間` | LATENT | 否 | - | 可選的潛在空間輸入，用於計算 sigma 調整所需的 token 數量 |

**注意：** `latent` 參數為可選項。若未提供，節點將使用預設的 token 數量 4096 進行計算。

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `sigmas` | SIGMAS | 為取樣過程生成的 sigma 值 |

---
**Source fingerprint (SHA-256):** `3c7e8721fd75bfb0a253c38cd29e2ee1905bfe08193aa97dbaa959550aba34bc`
