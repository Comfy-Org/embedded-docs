> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoImageToModelNode/zh-TW.md)

使用 Tripo 的 API 基於單一影像同步生成 3D 模型。此節點接收輸入影像並將其轉換為 3D 模型，提供紋理、品質和模型屬性的各種自訂選項。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | 是 | - | 用於生成 3D 模型的輸入影像 |
| `model_version` | COMBO | 否 | 多個選項可用 | 用於生成的 Tripo 模型版本 |
| `style` | COMBO | 否 | 多個選項可用 | 生成模型的風格設定（預設值："None"） |
| `texture` | BOOLEAN | 否 | - | 是否為模型生成紋理（預設值：True） |
| `pbr` | BOOLEAN | 否 | - | 是否使用基於物理的渲染（預設值：True） |
| `model_seed` | INT | 否 | - | 模型生成的隨機種子（預設值：42） |
| `orientation` | COMBO | 否 | 多個選項可用 | 生成模型的方向設定 |
| `texture_seed` | INT | 否 | - | 紋理生成的隨機種子（預設值：42） |
| `texture_quality` | COMBO | 否 | "standard"<br>"detailed" | 紋理生成的品質等級（預設值："standard"） |
| `texture_alignment` | COMBO | 否 | "original_image"<br>"geometry" | 紋理映射的對齊方法（預設值："original_image"） |
| `face_limit` | INT | 否 | -1 到 500000 | 生成模型中的最大面數，-1 表示無限制（預設值：-1） |
| `quad` | BOOLEAN | 否 | - | 是否使用四邊形面而非三角形面（預設值：False） |

**注意：** `image` 參數為必填項，必須提供才能使節點正常運作。如果未提供影像，節點將引發 RuntimeError。

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `model_file` | STRING | 生成的 3D 模型檔案 |
| `model task_id` | MODEL_TASK_ID | 用於追蹤模型生成過程的任務 ID |