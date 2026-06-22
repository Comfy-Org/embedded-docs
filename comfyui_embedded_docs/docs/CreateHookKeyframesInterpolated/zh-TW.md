# 建立 Hook 關鍵影格插值

創建一個鉤子關鍵影格序列，其強度值在起點和終點之間進行插值。此節點會生成多個關鍵影格，使強度參數在生成過程的指定百分比範圍內平滑過渡，並使用多種插值方法來控制過渡曲線。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `strength_start` | 插值序列的起始強度值（預設值：1.0） | FLOAT | 是 | 0.0 - 10.0 |
| `strength_end` | 插值序列的結束強度值（預設值：1.0） | FLOAT | 是 | 0.0 - 10.0 |
| `插值方式` | 用於在強度值之間過渡的插值方法（預設值：LINEAR） | COMBO | 是 | `LINEAR`<br>`EASE_IN`<br>`EASE_OUT`<br>`EASE_IN_OUT`<br>`EASE_OUT_IN`<br>`SINE`<br>`CUBIC`<br>`QUARTIC`<br>`QUINTIC`<br>`EXPO`<br>`CIRC`<br>`BACK`<br>`BOUNCE`<br>`ELASTIC` |
| `起始百分比` | 生成過程中的起始百分比位置（預設值：0.0） | FLOAT | 是 | 0.0 - 1.0 |
| `結束百分比` | 生成過程中的結束百分比位置（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `關鍵影格數量` | 在插值序列中生成的關鍵影格數量（預設值：5） | INT | 是 | 2 - 100 |
| `輸出關鍵影格` | 是否將生成的關鍵影格資訊輸出到日誌（預設值：False） | BOOLEAN | 是 | True/False |
| `前一個 Hook 關鍵影格` | 可選的先前鉤子關鍵影格群組，用於附加 | HOOK_KEYFRAMES | 否 | - |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `HOOK_KF` | 包含插值序列的已生成鉤子關鍵影格群組 | HOOK_KEYFRAMES |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateHookKeyframesInterpolated/zh-TW.md)

---
**Source fingerprint (SHA-256):** `f90c96745ca1f02bbb02e08d2d82be1bbb1f3c80ac5d53a4c6bc07a0e2b8d76f`
