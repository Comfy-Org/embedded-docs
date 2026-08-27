# Tripo：紋理模型

TripoTextureNode 使用 Tripo API 生成帶有紋理的 3D 模型。它接收模型任務 ID，並套用各種紋理生成選項，包括 PBR 材質、紋理品質設定和對齊方法。此節點與 Tripo API 通訊以處理紋理生成請求，並傳回生成的模型檔案和任務 ID。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `模型任務ID` | 要套用紋理的模型任務 ID | MODEL_TASK_ID | 是 | - |
| `紋理` | 是否生成紋理（預設：True） | BOOLEAN | 否 | - |
| `PBR材質` | 是否生成 PBR（基於物理的渲染）材質（預設：True） | BOOLEAN | 否 | - |
| `紋理種子` | 紋理生成的隨機種子（預設：42） | INT | 否 | - |
| `紋理品質` | 紋理生成的品質等級（預設："standard"）。"detailed" 選項費用為 0.20 美元，而 "standard" 費用為 0.10 美元。 | COMBO | 否 | "standard"<br>"detailed" |
| `紋理對齊` | 紋理對齊的方法（預設："original_image"）。"original_image" 將紋理對齊到原始輸入圖像，而 "geometry" 則對齊到 3D 幾何體。 | COMBO | 否 | "original_image"<br>"geometry" |
| `texture_prompt` | 紋理化的可選文字引導。實際上對於匯入的模型（Tripo: Import Model）是必需的，因為這些模型沒有可用於推斷顏色的來源圖像。（預設：""） | STRING | 否 | - |

*注意：此節點需要驗證令牌和 API 金鑰，系統會自動處理這些資訊。*

## 輸出

| 輸出名 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `模型檔案` | 已套用紋理的生成的模型檔案（僅供向後相容） | STRING |
| `模型任務 ID` | 用於追蹤紋理生成過程的任務 ID | MODEL_TASK_ID |
| `GLB` | 已套用紋理的 GLB 格式生成的 3D 模型 | FILE3DGLB |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoTextureNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `a0157b7fa2bb94d174ea5893d7389885180876794032a510642586e310ba30d4`
