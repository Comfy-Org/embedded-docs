# 儲存影像（進階）

**Save Image (Advanced)** 節點會將輸入影像儲存到你的 ComfyUI 輸出目錄，並可進階控制檔案格式、位元深度與色彩空間。它支援儲存為 PNG、EXR 或 AVIF 檔案（包含動畫 AVIF），且可將工作流程中繼資料嵌入已儲存的檔案中。

## 輸入

### 通用輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `images` | 要儲存的影像。 | IMAGE | 是 | - |
| `filename_prefix` | 要儲存檔案的檔名前綴。可包含格式代碼，例如 `%date:yyyy-MM-dd%` 或 `%Empty Latent Image.width%`。（預設："ComfyUI"） | STRING | 是 | - |
| `format` | 儲存影像所用的檔案格式。選取格式後會顯示該格式的其他選項。 | DYNAMIC_COMBO | 是 | `"png"`<br>`"exr"`<br>`"avif"` |

### PNG 輸入

這些選項會在 `format` 設為 `"png"` 時出現。

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `bit_depth` | 儲存 PNG 檔案的位元深度。（預設："8-bit"） | COMBO | 是（條件式） | `"8-bit"`<br>`"16-bit"` |
| `input_color_space` | 輸入張量的色彩空間。PNG 格式僅提供 sRGB。（預設："sRGB"） | COMBO | 是（條件式） | `"sRGB"` |
| `channels` | 要寫入 PNG 的通道。`"auto"` 會保留輸入通道，grayscale 會將 RGB 轉換為亮度並捨棄 alpha，RGB 會在不含 alpha 的情況下儲存色彩，而 RGBA 會保留 alpha 或加入一個完全不透明的 alpha。（預設：`"auto"`） | COMBO | 否 | `"auto"`<br>`"grayscale (1 channel)"`<br>`"RGB (3 channels)"`<br>`"RGBA (4 channels)"` |

### EXR 輸入

這些選項會在 `format` 設為 `"exr"` 時出現。

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `bit_depth` | 儲存 EXR 檔案的位元深度。（預設："16-bit float"） | COMBO | 是（條件式） | `"16-bit float"`<br>`"32-bit float"` |
| `input_color_space` | 輸入張量的色彩空間。EXR 一律以符合色域的場景線性格式寫入。<br>`"sRGB"` — 輸入為 sRGB 編碼的 Rec.709；會套用反向 sRGB EOTF。<br>`"HDR"` — 輸入為 HLG 編碼的 Rec.2020（BT.2100）；會套用反向 HLG OETF 以取得場景線性光。<br>`"linear"` — 輸入已是場景線性（Rec.709 原色）；會原樣寫入。適用於渲染器／合成器輸出。<br>`"linear ACEScg"` — 輸入已是場景線性 ACEScg（AP1 / D60）；會以 ACEScg 色度座標原樣寫入。（預設："sRGB"） | COMBO | 是（條件式） | `"sRGB"`<br>`"HDR"`<br>`"linear"`<br>`"linear ACEScg"` |

### AVIF 輸入

這些選項會在 `format` 設為 `"avif"` 時出現。

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `bit_depth` | 儲存 AVIF 檔案的位元深度。自動會對 sRGB 使用 8-bit YUV420，對 HDR 使用 10-bit YUV420。（預設："auto"） | COMBO | 是（條件式） | `"auto"`<br>`"8-bit YUV420"`<br>`"10-bit YUV420"` |
| `input_color_space` | 輸入影像的色彩空間。HDR 會選用 BT.2020/HLG，HDR PQ 會選用 BT.2020/PQ。（預設："sRGB"） | COMBO | 是（條件式） | `"sRGB"`<br>`"HDR"`<br>`"HDR PQ"` |
| `crf` | 較低的值會產生更高品質與更大的檔案。（預設：18） | INT | 是（條件式） | 1 至 63 |
| `save_mode` | AVIF 檔案的儲存模式。`"still images"` 會將批次中的每張影像儲存為個別的靜態檔案；`"animated"` 會將整個批次儲存為單一動畫 AVIF 檔案，並顯示 `fps` 與 `loop_count`。（預設："still images"） | DYNAMIC_COMBO | 是（條件式） | `"still images"`<br>`"animated"` |

### AVIF 動畫選項

這些選項會在 `save_mode` 設為 `"animated"` 時出現。

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `fps` | 動畫的影格率。（預設：6.0） | FLOAT | 是（條件式） | 0.01 至 1000.0 |
| `loop_count` | 動畫循環次數。0 表示無限循環。（預設：0） | INT | 是（條件式） | 0 至 1000 |

**參數相依性備註：**
- 格式專屬參數（`bit_depth`、`input_color_space`，以及 AVIF 的 `crf` 與 `save_mode`）僅在選取特定 `format` 時可用。
- 針對 PNG 格式，僅提供 "8-bit" 與 "16-bit" 位元深度，且僅提供 "sRGB" 色彩空間。
- 針對 EXR 格式，提供 "16-bit float" 與 "32-bit float" 兩種位元深度，色彩空間可為 "sRGB"、"HDR"、"linear" 或 "linear ACEScg"。"16-bit float" 為預設，並會產生較小的檔案。
- 針對 AVIF 格式，`fps` 與 `loop_count` 僅在 `save_mode` 設為 `"animated"` 時可用。
- PNG 與 EXR 影像必須具有 1（grayscale）、3（RGB）或 4（RGBA）個通道；不支援其他通道數，且會引發錯誤。
- AVIF 僅支援 1 通道 grayscale 與 3 通道 RGB 影像；不支援 RGBA（alpha）影像，且會引發錯誤。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `images` | 輸入影像，會原樣傳遞。此節點的 UI 輸出會提供已儲存影像結果的清單，每項包含檔案名稱、子資料夾與類型（"output"）。對於包含多張影像的動畫 AVIF，UI 輸出也會包含 `animated` 旗標。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImageAdvanced/zh-TW.md)

---
**Source fingerprint (SHA-256):** `4e8a92c5f1bba35bc4cdf8c858cc9a6fe57cf08436e2dc303d8204c726108216`
