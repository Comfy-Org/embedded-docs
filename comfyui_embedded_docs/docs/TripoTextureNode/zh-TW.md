# Tripo：紋理模型

TripoTextureNode 節點使用 Tripo API 生成帶有紋理的 3D 模型。它接收一個模型任務 ID，並套用各種紋理生成選項，包括 PBR 材質、紋理品質設定、對齊方法，以及可選的文字引導。此節點與 Tripo API 通訊以處理紋理生成請求，並回傳生成的模型檔案與任務 ID。

## 輸入

| 參數 | 描述 | 資料型別 | 必填 | 範圍 |
|------|------|---------|------|------|
| `model_task_id` | 要套用紋理的模型任務 ID | MODEL_TASK_ID | 是 | - |
| `texture` | 是否生成紋理（預設值：True） | BOOLEAN | 否 | - |
| `pbr` | 是否生成 PBR（基於物理的渲染）材質（預設值：True） | BOOLEAN | 否 | - |
| `texture_seed` | 紋理生成的隨機種子（預設值：42） | INT | 否 | - |
| `texture_quality` | 紋理生成的品質等級（預設值："standard"）。「detailed」選項費用為 0.20 美元，而「standard」費用為 0.10 美元。 | COMBO | 否 | "standard"<br>"detailed" |
| `texture_alignment` | 紋理對齊的方法（預設值："original_image"）。「original_image」會將紋理對齊至原始輸入影像，而「geometry」則對齊至 3D 幾何形狀。 | COMBO | 否 | "original_image"<br>"geometry" |
| `texture_prompt` | 紋理化的選用文字引導。對於匯入的模型（Tripo: Import Model），實際上需要此項，因為這些模型沒有可用於推斷顏色的來源影像。（多行文字方塊，預設值：空字串） | STRING | 否 | - |

*注意：此節點需要驗證令牌和 API 金鑰，系統會自動處理。*

## 輸出

| 輸出名 | 描述 | 資料型別 |
|--------|------|---------|
| `model_file` | 生成的已套用紋理之模型檔案（僅供向後相容） | STRING |
| `model task_id` | 用於追蹤紋理生成程序的任務 ID | MODEL_TASK_ID |
| `GLB` | 生成的 GLB 格式 3D 模型，已套用紋理 | FILE3DGLB |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoTextureNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `a0157b7fa2bb94d174ea5893d7389885180876794032a510642586e310ba30d4`
