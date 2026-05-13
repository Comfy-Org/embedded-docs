> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoMultiviewToModelNode/zh-TW.md)

# Tripo 多視圖轉模型節點

此節點透過 Tripo 的 API 同步生成 3D 模型，可處理最多四張顯示物體不同視角的影像。需要一張正面影像以及至少一個額外視角（左側、背面或右側）的影像，以建立具有紋理和材質選項的完整 3D 模型。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | 是 | - | 物體的正面視角影像（必要） |
| `image_left` | IMAGE | 否 | - | 物體的左側視角影像 |
| `image_back` | IMAGE | 否 | - | 物體的背面視角影像 |
| `image_right` | IMAGE | 否 | - | 物體的右側視角影像 |
| `model_version` | COMBO | 否 | 多個選項可用 | 用於生成的模型版本 |
| `orientation` | COMBO | 否 | 多個選項可用 | 3D 模型的方向設定（預設值："default"） |
| `texture` | BOOLEAN | 否 | - | 是否為模型生成紋理（預設值：True） |
| `pbr` | BOOLEAN | 否 | - | 是否生成 PBR（基於物理的渲染）材質（預設值：True） |
| `model_seed` | INT | 否 | - | 模型生成的隨機種子（預設值：42） |
| `texture_seed` | INT | 否 | - | 紋理生成的隨機種子（預設值：42） |
| `texture_quality` | COMBO | 否 | `"standard"`<br>`"detailed"` | 紋理生成的品質等級（預設值："standard"） |
| `texture_alignment` | COMBO | 否 | `"original_image"`<br>`"geometry"` | 紋理對齊模型的方法（預設值："original_image"） |
| `face_limit` | INT | 否 | -1 至 500000 | 生成模型中的最大面數。設為 -1 表示無限制（預設值：-1） |
| `quad` | BOOLEAN | 否 | - | 此參數已棄用，無實際作用（預設值：False） |
| `geometry_quality` | COMBO | 否 | `"standard"`<br>`"detailed"` | 幾何生成的品質等級（預設值："standard"） |

**注意：** 正面影像（`image`）始終為必要項目。必須提供至少一個額外視角的影像（`image_left`、`image_back` 或 `image_right`）才能進行多視圖處理。

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `model_file` | STRING | 生成的 3D 模型檔案路徑或識別碼（僅為向後相容性保留） |
| `model task_id` | MODEL_TASK_ID | 用於追蹤模型生成過程的任務識別碼 |
| `GLB` | FILE3DGLB | 以 GLB 格式生成的 3D 模型檔案 |

---
**Source fingerprint (SHA-256):** `4ad433f4a0060d0ac2ce14463497db3168a1bf3348f17b98e958409e9a63baaf`
