# SamplingPercentToSigma

## 概述

SamplingPercentToSigma 節點使用模型的取樣參數，將取樣百分比值轉換為對應的 sigma 值。它接受介於 0.0 到 1.0 之間的百分比值，並將其映射到模型噪聲調度中的適當 sigma 值，同時提供選項來返回計算出的 sigma 值或邊界處的實際最大/最小 sigma 值。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 包含用於轉換的取樣參數的模型 | MODEL | 是 | - |
| `sampling_percent` | 要轉換為 sigma 的取樣百分比（預設值：0.0） | FLOAT | 是 | 0.0 到 1.0 |
| `return_actual_sigma` | 返回實際 sigma 值，而非用於區間檢查的值。此選項僅影響 0.0 和 1.0 時的結果。（預設值：False） | BOOLEAN | 是 | - |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `sigma 值` | 對應於輸入取樣百分比的轉換後 sigma 值 | FLOAT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplingPercentToSigma/zh-TW.md)

---
**Source fingerprint (SHA-256):** `88ecea0528dfeff75248a8dfee8381e1f73d1a2d9ee3e7f8e37fef0f2b2499ec`
