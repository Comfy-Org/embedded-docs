# UNet 時間注意力倍增

## 概述

UNetTemporalAttentionMultiply 節點會對時間性 UNet 模型中的不同注意力機制套用乘法因子。它透過調整自注意力（self-attention）與交叉注意力（cross-attention）層的權重來修改模型，並區分結構性與時間性元件。這使得您可以精細調整每種注意力類型對模型輸出的影響程度。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 要使用注意力乘數進行修改的輸入模型 | MODEL | 是 | - |
| `自我結構` | 自注意力結構性元件的乘數（預設值：1.0） | FLOAT | 否 | 0.0 - 10.0 |
| `自我時間` | 自注意力時間性元件的乘數（預設值：1.0） | FLOAT | 否 | 0.0 - 10.0 |
| `交叉結構` | 交叉注意力結構性元件的乘數（預設值：1.0） | FLOAT | 否 | 0.0 - 10.0 |
| `交叉時間` | 交叉注意力時間性元件的乘數（預設值：1.0） | FLOAT | 否 | 0.0 - 10.0 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `model` | 已調整注意力權重的修改後模型 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/UNetTemporalAttentionMultiply/zh-TW.md)

---
**Source fingerprint (SHA-256):** `98d62fb28a0cdf62154ae4e0b672b3a7bcb9ed61186a164a43992263c1f9439a`
