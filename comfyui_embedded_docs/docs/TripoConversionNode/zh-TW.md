> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoConversionNode/zh-TW.md)

# TripoConversionNode

TripoConversionNode 使用 Tripo API 在不同檔案格式之間轉換 3D 模型。它接收來自先前 Tripo 操作（模型生成、骨架綁定或重定向）的任務 ID，並將生成的模型轉換為您所需的格式，提供多種匯出選項。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `original_model_task_id` | MODEL_TASK_ID,RIG_TASK_ID,RETARGET_TASK_ID | 是 | MODEL_TASK_ID<br>RIG_TASK_ID<br>RETARGET_TASK_ID | 來自先前 Tripo 操作（模型生成、骨架綁定或重定向）的任務 ID |
| `format` | COMBO | 是 | GLTF<br>USDZ<br>FBX<br>OBJ<br>STL<br>3MF | 轉換後 3D 模型的目標檔案格式 |
| `quad` | BOOLEAN | 否 | True/False | 是否將三角形轉換為四邊形（預設：False） |
| `face_limit` | INT | 否 | -1 至 2000000 | 輸出模型的最大面數，使用 -1 表示無限制（預設：-1） |
| `texture_size` | INT | 否 | 128 至 4096 | 輸出紋理的像素尺寸（預設：4096） |
| `texture_format` | COMBO | 否 | BMP<br>DPX<br>HDR<br>JPEG<br>OPEN_EXR<br>PNG<br>TARGA<br>TIFF<br>WEBP | 匯出紋理的格式（預設：JPEG） |
| `force_symmetry` | BOOLEAN | 否 | True/False | 是否強制模型對稱（預設：False） |
| `flatten_bottom` | BOOLEAN | 否 | True/False | 是否壓平模型底部（預設：False） |
| `flatten_bottom_threshold` | FLOAT | 否 | 0.0 至 1.0 | 底部壓平的閾值（預設：0.0） |
| `pivot_to_center_bottom` | BOOLEAN | 否 | True/False | 是否將樞軸點移動到模型底部中心（預設：False） |
| `scale_factor` | FLOAT | 否 | 0.0 及以上 | 應用於模型的縮放係數（預設：1.0） |
| `with_animation` | BOOLEAN | 否 | True/False | 是否在匯出中包含動畫資料（預設：False） |
| `pack_uv` | BOOLEAN | 否 | True/False | 是否打包 UV 座標（預設：False） |
| `bake` | BOOLEAN | 否 | True/False | 是否烘焙紋理（預設：False） |
| `part_names` | STRING | 否 | 逗號分隔列表 | 要包含在匯出中的零件名稱逗號分隔列表（預設：""） |
| `fbx_preset` | COMBO | 否 | blender<br>mixamo<br>3dsmax | 要使用的 FBX 匯出預設（預設：blender） |
| `export_vertex_colors` | BOOLEAN | 否 | True/False | 是否匯出頂點顏色（預設：False） |
| `export_orientation` | COMBO | 否 | align_image<br>default | 匯出方向模式（預設：default） |
| `animate_in_place` | BOOLEAN | 否 | True/False | 是否在原地對模型進行動畫處理（預設：False） |

**注意：** `original_model_task_id` 必須是來自先前 Tripo 操作（模型生成、骨架綁定或重定向）的有效任務 ID。標記為「進階」的參數為選用，僅在特定匯出需求時才需要配置。

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| *無命名輸出* | - | 此節點非同步處理轉換，並透過 Tripo API 系統返回結果 |

---
**Source fingerprint (SHA-256):** `b11ecab98701b7153a350f5e4980ddc2f446c0a12be3402ca98a5e6de60bd7ce`
