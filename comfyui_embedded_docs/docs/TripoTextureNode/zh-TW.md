# Tripo：模型貼圖（舊版）

此節點在原始碼中標記為已棄用（legacy）；顯示名稱為「Tripo: Texture model (Legacy)」。現有文檔的參數表仍與目前原始碼相符；這些參數表會保留，並在概覽中註明其 legacy 狀態。

Tripo: Texture model (Legacy) 節點會透過 Tripo API 為現有的 Tripo 3D 模型加上紋理。它會接收由其他 Tripo 節點所建立模型的任務 ID，並在紋理工作完成後傳回已加上紋理的 GLB 或 FBX 模型。你可以控制材質貼圖、紋理品質、對齊方式與種子，並使用文字提示、風格影像或參考影像來引導紋理。此節點是紋理工具的 legacy 版本。

## 輸入

### 通用輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `模型任務ID` | 要加上紋理的模型 Tripo 任務 ID。接受模型任務 ID 與分割任務 ID。 | MODEL_TASK_ID, SEGMENT_TASK_ID | 是 | - |
| `紋理` | 已忽略：此節點一律會產生紋理。為較舊的工作流程保留。（預設：True） | BOOLEAN | 否 | true<br>false |
| `PBR材質` | PBR 材質貼圖（基礎顏色、金屬度、粗糙度、法線）；關閉時會產生純色紋理。（預設：True） | BOOLEAN | 否 | true<br>false |
| `紋理種子` | 紋理產生的隨機種子。（預設：42） | INT | 否 | 0 – 2147483647 |
| `紋理品質` | 紋理解析度品質：detailed = HD 紋理，extreme = 8K Ultra 紋理。（預設："standard"）。預估費用：standard $0.10、detailed $0.20、extreme $0.30。 | COMBO | 否 | "standard"<br>"detailed"<br>"extreme" |
| `紋理對齊` | 用於將產生的紋理對齊至模型的方法。（預設："original_image"） | COMBO | 否 | "original_image"<br>"geometry" |
| `texture_prompt` | 選用的紋理文字引導。實務上，對於匯入模型（Tripo: Import Model）為必填，因為這些模型沒有可用來推斷顏色的來源影像。不可與參考影像合併使用。（預設：""） | STRING | 否 | - |
| `model_version` | 紋理模型：v3.0 用於以 v3.x 產生的網格，v2.5 用於以 v2.5 產生的網格。（預設：v3.0_20250812） | COMBO | 否 | 有多個可用選項 |
| `style_image` | 紋理藝術風格的參考影像。僅可與 `texture_prompt` 搭配使用。 | IMAGE | 否 | - |
| `參考` | 引導紋理的參考影像。不可與 `texture_prompt` 或 `style_image` 合併使用。（預設："none"） | DYNAMIC_COMBO | 否 | "none"<br>"image"<br>"multiview" |
| `part_names` | 以逗號分隔的部件名稱，來自 Tripo: Segment Model，用於指定要產生紋理的部件。留空時會為每個部件產生紋理。（預設：""） | STRING | 否 | - |

### `image` 參考輸入

當 `reference` 設為 `"image"` 時，可使用這些輸入。

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `reference_image` | 紋理應遵循的單一參考影像。 | IMAGE | 是 | - |

### `multiview` 參考輸入

當 `reference` 設為 `"multiview"` 時，可使用這些輸入。

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `image_front` | 前視圖（0°）。 | IMAGE | 是 | - |
| `image_left` | 左視圖（90°）。 | IMAGE | 是 | - |
| `image_back` | 後視圖（180°）。 | IMAGE | 是 | - |
| `image_right` | 右視圖（270°）。 | IMAGE | 是 | - |

**注意：** `"image"` 與 `"multiview"` 參考模式不可與非空的 `texture_prompt` 或 `style_image` 合併使用。`style_image` 輸入需要非空的 `texture_prompt`。當 `texture_prompt` 留空時，來源模型必須已有自己的來源影像（例如由 text-to-model、image-to-model、multiview-to-model 或先前的紋理任務所產生的模型）。沒有來源影像的模型——例如匯入、分割、完成或重新拓撲的模型——必須使用 `texture_prompt` 來產生紋理；參考影像僅接受用於 Tripo API 自行產生的模型。`part_names` 輸入可留空，以針對每個部件產生紋理。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `model_file` | 產生的模型檔案（僅為回溯相容性而保留）。 | STRING |
| `model task_id` | 完成的紋理產生任務的任務 ID，可作為其他 Tripo 節點的輸入。 | MODEL_TASK_ID |
| `GLB` | 以 GLB 格式產生的紋理模型。當來源為四邊形網格或 FBX 匯入時為空。 | FILE3DGLB |
| `FBX` | 以 FBX 格式產生的紋理模型。Tripo 會為四邊形網格與 FBX 匯入傳回 FBX；其他情況為空。 | FILE3DFBX |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoTextureNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `850685123b5f14cded5829d86a7307452a1e812e78d11f52806e64ea41d66350`
