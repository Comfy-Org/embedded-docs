# Rodin 3D 生成 - 平滑生成

Rodin 3D Smooth 節點透過處理輸入影像並將其轉換為平滑的 3D 模型，使用 Rodin API 來生成 3D 資產。它接收多張影像作為輸入，並產生可下載的 3D 模型檔案。此節點會自動處理整個生成過程，包括任務建立、狀態輪詢和檔案下載。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `圖片` | 用於 3D 模型生成的輸入影像。可提供多張影像。 | IMAGE | 是 | - |
| `種子值` | 用於生成一致性的隨機種子值。 | INT | 是 | - |
| `材質類型` | 應用於 3D 模型的材質類型。 | STRING | 是 | - |
| `多邊形數量` | 生成的 3D 模型的目標多邊形數量。決定網格品質和細節層級。 | STRING | 是 | - |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `3D 模型路徑` | 已下載 3D 模型的檔案路徑（僅為向後相容性保留）。 | STRING |
| `GLB` | 以 GLB 格式生成的 3D 模型。 | FILE3DGLB |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Rodin3D_Smooth/zh-TW.md)

---
**Source fingerprint (SHA-256):** `18783d4a3010234a3640d20c73cdd78e35a0eef7090bd433dba0fcc58e35ad3f`
