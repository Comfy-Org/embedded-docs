# Rodin 3D 生成 - 常規生成

Rodin 3D Regular 節點使用 Rodin API 生成 3D 資產。它接收輸入影像，並透過 Rodin 服務進行處理以建立 3D 模型。此節點處理從任務建立到下載最終 3D 模型檔案的完整工作流程。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `圖片` | 用於 3D 模型生成的輸入影像。可提供多張影像。 | IMAGE | 是 | - |
| `種子值` | 用於可重現結果的隨機種子值。 | INT | 是 | - |
| `材質類型` | 應用於 3D 模型的材質類型。 | STRING | 是 | - |
| `多邊形數量` | 生成 3D 模型的目標多邊形數量。此參數決定品質模式和網格複雜度。 | STRING | 是 | - |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `3D 模型路徑` | 生成的 3D 模型檔案路徑（為保持向後相容性而保留）。 | STRING |
| `GLB` | 以 GLB 格式生成的 3D 模型。 | FILE3DGLB |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Rodin3D_Regular/zh-TW.md)

---
**Source fingerprint (SHA-256):** `f937be3aa579baf4407434839e741141d6bd63c09b7e0bdc49a9e92a10d7a130`
