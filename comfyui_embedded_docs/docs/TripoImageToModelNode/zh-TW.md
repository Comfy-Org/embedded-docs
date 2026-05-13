> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoImageToModelNode/zh-TW.md)

# Tripo 影像轉模型節點

根據單一影像，使用 Tripo 的 API 同步生成 3D 模型。此節點接收輸入影像，並將其轉換為 3D 模型，提供多種紋理、品質和模型屬性的自訂選項。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | 是 | - | 用於生成 3D 模型的輸入影像 |
| `model_version` | COMBO | 否 | 多個可用選項 | 用於生成的 Tripo 模型版本 |
| `style` | COMBO | 否 | 多個可用選項 | 生成模型的樣式設定（預設："None"） |
| `texture` | BOOLEAN | 否 | - | 是否為模型生成紋理（預設：True） |
| `pbr` | BOOLEAN | 否 | - | 是否使用基於物理的渲染（預設：True） |
| `model_seed` | INT | 否 | - | 模型生成的隨機種子（預設：42） |
| `orientation` | COMBO | 否 | 多個可用選項 | 生成模型的方位設定 |
| `texture_seed` | INT | 否 | - | 紋理生成的隨機種子（預設：42） |
| `texture_quality` | COMBO | 否 | "standard"<br>"detailed" | 紋理生成的品質等級（預設："standard"） |
| `texture_alignment` | COMBO | 否 | "original_image"<br>"geometry" | 紋理映射的對齊方式（預設："original_image"） |
| `face_limit` | INT | 否 | -1 至 500000 | 生成模型的最大面數，-1 表示無限制（預設：-1） |
| `quad` | BOOLEAN | 否 | - | 是否使用四邊形面而非三角形（預設：False） |
| `geometry_quality` | COMBO | 否 | "standard"<br>"detailed" | 幾何生成的品質等級（預設："standard"） |

**注意：** `image` 參數為必要參數，必須提供才能使節點正常運作。如果未提供影像，節點將引發 RuntimeError。

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `model_file` | STRING | 生成的 3D 模型檔案（僅為向後相容性保留） |
| `model task_id` | MODEL_TASK_ID | 用於追蹤模型生成過程的任務 ID |
| `GLB` | FILE3DGLB | 以 GLB 格式生成的 3D 模型 |

---
**Source fingerprint (SHA-256):** `1342de2f9788fac504fa0cfa248d011c04a8874307bb26dac86a7ced43a2809e`
