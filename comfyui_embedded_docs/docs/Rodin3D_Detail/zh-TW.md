> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Rodin3D_Detail/zh-TW.md)

## 概述

Rodin 3D Detail 節點使用 Rodin API 生成詳細的 3D 資產。它接收輸入圖像，並透過 Rodin 服務進行處理，以創建具有精細幾何形狀和材質的高品質 3D 模型。此節點處理從任務創建到下載最終 3D 模型檔案的完整工作流程。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `Images` | IMAGE | 是 | - | 用於 3D 模型生成的輸入圖像。可提供多張圖像。 |
| `Seed` | INT | 是 | - | 用於可重現結果的隨機種子值 |
| `Material_Type` | STRING | 是 | - | 應用於 3D 模型的材質類型 |
| `Polygon_count` | STRING | 是 | - | 生成的 3D 模型的目標多邊形數量。決定網格品質等級。 |

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `3D Model Path` | STRING | 生成的 3D 模型檔案路徑（僅用於向後相容） |
| `GLB` | FILE3DGLB | 以 GLB 格式生成的 3D 模型 |

---
**Source fingerprint (SHA-256):** `ed9ed2c8a55ca80d18da88ee2703c66057a09beeac7163fc270d81a492417b0a`
