# 儲存影像（進階）

**SaveImageAdvanced** 節點將影像儲存至您的 ComfyUI 輸出目錄，並可對檔案格式、位元深度與色彩空間進行進階控制。它支援儲存為 PNG 或 EXR 檔案，並可將工作流程中繼資料嵌入所儲存的檔案。

## 輸入

### 通用輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `images` | 要儲存的影像。 | IMAGE | 是 | - |
| `filename_prefix` | 要儲存檔案的前置名稱。可包含格式權杖，例如 `%date:yyyy-MM-dd%` 或 `%Empty Latent Image.width%`。（預設值："ComfyUI"） | STRING | 是 | - |
| `format` | 儲存影像時使用的檔案格式。選取格式後，會顯示該格式的其他選項。 | DYNAMIC_COMBO | 是 | `"png"`<br>`"exr"` |

### PNG 輸入

當 `format` 設定為 `"png"` 時，會顯示這些輸入。

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `bit_depth` | 儲存影像時使用的位元深度。（預設值："8-bit"） | COMBO | 是（條件式） | `"8-bit"`<br>`"16-bit"` |
| `input_color_space` | 輸入張量的色彩空間。（預設值："sRGB"） | COMBO | 是（條件式） | `"sRGB"` |

### EXR 輸入

當 `format` 設定為 `"exr"` 時，會顯示這些輸入。

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `bit_depth` | 儲存影像時使用的位元深度。（預設值："32-bit float"） | COMBO | 是（條件式） | `"32-bit float"` |
| `input_color_space` | 輸入張量的色彩空間。EXR 一律以符合色域中的場景線性（scene-linear）格式寫入。（預設值："sRGB"） | COMBO | 是（條件式） | `"sRGB"`<br>`"HDR"`<br>`"linear"` |

**關於參數依賴關係與檔案行為的注意事項：**

- `bit_depth` 與 `input_color_space` 僅在其所屬 `format` 被選取時才會出現。
- 對於 PNG 格式，僅提供 `"8-bit"` 與 `"16-bit"` 位元深度，且僅有 `"sRGB"` 色彩空間。色彩空間的選取不會修改 PNG 像素——PNG 檔案一律以 sRGB 編碼的影像儲存。
- 對於 EXR 格式，僅提供 `"32-bit float"` 位元深度，並可選擇 `"sRGB"`、`"HDR"` 或 `"linear"` 色彩空間。
- EXR 的 `input_color_space` 參數決定輸入張量在儲存前如何被解讀：
  - `"sRGB"` — 輸入為 sRGB 編碼的 Rec.709；套用反向 sRGB EOTF。
  - `"HDR"` — 輸入為 HLG 編碼的 Rec.2020（BT.2100）；套用反向 HLG OETF 以取得場景線性光。
  - `"linear"` — 輸入已是場景線性（Rec.709 原色）；直接寫入不做變更。適用於渲染器／合成器的輸出。
- 工作流程中繼資料（提示詞與額外 PNG 資訊）會嵌入所儲存的 PNG 與 EXR 檔案，除非使用 `--disable-metadata` 命令列參數停用中繼資料寫入。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `images` | 已儲存的影像（與傳入 `images` 輸入的影像相同）。節點的 UI 結果包含所儲存檔案的清單，每個檔案皆以其檔名、子資料夾與類型（"output"）回報。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImageAdvanced/zh-TW.md)

---
**Source fingerprint (SHA-256):** `b03a822a90cf50d30fbf4397ab280393951f08d2339dd48c0dbaf75d9c415bca`
