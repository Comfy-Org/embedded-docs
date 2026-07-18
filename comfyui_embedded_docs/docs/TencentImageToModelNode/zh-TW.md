此節點使用騰訊的 Hunyuan3D Pro API，從一張或多張輸入圖片生成 3D 模型。它會處理圖片、將其發送至 API，並傳回生成的 GLB 和 OBJ 格式 3D 模型檔案，以及可選的紋理貼圖。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `模型` | 要使用的 Hunyuan3D 模型版本。`3.1` 模型不提供 LowPoly 選項。 | COMBO | 是 | `"3.0"`<br>`"3.1"` |
| `圖片` | 用於生成 3D 模型的主要輸入圖片。必須至少為 128x128 像素。 | IMAGE | 是 | - |
| `左側圖片` | 物體左側的可選圖片，用於多視角生成。必須至少為 128x128 像素。 | IMAGE | 否 | - |
| `右側圖片` | 物體右側的可選圖片，用於多視角生成。必須至少為 128x128 像素。 | IMAGE | 否 | - |
| `背面圖片` | 物體背面的可選圖片，用於多視角生成。必須至少為 128x128 像素。 | IMAGE | 否 | - |
| `面數` | 生成的 3D 模型目標面數（預設值：500000）。 | INT | 是 | 3000 - 1500000 |
| `生成類型` | 要生成的 3D 模型類型。選擇一個選項會顯示額外的相關參數。 | DYNAMICCOMBO | 是 | `"Normal"`<br>`"LowPoly"`<br>`"Geometry"` |
| `generate_type.pbr` | 啟用基於物理的渲染（PBR）材質生成。此參數僅在 `生成類型` 設定為 "Normal" 或 "LowPoly" 時可見（預設值：False）。 | BOOLEAN | 否 | - |
| `generate_type.polygon_type` | 用於網格的多邊形類型。此參數僅在 `生成類型` 設定為 "LowPoly" 時可見。 | COMBO | 否 | `"triangle"`<br>`"quadrilateral"` |
| `種子` | 生成過程的種子值。種子控制節點是否應重新執行；無論種子為何，結果皆非確定性（預設值：0）。 | INT | 是 | 0 - 2147483647 |

**注意：** 所有輸入圖片的最小寬度和高度必須為 128 像素。如果圖片最長邊超過 4900 像素，則會自動縮小。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `模型檔案` | 為向後相容性保留的舊版輸出。 | STRING |
| `GLB` | 以 GLB（二進位 GL 傳輸格式）檔案格式生成的 3D 模型。 | FILE3DGLB |
| `OBJ` | 以 OBJ（Wavefront）檔案格式生成的 3D 模型。 | FILE3DOBJ |
| `texture_image` | 生成的 3D 模型的紋理圖片。 | IMAGE |
| `optional_metallic` | PBR 材質的金屬貼圖。若不可用則回傳黑色圖片。 | IMAGE |
| `optional_normal` | PBR 材質的法線貼圖。若不可用則回傳黑色圖片。 | IMAGE |
| `optional_roughness` | PBR 材質的粗糙度貼圖。若不可用則回傳黑色圖片。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TencentImageToModelNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `56ac9e55bd9bb3a5c7c46c2de1ea06921cf41c0971471f6d0b64166722705e4d`
