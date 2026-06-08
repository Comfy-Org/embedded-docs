# SaveImageAdvanced

**SaveImageAdvanced** 節點可將影像儲存至您的 ComfyUI 輸出目錄，並提供對檔案格式、位元深度和色彩空間的進階控制。它支援儲存為 PNG 或 EXR 檔案，並可將工作流程中繼資料嵌入到儲存的檔案中。

## ## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `影像` | 要儲存的影像。 | IMAGE | 是 | - |
| `檔名字首` | 要儲存檔案的檔名前綴。可包含格式化標記，例如 `%date:yyyy-MM-dd%` 或 `%Empty Latent Image.width%`。（預設值："ComfyUI"） | STRING | 是 | - |
| `格式` | 儲存影像的檔案格式。選擇格式後會顯示該格式的額外選項。 | COMBO | 是 | `"png"`<br>`"exr"` |
| `bit_depth` | 所選格式的位元深度。此參數在選擇格式後出現。（預設值：PNG 為 "8-bit"，EXR 為 "32-bit float"） | COMBO | 是（條件式） | 對於 PNG：`"8-bit"`<br>`"16-bit"`<br>對於 EXR：`"32-bit float"` |
| `input_color_space` | 輸入張量的色彩空間。對於 PNG，僅提供 sRGB。對於 EXR，影像始終以場景線性方式寫入匹配的色域中。（預設值："sRGB"） | COMBO | 是（條件式） | 對於 PNG：`"sRGB"`<br>對於 EXR：`"sRGB"`<br>`"HDR"`<br>`"linear"` |

**參數依賴關係說明：**
- `bit_depth` 和 `input_color_space` 參數僅在選擇了特定 `format` 時才可用。
- 對於 PNG 格式，僅提供 "8-bit" 和 "16-bit" 位元深度，且僅支援 "sRGB" 色彩空間。
- 對於 EXR 格式，僅提供 "32-bit float" 位元深度，並支援 "sRGB"、"HDR" 或 "linear" 色彩空間。
- EXR 的 `input_color_space` 參數決定了輸入張量的解讀方式：
  - `"sRGB"` — 輸入為 sRGB 編碼的 Rec.709；會套用反向 sRGB EOTF。
  - `"HDR"` — 輸入為 HLG 編碼的 Rec.2020 (BT.2100)；會套用反向 HLG OETF 以取得場景線性光。
  - `"linear"` — 輸入已為場景線性（Rec.709 原色）；直接寫入不做變更。適用於渲染器/合成器輸出。

## ## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `影像` | 已儲存影像結果的清單，每個結果包含檔名、子資料夾和類型（"output"）。此輸出用於 UI 顯示目的。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImageAdvanced/zh-TW.md)

---
**Source fingerprint (SHA-256):** `61e52bab8c28437cf648e4790823c15dbe0f758478635b0bd8b5cce785421fe5`
