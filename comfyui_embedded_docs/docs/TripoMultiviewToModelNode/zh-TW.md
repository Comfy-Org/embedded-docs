> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoMultiviewToModelNode/zh-TW.md)

此節點使用 Tripo 的 API 同步生成 3D 模型，透過處理最多四張顯示物件不同視角的圖片。它需要一張正面圖片以及至少一張額外的視角圖片（左側、背面或右側），以建立一個包含紋理和材質選項的完整 3D 模型。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | 是 | - | 物件的正面視角圖片（必需） |
| `image_left` | IMAGE | 否 | - | 物件的左側視角圖片 |
| `image_back` | IMAGE | 否 | - | 物件的背面視角圖片 |
| `image_right` | IMAGE | 否 | - | 物件的右側視角圖片 |
| `model_version` | COMBO | 否 | 多個選項可用 | 用於生成的 Tripo 模型版本 |
| `orientation` | COMBO | 否 | 多個選項可用 | 3D 模型的方向設定 |
| `texture` | BOOLEAN | 否 | - | 是否為模型生成紋理（預設值：True） |
| `pbr` | BOOLEAN | 否 | - | 是否生成 PBR（基於物理的渲染）材質（預設值：True） |
| `model_seed` | INT | 否 | - | 模型生成的隨機種子（預設值：42） |
| `texture_seed` | INT | 否 | - | 紋理生成的隨機種子（預設值：42） |
| `texture_quality` | COMBO | 否 | "standard"<br>"detailed" | 紋理生成的品質等級（預設值："standard"） |
| `texture_alignment` | COMBO | 否 | "original_image"<br>"geometry" | 將紋理對齊到模型的方法（預設值："original_image"） |
| `face_limit` | INT | 否 | -1 到 500000 | 生成模型中面的最大數量，-1 表示無限制（預設值：-1） |
| `quad` | BOOLEAN | 否 | - | 是否生成基於四邊形的幾何體而非三角形（預設值：False） |

**注意：** 正面圖片 (`image`) 始終是必需的。必須提供至少一張額外的視角圖片 (`image_left`、`image_back` 或 `image_right`) 以進行多視角處理。

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `model_file` | STRING | 生成的 3D 模型的檔案路徑或識別碼 |
| `model task_id` | MODEL_TASK_ID | 用於追蹤模型生成過程的任務識別碼 |