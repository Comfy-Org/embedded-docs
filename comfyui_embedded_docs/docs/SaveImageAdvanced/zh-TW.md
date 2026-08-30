# 儲存影像（進階）

**Save Image (Advanced)** 節點會將輸入圖像儲存到您的 ComfyUI 輸出目錄，並提供對檔案格式、位元深度及色彩空間的進階控制。它支援儲存為 PNG、EXR 或 AVIF 檔案（包括動畫 AVIF），並可將工作流程中繼資料嵌入所儲存的檔案中。

## 輸入

### 通用輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `影像` | 要儲存的圖像。 | IMAGE | 是 | - |
| `檔名字首` | 要儲存檔案的前置詞。可包含格式化 token，例如 `%date:yyyy-MM-dd%` 或 `%Empty Latent Image.width%`。（預設值："ComfyUI"） | STRING | 是 | - |
| `格式` | 儲存圖像時使用的檔案格式。選擇格式會顯示該格式的其他選項。 | DYNAMIC_COMBO | 是 | `"png"`<br>`"exr"`<br>`"avif"` |

### PNG 輸入

當 `format` 設定為 `"png"` 時，會顯示這些選項。

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `bit_depth` | 所儲存 PNG 檔案的位元深度。（預設值："8-bit"） | COMBO | 是（條件性） | `"8-bit"`<br>`"16-bit"` |
| `input_color_space` | 輸入張量的色彩空間。PNG 格式僅提供 sRGB。（預設值："sRGB"） | COMBO | 是（條件性） | `"sRGB"` |

### EXR 輸入

當 `format` 設定為 `"exr"` 時，會顯示這些選項。

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `bit_depth` | 所儲存 EXR 檔案的位元深度。（預設值："32-bit float"） | COMBO | 是（條件性） | `"32-bit float"` |
| `input_color_space` | 輸入張量的色彩空間。EXR 一律以相符色域中的場景線性（scene-linear）寫入。<br>`"sRGB"` — 輸入為 sRGB 編碼的 Rec.709；會套用反向 sRGB EOTF。<br>`"HDR"` — 輸入為 HLG 編碼的 Rec.2020（BT.2100）；會套用反向 HLG OETF 以取得場景線性光。<br>`"linear"` — 輸入已是場景線性（Rec.709 原色）；直接原樣寫入。若輸出來自渲染器/合成器，請使用此選項。（預設值："sRGB"） | COMBO | 是（條件性） | `"sRGB"`<br>`"HDR"`<br>`"linear"` |

### AVIF 輸入

當 `format` 設定為 `"avif"` 時，會顯示這些選項。

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `bit_depth` | 所儲存 AVIF 檔案的位元深度。自動（Auto）會對 sRGB 使用 8 位元 YUV420，對 HDR 使用 10 位元 YUV420。（預設值："auto"） | COMBO | 是（條件性） | `"auto"`<br>`"8-bit YUV420"`<br>`"10-bit YUV420"` |
| `input_color_space` | 輸入圖像的色彩空間。HDR 會選用 BT.2020/HLG，HDR PQ 會選用 BT.2020/PQ。（預設值："sRGB"） | COMBO | 是（條件性） | `"sRGB"`<br>`"HDR"`<br>`"HDR PQ"` |
| `crf` | 數值越低，品質越高，檔案越大。（預設值：18） | INT | 是（條件性） | 1 至 63 |
| `save_mode` | AVIF 檔案的儲存模式。`"still images"` 會將批次中的每張圖像儲存為獨立的靜態檔案；`"animated"` 會將整個批次儲存為單一動畫 AVIF 檔案，並顯示 `fps` 和 `loop_count`。（預設值："still images"） | DYNAMIC_COMBO | 是（條件性） | `"still images"`<br>`"animated"` |

### AVIF 動畫選項

當 `save_mode` 設定為 `"animated"` 時，會顯示這些選項。

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `fps` | 動畫的幀率。（預設值：6.0） | FLOAT | 是（條件性） | 0.01 至 1000.0 |
| `loop_count` | 動畫重複播放的次數。0 表示無限循環。（預設值：0） | INT | 是（條件性） | 0 至 1000 |

**關於參數依賴性的說明：**
- 格式專屬參數（`bit_depth`、`input_color_space`，以及 AVIF 的 `crf` 和 `save_mode`）只有在選定特定 `format` 時才可使用。
- 對於 PNG 格式，僅提供 "8-bit" 和 "16-bit" 位元深度，且色彩空間僅提供 "sRGB"。
- 對於 EXR 格式，僅提供 "32-bit float" 位元深度，色彩空間則有 "sRGB"、"HDR" 或 "linear"。
- 對於 AVIF 格式，`fps` 和 `loop_count` 只有在 `save_mode` 設定為 `"animated"` 時才可使用。
- PNG 和 EXR 圖像必須具有 1（灰階）、3（RGB）或 4（RGBA）個通道；其他通道數不受支援，會引發錯誤。
- AVIF 僅支援 1 通道灰階和 3 通道 RGB 圖像；RGBA（Alpha）圖像不受支援，會引發錯誤。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `images` | 輸入圖像，原樣傳遞。節點的 UI 輸出會提供已儲存圖像結果的清單，每個結果都包含檔案名稱、子資料夾及類型（"output"）。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImageAdvanced/zh-TW.md)

---
**Source fingerprint (SHA-256):** `d3df3caca99d58d973d0bc2ff7c22c4626185d390ec2acf870d4014331c4c335`
