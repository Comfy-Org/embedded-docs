# 儲存影像（進階）

**Save Image (Advanced)** 節點會將輸入影像儲存至你的 ComfyUI 輸出目錄，並可進階控制檔案格式、位元深度與色彩空間。它支援儲存為 PNG、EXR 或 AVIF 檔案（包含動畫 AVIF），且可將工作流程中繼資料嵌入已儲存的檔案中。

## 輸入

### 通用輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `影像` | 要儲存的影像。 | IMAGE | 是 | - |
| `檔名字首` | 要儲存檔案的前綴。可包含格式化符記，例如 `%date:yyyy-MM-dd%` 或 `%Empty Latent Image.width%`。（預設值："ComfyUI"） | STRING | 是 | - |
| `格式` | 要儲存影像的檔案格式。選取某種格式後，會顯示該格式的額外選項。 | DYNAMIC_COMBO | 是 | `"png"`<br>`"exr"`<br>`"avif"` |

### PNG 輸入

當 `format` 設為 `"png"` 時，會顯示這些選項。

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `bit_depth` | 所儲存 PNG 檔案的位元深度。（預設值："8-bit"） | COMBO | 是（條件式） | `"8-bit"`<br>`"16-bit"` |
| `input_color_space` | 輸入張量的色彩空間。PNG 格式僅支援 sRGB。（預設值："sRGB"） | COMBO | 是（條件式） | `"sRGB"` |

### EXR 輸入

當 `format` 設為 `"exr"` 時，會顯示這些選項。

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `bit_depth` | 所儲存 EXR 檔案的位元深度。（預設值："32-bit float"） | COMBO | 是（條件式） | `"32-bit float"` |
| `input_color_space` | 輸入張量的色彩空間。EXR 一律以對應色域的場景線性格式寫入。<br>`"sRGB"` — 輸入為 sRGB 編碼的 Rec.709；會套用反向 sRGB EOTF。<br>`"HDR"` — 輸入為 HLG 編碼的 Rec.2020（BT.2100）；會套用反向 HLG OETF 以取得場景線性光。<br>`"linear"` — 輸入已是場景線性（Rec.709 原色）；會原樣寫入。用於渲染器/合成器輸出。（預設值："sRGB"） | COMBO | 是（條件式） | `"sRGB"`<br>`"HDR"`<br>`"linear"` |

### AVIF 輸入

當 `format` 設為 `"avif"` 時，會顯示這些選項。

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `bit_depth` | 所儲存 AVIF 檔案的位元深度。Auto 會對 sRGB 使用 8-bit YUV420，並對 HDR 使用 10-bit YUV420。（預設值："auto"） | COMBO | 是（條件式） | `"auto"`<br>`"8-bit YUV420"`<br>`"10-bit YUV420"` |
| `input_color_space` | 輸入影像的色彩空間。HDR 會選用 BT.2020/HLG，HDR PQ 則會選用 BT.2020/PQ。（預設值："sRGB"） | COMBO | 是（條件式） | `"sRGB"`<br>`"HDR"`<br>`"HDR PQ"` |
| `crf` | 較低的值會產生更高品質且更大的檔案。（預設值：18） | INT | 是（條件式） | 1 至 63 |
| `save_mode` | AVIF 檔案的儲存模式。`"still images"` 會將批次中的每個影像儲存為個別的靜態檔案；`"animated"` 會將整個批次儲存為單一動畫 AVIF 檔案，並顯示 `fps` 與 `loop_count`。（預設值："still images"） | DYNAMIC_COMBO | 是（條件式） | `"still images"`<br>`"animated"` |

### AVIF 動畫選項

當 `save_mode` 設為 `"animated"` 時，會顯示這些選項。

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `fps` | 動畫的影格率。（預設值：6.0） | FLOAT | 是（條件式） | 0.01 至 1000.0 |
| `loop_count` | 動畫的循環次數。0 表示無限循環。（預設值：0） | INT | 是（條件式） | 0 至 1000 |

**參數相依性備註：**
- 格式專屬參數（`bit_depth`、`input_color_space`，而 AVIF 還包括 `crf` 與 `save_mode`）僅在選取特定 `format` 時可用。
- PNG 格式僅提供 "8-bit" 與 "16-bit" 位元深度，且僅支援 "sRGB" 色彩空間。
- EXR 格式僅提供 "32-bit float" 位元深度，並支援 "sRGB"、"HDR" 或 "linear" 色彩空間。
- AVIF 格式中，`fps` 與 `loop_count` 僅在 `save_mode` 設為 `"animated"` 時可用。
- PNG 與 EXR 影像必須有 1（灰階）、3（RGB）或 4（RGBA）個通道；不支援其他通道數，並會引發錯誤。
- AVIF 僅支援單通道灰階與三通道 RGB 影像；不支援 RGBA（alpha）影像，並會引發錯誤。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `images` | 輸入影像，會原樣傳遞。此節點的 UI 輸出會提供已儲存影像結果的清單，每項包含檔名、子資料夾與類型（"output"）。對於包含多張影像的動畫 AVIF，UI 輸出也會包含 `animated` 旗標。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImageAdvanced/zh-TW.md)

---
**Source fingerprint (SHA-256):** `d3df3caca99d58d973d0bc2ff7c22c4626185d390ec2acf870d4014331c4c335`
