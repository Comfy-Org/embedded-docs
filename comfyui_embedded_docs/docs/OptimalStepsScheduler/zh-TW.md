# 最佳步數排程器

The OptimalStepsScheduler 節點會建立用於擴散取樣期間的雜訊排程（一連串 sigma 值）。它會從所選模型類型中選擇基礎雜訊等級，在僅部分套用去雜訊時調整排程，並對這些等級進行內插，使傳回的 sigmas 符合要求的步數。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model_type` | 用於雜訊等級計算的擴散模型類型。每個選項都使用其自身預先定義的雜訊等級表。 | COMBO | 是 | "FLUX"<br>"Wan"<br>"Chroma" |
| `步驟數` | 要計算的取樣步數總數（預設：20）。 | INT | 是 | 3 到 1000 |
| `去雜訊強度` | 控制去雜訊強度，這會調整有效步數（預設：1.0）。 | FLOAT | 是 | 0.0 到 1.0（步長：0.01） |

**注意：** 所選 `model_type` 的基礎雜訊等級表，只要其長度不等於 `steps + 1`，就會以對數線性內插重新取樣，因此輸出始終符合要求的步數。

**注意：** 當 `denoise` 小於 1.0 時，此節點會使用 `round(steps * denoise)` 作為有效步數總數，並只保留排程中相符的尾端。若 `denoise` 為 0.0 或更低，此節點會傳回空張量。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `sigmas` | 代表擴散取樣雜訊排程的一連串 sigma 值。序列中的最終值一律設為 0。 | SIGMAS |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OptimalStepsScheduler/zh-TW.md)

---
**Source fingerprint (SHA-256):** `fd48c94ca16c8a3d8e6f0138018e7b13c15d100d6147807bcb23d838899045b7`
