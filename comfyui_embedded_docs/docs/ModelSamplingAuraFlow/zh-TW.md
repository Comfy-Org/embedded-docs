# 模型取樣 AuraFlow

ModelSamplingAuraFlow 節點會將專門的取樣設定套用至擴散模型，此設定專為 AuraFlow 模型架構設計。它會透過套用可調整取樣分佈的 `shift` 值，來修改模型的取樣行為。此節點繼承自 SD3 模型取樣框架，並提供對取樣過程的精細控制。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 要套用 AuraFlow 取樣設定的擴散模型 | MODEL | 是 | - |
| `偏移` | 要套用至取樣分佈的 `shift` 值（預設值：1.73，步長：0.01） | FLOAT | 是 | 0.0 - 100.0 |
| `sampling` | 對模型進行修補時所使用的取樣模式（預設值："flow"）。標記為進階選項。 | COMBO | 否 | "flow"<br>"img_to_img_velocity" |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `model` | 已套用 AuraFlow 取樣設定的修改後模型 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingAuraFlow/zh-TW.md)

---
**Source fingerprint (SHA-256):** `5c1381d2dec9ac84a7ee6cd134de444ab50f657eafd960263c63a055d0a139d6`
