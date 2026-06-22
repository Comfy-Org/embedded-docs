# 移除背景

## 概述

移除背景節點使用背景移除模型來生成遮罩，將輸入影像中的前景主體與背景分離。此節點接收一張影像和一個背景移除模型，然後產生標示出主要主體的遮罩。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `圖像` | 要移除背景的輸入影像 | IMAGE | 是 | 不適用 |
| `bg_removal_model` | 用於生成遮罩的背景移除模型 | BACKGROUND_REMOVAL_MODEL | 是 | 不適用 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `mask` | 生成的前景遮罩，用於標示輸入影像中的主要主體 | MASK |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RemoveBackground/zh-TW.md)

---
**Source fingerprint (SHA-256):** `cd19134e6afed4d31096b613dd534eacad39afe7de2c8b74feab512bd5f09f66`
