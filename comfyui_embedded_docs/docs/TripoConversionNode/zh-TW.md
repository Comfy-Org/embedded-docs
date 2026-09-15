# Tripo：轉換模型

此節點會將現有的 Tripo 3D 模型轉換為另一種 3D 檔案格式。它會取得先前由 Tripo 操作（例如模型生成、綁定、重新定向或分割）建立或處理過的模型任務 ID，將轉換任務提交至 Tripo API，等待該任務完成，然後傳回轉換後的模型檔案。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `原始模型任務ID` | 要轉換的 Tripo 模型任務 ID。它必須來自先前的 Tripo 模型生成、綁定、重新定向或分割任務。如果 ID 缺少或為空，節點會擲回錯誤。 | STRING | 是 | MODEL_TASK_ID<br>RIG_TASK_ID<br>RETARGET_TASK_ID<br>SEGMENT_TASK_ID |
| `格式` | 轉換後 3D 模型的目標檔案格式。 | COMBO | 是 | GLTF<br>USDZ<br>FBX<br>OBJ<br>STL<br>3MF |
| `四邊形` | 啟用時將三角形轉換為四邊形（預設：False）。 | BOOLEAN | 否 | True or False |
| `面數限制` | 轉換後模型的最大面數。設為 -1 表示無限制（預設：-1）。 | INT | 否 | -1 至 2000000 |
| `紋理尺寸` | 輸出紋理的解析度，單位為像素（預設：4096）。 | INT | 否 | 128 至 8192 |
| `紋理格式` | 匯出紋理所使用的檔案格式（預設：JPEG）。 | COMBO | 否 | BMP<br>DPX<br>HDR<br>JPEG<br>OPEN_EXR<br>PNG<br>TARGA<br>TIFF<br>WEBP |
| `強制對稱` | 啟用時強制模型對稱（預設：False）。 | BOOLEAN | 否 | True or False |
| `底部平整化` | 啟用時壓平模型底部（預設：False）。 | BOOLEAN | 否 | True or False |
| `平整化閾值` | 與 `flatten_bottom` 搭配使用的壓平深度（預設：0.01）。只有啟用 `flatten_bottom` 時才會套用此值。 | FLOAT | 否 | 0.01 至 1.0 |
| `樞軸移至底部中心` | 啟用時將樞軸點移至模型底部的中心（預設：False）。 | BOOLEAN | 否 | True or False |
| `縮放係數` | 套用至轉換後模型的縮放係數（預設：1.0）。 | FLOAT | 否 | 0.01 and above |
| `包含動畫` | 保留已綁定或重新定向模型的骨骼與動畫（預設：True）。 | BOOLEAN | 否 | True or False |
| `打包 UV` | 啟用時重新打包 UV 座標（預設：False）。 | BOOLEAN | 否 | True or False |
| `烘焙` | 將進階材質烘焙至基礎紋理，以獲得更廣泛的相容性（預設：True）。 | BOOLEAN | 否 | True or False |
| `部件名稱` | 要傳送至轉換程序的模型部位名稱清單，以逗號分隔。空白項目會被忽略，重複名稱會被移除。留空即可省略此選項（預設：空）。 | STRING | 否 | Comma-separated list of part names |
| `FBX 預設` | FBX 相容性預設集。bake_scale 會將縮放轉換烘焙至幾何中（預設：blender）。 | COMBO | 否 | blender<br>mixamo<br>3dsmax<br>bake_scale |
| `匯出頂點色` | 啟用時匯出頂點顏色（預設：False）。 | BOOLEAN | 否 | True or False |
| `匯出方向` | 匯出模型的前向軸。default 會保留 Tripo 的 +x（預設：default）。 | COMBO | 否 | default<br>+x<br>-x<br>+y<br>-y |
| `原地動畫` | 啟用時讓模型原地動畫（預設：False）。 | BOOLEAN | 否 | True or False |

**注意：** 除了 `original_model_task_id` 和 `format` 之外，所有輸入都是選用的進階設定。大多數保留預設值的設定都會從轉換要求中省略，以便 Tripo API 使用其標準行為。`with_animation` 和 `bake` 選項一律會傳送。`flatten_bottom_threshold` 只有在啟用 `flatten_bottom` 時才會套用。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `model_3d` | 以要求的格式轉換後的模型。OBJ 由 Tripo 以 ZIP 壓縮檔形式提供（網格、材質和紋理）。 | FILE_3D |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoConversionNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `b6be09bf6b1c5ccd6de5ae56ed28bfe1f0b81c1ca8ff61623e3094917c98d68a`
