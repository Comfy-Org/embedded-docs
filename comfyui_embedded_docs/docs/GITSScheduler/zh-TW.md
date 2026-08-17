# GITSScheduler

GITSScheduler 節點會產生 GITS 取樣方法所使用的 sigma（噪聲等級）排程。它會根據 `coeff` 參數和 `steps` 數量選擇預定義的噪聲等級表，並在 `denoise` 值低於 1.0 時可選擇性地縮短排程。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `coeff` | 用於選擇要用來建立排程之預定義噪聲等級表的係數。此值會四捨五入至小數點後第二位（預設值：1.20） | FLOAT | 是 | 0.80 - 1.50 |
| `steps` | 要為其產生 sigma 的取樣步驟總數（預設值：10） | INT | 是 | 2 - 1000 |
| `denoise` | 降低所使用步驟數量的去噪因子（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |

**注意：** 當 `denoise` 設定為 0.0 時，節點會回傳一個空張量。當 `denoise` 小於 1.0 時，實際使用的步驟數會計算為 `round(steps * denoise)`。當步驟數不超過 20 時，節點會直接使用預定義的噪聲等級；當步驟數大於 20 時，則使用對數線性插值將預定義的噪聲等級擴展到所需的步驟數。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `sigmas` | 為噪聲排程產生的 sigma 值 | SIGMAS |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GITSScheduler/zh-TW.md)

---
**Source fingerprint (SHA-256):** `f46681970fece985f6a4b62d0817d1ea306f1ca9a20189f937512dd5717f458b`
