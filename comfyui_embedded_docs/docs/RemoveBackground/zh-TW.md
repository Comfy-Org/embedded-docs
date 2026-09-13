# 移除背景

## 概述

Remove Background 節點會產生前景遮罩，將輸入影像中的主要主體與背景分離。它使用背景移除模型分析影像，並產生一個突顯前景元素的遮罩。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `bg_removal_model` | 用於產生遮罩的背景移除模型 | BACKGROUND_REMOVAL_MODEL | 是 | N/A |
| `圖像` | 要移除背景的輸入影像 | IMAGE | 是 | N/A |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `mask` | 產生的前景遮罩 | MASK |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RemoveBackground/zh-TW.md)

---
**Source fingerprint (SHA-256):** `75b415acedaeaa1a694aeba2e4b0367524c6878e3e4a1f48b2a62898c68109f9`
