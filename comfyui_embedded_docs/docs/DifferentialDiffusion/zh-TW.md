# 差分擴散

## 概述

Differential Diffusion 節點透過基於時間步長閾值應用二進位遮罩來修改去噪過程。它建立一個遮罩，在原始去噪遮罩與基於閾值的二進位遮罩之間進行混合，從而允許對擴散過程強度進行受控調整。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `模型` | 要修改的擴散模型 | MODEL | 是 | - |
| `強度` | 控制原始去噪遮罩與二進位閾值遮罩之間的混合強度（預設值：1.0） | FLOAT | 否 | 0.0 - 1.0 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `模型` | 已更新去噪遮罩函數的修改後擴散模型 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DifferentialDiffusion/zh-TW.md)

---
**Source fingerprint (SHA-256):** `3b1727baa6c546516f5dfb53e6e39f27fc7429cde2ac7fd7dfbab99eebb39816`
