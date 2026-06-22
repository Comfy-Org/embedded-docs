# GITSScheduler

GITSScheduler 節點為 GITS（生成式迭代時間步長）取樣方法生成噪聲排程的 sigma 值。它根據係數參數和步數計算 sigma 值，並可選用降噪因子來減少使用的總步數。該節點使用預定義的噪聲級別和插值來創建最終的 sigma 排程。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `coeff` | 控制噪聲排程曲線的係數值（預設值：1.20） | FLOAT | 是 | 0.80 - 1.50 |
| `步驟數` | 要生成 sigma 值的總取樣步數（預設值：10） | INT | 是 | 2 - 1000 |
| `去雜訊強度` | 用於減少使用步數的降噪因子（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |

**注意：** 當 `denoise` 設定為 0.0 時，節點會返回一個空張量。當 `denoise` 小於 1.0 時，實際使用的步數計算為 `round(steps * denoise)`。對於大於 20 的步數，節點使用對數線性插值將預定義的噪聲級別擴展到所需的步數。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `sigmas` | 為噪聲排程生成的 sigma 值 | SIGMAS |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GITSScheduler/zh-TW.md)

---
**Source fingerprint (SHA-256):** `b81b85f95236276822429ec7cbc90204c6f4f86ea3e89ed8b7c2aea40597fea9`
