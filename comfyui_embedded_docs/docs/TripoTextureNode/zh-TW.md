> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoTextureNode/zh-TW.md)

TripoTextureNode 使用 Tripo API 生成帶有紋理的 3D 模型。它接收一個模型任務 ID，並應用包含 PBR 材質、紋理品質設定和對齊方法在內的各種選項來進行紋理生成。該節點與 Tripo API 通訊以處理紋理生成請求，並返回生成的模型檔案和任務 ID。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `model_task_id` | MODEL_TASK_ID | 是 | - | 要應用紋理的模型任務 ID |
| `texture` | BOOLEAN | 否 | - | 是否生成紋理（預設值：True） |
| `pbr` | BOOLEAN | 否 | - | 是否生成 PBR（基於物理的渲染）材質（預設值：True） |
| `texture_seed` | INT | 否 | - | 用於紋理生成的隨機種子（預設值：42） |
| `texture_quality` | COMBO | 否 | "standard"<br>"detailed" | 紋理生成的品質等級（預設值："standard"） |
| `texture_alignment` | COMBO | 否 | "original_image"<br>"geometry" | 紋理對齊的方法（預設值："original_image"） |

*注意：此節點需要驗證令牌和 API 金鑰，這些已由系統自動處理。*

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `model_file` | STRING | 已應用紋理的生成模型檔案 |
| `model task_id` | MODEL_TASK_ID | 用於追蹤紋理生成過程的任務 ID |