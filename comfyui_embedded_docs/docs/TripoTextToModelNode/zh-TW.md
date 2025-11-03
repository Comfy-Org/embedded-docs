> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoTextToModelNode/zh-TW.md)

使用 Tripo 的 API，根據文字提示同步生成 3D 模型。此節點接收文字描述並創建具有可選紋理和材質屬性的 3D 模型。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | 是 | - | 用於生成 3D 模型的文字描述（多行輸入） |
| `negative_prompt` | STRING | 否 | - | 描述在生成模型中應避免內容的文字（多行輸入） |
| `model_version` | COMBO | 否 | 多個選項可用 | 用於生成的 Tripo 模型版本 |
| `style` | COMBO | 否 | 多個選項可用 | 生成模型的風格設定（預設："None"） |
| `texture` | BOOLEAN | 否 | - | 是否為模型生成紋理（預設：True） |
| `pbr` | BOOLEAN | 否 | - | 是否生成 PBR（基於物理的渲染）材質（預設：True） |
| `image_seed` | INT | 否 | - | 圖像生成的隨機種子（預設：42） |
| `model_seed` | INT | 否 | - | 模型生成的隨機種子（預設：42） |
| `texture_seed` | INT | 否 | - | 紋理生成的隨機種子（預設：42） |
| `texture_quality` | COMBO | 否 | "standard"<br>"detailed" | 紋理生成的品質等級（預設："standard"） |
| `face_limit` | INT | 否 | -1 到 500000 | 生成模型中的最大面數，-1 表示無限制（預設：-1） |
| `quad` | BOOLEAN | 否 | - | 是否生成基於四邊形的幾何體而非三角形（預設：False） |

**注意：** `prompt` 參數為必填項，不能為空。如果未提供提示，節點將引發錯誤。

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `model_file` | STRING | 生成的 3D 模型檔案 |
| `model task_id` | MODEL_TASK_ID | 模型生成過程的唯一任務識別碼 |