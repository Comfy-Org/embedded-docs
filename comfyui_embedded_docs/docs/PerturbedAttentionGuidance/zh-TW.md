# 擾動注意力引導

## 概述

PerturbedAttentionGuidance 節點會對擴散模型應用擾動注意力引導，以提升生成品質。在取樣過程中，它會將模型的自注意力機制替換為專注於數值投影的簡化版本。此技術透過調整條件去噪過程，有助於改善生成影像的連貫性與品質。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `模型` | 要應用擾動注意力引導的擴散模型 | MODEL | 是 | - |
| `比例` | 擾動注意力引導效果的強度（預設值：3.0）。設為 0 時，節點無作用並回傳原始去噪結果。 | FLOAT | 否 | 0.0 - 100.0 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `模型` | 已套用擾動注意力引導的修改後模型 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PerturbedAttentionGuidance/zh-TW.md)

---
**Source fingerprint (SHA-256):** `8808aa3a3f7cfe306e17f8f4424779cb8e4565647bbcc9d4907da2215affe191`
