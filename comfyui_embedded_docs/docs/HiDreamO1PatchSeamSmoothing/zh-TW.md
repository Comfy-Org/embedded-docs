# HiDream-O1 區塊接縫平滑

此節點會在取樣過程的後期，將模型輸出在多個偏移的 patch 網格位置上進行平均，以減少 HiDream-O1 模型生成影像中可見的接縫。其運作方式是多次執行模型，每次使用略微不同的影像對齊方式，再將結果混合，這有助於消除 patch 邊界可能出現的網格狀假影。

## 輸入
| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `模型` | 要套用接縫平滑的 HiDream-O1 模型。 | MODEL | 是 | - |
| `起始百分比` | 取樣進度（0=開始，1=結束），到達此值時平滑效果會開啟（預設：0.8）。 | FLOAT | 是 | 0.0 至 1.0 (step: 0.01) |
| `結束百分比` | 取樣進度，到達此值時平滑效果會關閉（預設：1.0）。 | FLOAT | 是 | 0.0 至 1.0 (step: 0.01) |
| `模式` | 偏移網格位置的佈局。`single_shift`：一次在未偏移的 patch 網格上執行，其餘則偏移。`symmetric`：所有執行皆偏離網格，偏移量以原點為中心對稱分割（預設：`"single_shift"`）。 | COMBO | 是 | `"single_shift"`<br>`"symmetric"` |
| `通過次數` | 每個門控步驟的執行次數（模型執行次數）。`2` 或 `4` 為固定次數。`ramp_2_4` 和 `ramp_2_4_8` 會在取樣接近結束時增加執行次數，在接縫最明顯處提供更多平滑效果（預設：`"2"`）。 | COMBO | 是 | `"2"`<br>`"4"`<br>`"ramp_2_4"`<br>`"ramp_2_4_8"` |
| `混合方式` | 用於合併每次執行結果的方法。`average`：所有執行的等權重平均值。`window`：使用 Hann 窗，對每次執行的中心賦予較高權重，以減少邊界假影。`median`：取每個像素的中位數，可排除因環繞（wraparound）造成的離群執行結果（預設：`"average"`）。 | COMBO | 是 | `"average"`<br>`"window"`<br>`"median"` |
| `強度` | 控制原始模型輸出（0.0）與完全平滑結果（1.0）之間的插值（預設：1.0）。 | FLOAT | 是 | 0.0 至 1.0 (step: 0.01) |

**參數限制注意事項：**

- 若 `strength` 為 0.0 或更低，或 `end_percent` 小於或等於 `start_percent`，則不會套用平滑效果。在這些情況下，節點會原封不動地回傳模型。
- `passes` 參數的漸增選項（`ramp_2_4`、`ramp_2_4_8`）只有在 `start_percent` 和 `end_percent` 定義一個範圍時才有意義，因為取樣在該範圍內推進時，執行次數會增加。

## 輸出
| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `model` | 已套用接縫平滑包裝器的修改後模型。 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HiDreamO1PatchSeamSmoothing/zh-TW.md)

---
**Source fingerprint (SHA-256):** `02a2256fbf1868cc033a00f15066e9a896a7685ecdca0564ceec5b5b618b6a3c`
