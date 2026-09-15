# TripoTextureNodeV2

此節點會為來自 Tripo 工作流程的現有 3D 模型加入紋理，該模型由先前生成步驟的任務 ID 識別。它可以產生 PBR 材質貼圖或純色紋理，且結果可由文字提示、風格影像或參考影像引導。

## 輸入

### 通用輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model_task_id` | 由先前 Tripo 節點（模型生成或模型分割）產生的來源模型任務 ID。 | MODEL_TASK_ID / SEGMENT_TASK_ID | 是 | - |
| `pbr` | PBR 材質貼圖（基礎色、金屬度、粗糙度、法線）；關閉時會產生純色紋理。（預設：true） | BOOLEAN | 否 | true<br>false |
| `texture_seed` | 用於紋理生成的種子。（預設：42）進階輸入。 | INT | 否 | 0 至 2147483647 |
| `紋理品質` | 生成紋理的品質。`detailed` = HD 紋理，`extreme` = 8K Ultra 紋理。（預設："standard"）進階輸入。 | COMBO | 否 | "standard"<br>"detailed"<br>"extreme" |
| `紋理對齊` | 紋理對齊模型的方式。（預設："original_image"）進階輸入。 | COMBO | 否 | "original_image"<br>"geometry" |
| `紋理提示詞` | 用於紋理生成的選用文字引導。對於匯入的模型（Tripo：Import Model）實務上為必填，因為這些模型沒有可用來推斷顏色的來源影像。不能與參考影像合併使用。（預設：空） | STRING | 否 | - |
| `模型版本` | 紋理模型：v3.0 用於以 v3.x 生成的網格，v2.5 用於以 v2.5 生成的網格。（預設：v3_0_20250812） | COMBO | 否 | Tripo 紋理模型版本，預設 "v3_0_20250812" |
| `風格影像` | 用於紋理藝術風格的參考影像。僅與 `texture_prompt` 一起使用。 | IMAGE | 否 | - |
| `參考影像` | 引導紋理的參考影像。不能與 `texture_prompt` 或 `style_image` 合併使用。（預設："none"） | DYNAMIC_COMBO | 否 | "none"<br>"image"<br>"multiview" |
| `零件名稱` | 來自 Tripo：Segment Model 的逗號分隔部件名稱，用於指定要貼圖的部件。空值會為每個部件貼圖。（預設：空）進階輸入。 | STRING | 否 | - |

### 影像參考輸入

當 `reference` 設為 "image" 時顯示。

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `reference_image` | 紋理應遵循的單一參考影像。 | IMAGE | 是 | - |

### 多視角參考輸入

當 `reference` 設為 "multiview" 時顯示。

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `image_front` | 前視圖（0°）。 | IMAGE | 是 | - |
| `image_left` | 左視圖（90°）。 | IMAGE | 是 | - |
| `image_back` | 後視圖（180°）。 | IMAGE | 是 | - |
| `image_right` | 右視圖（270°）。 | IMAGE | 是 | - |

**參數限制注意事項：**

- 參考影像（參考模式 "image" 或 "multiview"）不能與 `texture_prompt` 或 `style_image` 合併使用。
- `style_image` 需要提供 `texture_prompt`。
- 未提供 `texture_prompt` 時，來源模型必須來自文字轉模型、影像轉模型、多視角轉模型或紋理模型任務。沒有來源影像的模型（匯入、分割、完成或重新拓撲的模型）需要 `texture_prompt`，因為 Tripo 僅接受其自行生成模型的參考影像。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `model task_id` | 紋理操作的任務 ID，可傳遞給其他 Tripo 節點。 | MODEL_TASK_ID |
| `GLB` | GLB 格式的已貼圖模型。當來源是四邊形網格或 FBX 匯入時為空。 | FILE_3D_GLB |
| `FBX` | FBX 格式的已貼圖模型。Tripo 會為四邊形網格與 FBX 匯入回傳 FBX；其他情況為空。 | FILE_3D_FBX |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoTextureNodeV2/zh-TW.md)

---
**Source fingerprint (SHA-256):** `dd9b05e37fcdd29896a50451b92a267862ad94b59abfb8680c8b648390cca091`
