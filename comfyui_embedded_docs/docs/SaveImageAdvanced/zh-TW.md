# 儲存影像（進階）

**Save Image (Advanced)** 節點會將輸入的影像儲存到您的 ComfyUI 輸出目錄，並提供對檔案格式、位元深度與色彩空間的進階控制。它支援儲存為 PNG 或 EXR 檔案，並可將工作流程中繼資料嵌入到儲存的檔案中。

## 輸入

### 通用輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `影像` | 要儲存的影像。 | IMAGE | 是 | - |
| `檔名字首` | 儲存檔案的前置詞。可包含格式化 token，例如 `%date:yyyy-MM-dd%` 或 `%Empty Latent Image.width%`。（預設值："ComfyUI"） | STRING | 是 | - |
| `格式` | 儲存影像的檔案格式。選擇格式會顯示該格式的額外選項。 | DYNAMIC_COMBO | 是 | `"png"`<br>`"exr"` |

### PNG 輸入

當 `format` 設定為 `"png"` 時，會顯示這些選項。

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `bit_depth` | 儲存 PNG 檔案的位元深度。（預設值："8-bit"） | COMBO | 是（條件性） | `"8-bit"`<br>`"16-bit"` |
| `input_color_space` | 輸入張量的色彩空間。PNG 格式僅提供 sRGB。（預設值："sRGB"） | COMBO | 是（條件性） | `"sRGB"` |

### EXR 輸入

當 `format` 設定為 `"exr"` 時，會顯示這些選項。

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `bit_depth` | 儲存 EXR 檔案的位元深度。（預設值："32-bit float"） | COMBO | 是（條件性） | `"32-bit float"` |
| `input_color_space` | 輸入張量的色彩空間。EXR 一律以相符色域中的場景線性（scene-linear）寫入。<br>`"sRGB"` — 輸入為 sRGB 編碼的 Rec.709；套用反向 sRGB EOTF。<br>`"HDR"` — 輸入為 HLG 編碼的 Rec.2020（BT.2100）；套用反向 HLG OETF 以取得場景線性光。<br>`"linear"` — 輸入已是場景線性（Rec.709 原色）；直接寫入而不變更。請針對算圖器／合成器輸出使用此選項。（預設值："sRGB"） | COMBO | 是（條件性） | `"sRGB"`<br>`"HDR"`<br>`"linear"` |

**參數依賴注意事項：**
- `bit_depth` 與 `input_color_space` 參數只有在選取特定 `format` 時才可用。
- 對於 PNG 格式，僅提供 "8-bit" 與 "16-bit" 位元深度，且僅提供 "sRGB" 色彩空間。
- 對於 EXR 格式，僅提供 "32-bit float" 位元深度，色彩空間則有 "sRGB"、"HDR" 或 "linear"。
- 影像必須具有 1（灰階）、3（RGB）或 4（RGBA）個通道；其他通道數不受支援，並會引發錯誤。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `images` | 輸入的影像，原封不動地傳遞。節點的 UI 輸出會提供已儲存影像結果的清單，每個結果包含檔案名稱、子資料夾與類型（"output"）。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImageAdvanced/zh-TW.md)

---
**Source fingerprint (SHA-256):** `b03a822a90cf50d30fbf4397ab280393951f08d2339dd48c0dbaf75d9c415bca`
