> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TencentImageToModelNode/zh-TW.md)

此節點使用騰訊的 Hunyuan3D Pro API，從一張或多張輸入圖片生成 3D 模型。它會處理圖片、將其發送至 API，並傳回生成的 GLB 和 OBJ 格式 3D 模型檔案，以及可選的紋理貼圖。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `模型` | COMBO | 是 | `"3.0"`<br>`"3.1"` | 要使用的 Hunyuan3D 模型版本。`3.1` 模型不提供 LowPoly 選項。 |
| `圖片` | IMAGE | 是 | - | 用於生成 3D 模型的主要輸入圖片。必須至少為 128x128 像素。 |
| `左側圖片` | IMAGE | 否 | - | 物體左側的可選圖片，用於多視角生成。必須至少為 128x128 像素。 |
| `右側圖片` | IMAGE | 否 | - | 物體右側的可選圖片，用於多視角生成。必須至少為 128x128 像素。 |
| `背面圖片` | IMAGE | 否 | - | 物體背面的可選圖片，用於多視角生成。必須至少為 128x128 像素。 |
| `面數` | INT | 是 | 3000 - 1500000 | 生成的 3D 模型目標面數（預設值：500000）。 |
| `生成類型` | DYNAMICCOMBO | 是 | `"Normal"`<br>`"LowPoly"`<br>`"Geometry"` | 要生成的 3D 模型類型。選擇一個選項會顯示額外的相關參數。 |
| `generate_type.pbr` | BOOLEAN | 否 | - | 啟用基於物理的渲染（PBR）材質生成。此參數僅在 `生成類型` 設定為 "Normal" 或 "LowPoly" 時可見（預設值：False）。 |
| `generate_type.polygon_type` | COMBO | 否 | `"triangle"`<br>`"quadrilateral"` | 用於網格的多邊形類型。此參數僅在 `生成類型` 設定為 "LowPoly" 時可見。 |
| `種子` | INT | 是 | 0 - 2147483647 | 生成過程的種子值。種子控制節點是否應重新執行；無論種子為何，結果皆非確定性（預設值：0）。 |

**注意：** 所有輸入圖片的最小寬度和高度必須為 128 像素。如果圖片最長邊超過 4900 像素，則會自動縮小。

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `GLB` | STRING | 為向後相容性保留的舊版輸出。 |
| `OBJ` | FILE3DGLB | 以 GLB（二進位 GL 傳輸格式）檔案格式生成的 3D 模型。 |
| `texture_image` | FILE3DOBJ | 以 OBJ（Wavefront）檔案格式生成的 3D 模型。 |
| `optional_metallic` | IMAGE | 生成的 3D 模型的紋理圖片。 |
| `optional_normal` | IMAGE | PBR 材質的金屬貼圖。若不可用則回傳黑色圖片。 |
| `optional_roughness` | IMAGE | PBR 材質的法線貼圖。若不可用則回傳黑色圖片。 |
| `optional_roughness` | IMAGE | PBR 材質的粗糙度貼圖。若不可用則回傳黑色圖片。 |

---
**Source fingerprint (SHA-256):** `56ac9e55bd9bb3a5c7c46c2de1ea06921cf41c0971471f6d0b64166722705e4d`
