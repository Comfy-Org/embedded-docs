> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Rodin3D_Gen2/zh-TW.md)

# Rodin3D_Gen2 節點

Rodin3D_Gen2 節點使用 Rodin API 生成 3D 資產。它接收輸入圖像並將其轉換為具有各種材質類型和多邊形數量的 3D 模型。此節點會自動處理整個生成過程，包括任務創建、狀態輪詢和檔案下載。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `圖像` | IMAGE | 是 | - | 用於生成 3D 模型的輸入圖像 |
| `種子值` | INT | 否 | 0-65535 | 生成用的隨機種子值（預設值：0） |
| `材質類型` | COMBO | 否 | "PBR"<br>"Shaded" | 應用於 3D 模型的材質類型（預設值："PBR"） |
| `多邊形數量` | COMBO | 否 | "4K-Quad"<br>"8K-Quad"<br>"18K-Quad"<br>"50K-Quad"<br>"2K-Triangle"<br>"20K-Triangle"<br>"150K-Triangle"<br>"500K-Triangle" | 生成的 3D 模型的目標多邊形數量（預設值："500K-Triangle"） |
| `TAPose` | BOOLEAN | 否 | - | 是否套用 TAPose 處理（預設值：False） |

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `GLB` | STRING | 生成的 3D 模型檔案路徑（用於向後相容） |
| `GLB` | FILE3DGLB | 以 GLB 格式生成的 3D 模型 |

---
**Source fingerprint (SHA-256):** `940712a9a40f4cb07050f3ed7ac502469b30bd364f86bb42b9dd8bf63eb912a2`
