# HiDream-O1 區塊接縫平滑

此節點透過在取樣過程後段，對模型輸出在多個位移的 patch-grid 位置進行平均，以減少 HiDream-O1 模型所生成影像中的可見接縫。它會以略有不同的影像對齊方式多次執行模型，並將結果混合在一起，這有助於抵消可能出現在 patch 邊界處的網格狀偽影。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `模型` | 要套用接縫平滑的模型。 | MODEL | 是 | - |
| `起始百分比` | 混合開啟時的取樣進度（0=開始，1=結束）。預設：0.8 | FLOAT | 是 | 0.0 至 1.0 （步進值：0.01） |
| `結束百分比` | 混合關閉時的取樣進度。預設：1.0 | FLOAT | 是 | 0.0 至 1.0 （步進值：0.01） |
| `模式` | 位移配置。`single_shift`：在自然 patch 網格上進行一次傳遞，其餘則位移。`symmetric`：所有傳遞皆偏離網格，位移以原點為中心分開。預設："single_shift" | COMBO | 是 | `"single_shift"`<br>`"symmetric"` |
| `通過次數` | 每個閘控步驟的傳遞次數。`2`/`4` = 固定。`ramp_*`：傳遞次數會隨著取樣接近結束而增加（在接縫最明顯處進行更多平滑）。預設："2" | COMBO | 是 | `"2"`<br>`"4"`<br>`"ramp_2_4"`<br>`"ramp_2_4_8"` |
| `混合方式` | `average`：等權平均。`window`：使用 Hann 窗加權，讓每次傳遞在其 patch 邊界之外獲得較高權重。`median`：逐像素中位數，排除環繞離群值的傳遞。預設："average" | COMBO | 是 | `"average"`<br>`"window"`<br>`"median"` |
| `強度` | 在自然網格預測（0）與平均結果（1）之間進行插值。預設：1.0 | FLOAT | 是 | 0.0 至 1.0 （步進值：0.01） |

**參數限制注意事項：**
- 若 `strength` 為 0.0 或更低，或 `end_percent` 小於或等於 `start_percent`，則不會套用平滑效果。在這些情況下，節點會回傳未變更的模型。
- `passes` 參數的 ramp 選項（`ramp_2_4`、`ramp_2_4_8`）只有在 `end_percent` 大於 `start_percent` 時才有意義，因為傳遞次數會隨著取樣在該範圍內推進而增加。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `model` | 已套用接縫平滑包裝器的修改後模型。 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HiDreamO1PatchSeamSmoothing/zh-TW.md)

---
**Source fingerprint (SHA-256):** `02a2256fbf1868cc033a00f15066e9a896a7685ecdca0564ceec5b5b618b6a3c`
