# Tripo紋理節點

Tripo紋理節點使用 Tripo API 生成帶有紋理的 3D 模型。它接收一個模型任務 ID，並透過各種選項（包括 PBR 材質、紋理品質設定和對齊方法）來應用紋理生成。此節點與 Tripo API 通訊以處理紋理生成請求，並返回生成的模型檔案和任務 ID。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `模型任務ID` | 要應用紋理的模型任務 ID | MODEL_TASK_ID | 是 | - |
| `紋理` | 是否生成紋理（預設：True） | BOOLEAN | 否 | - |
| `PBR材質` | 是否生成 PBR（基於物理的渲染）材質（預設：True） | BOOLEAN | 否 | - |
| `紋理種子` | 紋理生成的隨機種子（預設：42） | INT | 否 | - |
| `紋理品質` | 紋理生成的品質等級（預設："standard"）。"detailed" 選項費用為 0.20 美元，"standard" 費用為 0.10 美元。 | COMBO | 否 | "standard"<br>"detailed" |
| `紋理對齊` | 紋理的對齊方法（預設："original_image"）。"original_image" 將紋理對齊到原始輸入影像，而 "geometry" 則將其對齊到 3D 幾何體。 | COMBO | 否 | "original_image"<br>"geometry" |

*注意：此節點需要驗證令牌和 API 金鑰，這些將由系統自動處理。*

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `模型檔案` | 已應用紋理的生成模型檔案（僅為向後相容性保留） | STRING |
| `模型任務 ID` | 用於追蹤紋理生成過程的任務 ID | MODEL_TASK_ID |
| `GLB` | 以 GLB 格式生成的 3D 模型，已應用紋理 | FILE3DGLB |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoTextureNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `6d2a6ff7bbbe9fa91f63c6c7d237799044d2f9aa5afe7b90b99cf9e5a21afc32`
