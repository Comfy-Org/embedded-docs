# HiDream-O1 區塊接縫平滑

## 概述

此節點透過在取樣過程的後期，平均 HiDream-O1 模型在多個偏移區塊網格位置上的輸出，來減少該模型所產生影像中的明顯接縫。具體做法是多次執行模型，每次使用略微不同的影像對齊，並將結果混合在一起，這有助於消除區塊邊界可能出現的網格狀偽影。

## 輸入

| 參數 | 描述 | 資料型態 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 要套用接縫平滑包裝器的 HiDream-O1 模型。 | MODEL | 是 | - |
| `start_percent` | 混合功能開啟時的取樣進度（0=開始，1=結束）（預設：0.8）。 | FLOAT | 是 | 0.0 to 1.0 (step: 0.01) |
| `end_percent` | 混合功能關閉時的取樣進度（預設：1.0）。 | FLOAT | 是 | 0.0 to 1.0 (step: 0.01) |
| `pattern` | 偏移布局。`single_shift`：一次通過位於自然區塊網格位置上，其餘通過則偏移。`symmetric`：所有通過皆偏離網格，偏移量以原點為中心對稱分佈（預設：`"single_shift"`）。 | COMBO | 是 | `"single_shift"`<br>`"symmetric"` |
| `passes` | 每個門控步驟的通過次數。`2`/`4` = 固定。`ramp_*`：通過次數會隨著取樣接近結尾而增加（在接縫最明顯處提供更多平滑效果）（預設：`"2"`）。 | COMBO | 是 | `"2"`<br>`"4"`<br>`"ramp_2_4"`<br>`"ramp_2_4_8"` |
| `blend` | `average`：等權重平均。`window`：Hann 窗加權，偏好遠離區塊邊界的每次通過。`median`：逐像素中位數，排除因環繞效應產生的異常通過（預設：`"average"`）。 | COMBO | 是 | `"average"`<br>`"window"`<br>`"median"` |
| `strength` | 自然網格預測（0）與平均結果（1）之間的插值（預設：1.0）。 | FLOAT | 是 | 0.0 to 1.0 (step: 0.01) |

**限制說明：**

- 若 `strength` 為 0.0 或更低，或 `end_percent` 小於等於 `start_percent`，則不會套用平滑效果；在此情況下，節點會直接回傳未修改的模型。
- `passes` 的 ramp 選項（`ramp_2_4`、`ramp_2_4_8`）會在取樣於門控範圍內朝 `end_percent` 推進時增加通過次數，因此只有在 `start_percent` 與 `end_percent` 定義出非空範圍時才有意義。
- 平均結果僅在遠離影像邊緣的地方混合回模型輸出：遮罩會沿每個邊緣保留 32 像素條帶中的原始預測（帶有 4 像素羽化），避免偏移通過所造成的環繞污染。

## 輸出

| 輸出名稱 | 描述 | 資料型態 |
| --- | --- | --- |
| `model` | 已套用區塊接縫平滑包裝器的修改後模型。 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HiDreamO1PatchSeamSmoothing/zh-TW.md)

---
**Source fingerprint (SHA-256):** `02a2256fbf1868cc033a00f15066e9a896a7685ecdca0564ceec5b5b618b6a3c`
