# Topaz 影像增強

Topaz Image Enhance 使用 Topaz 模型，對單一輸入影像套用業界標準的放大與影像增強。它會將影像傳送至 Topaz API，使用所選模型進行處理，並傳回增強後的結果。您可以從三種模型中選擇：Reimagine、Bloom 2 和 Wonder 3.5。

## 輸入

### 通用輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `image` | 要增強的輸入影像。僅支援一張輸入影像。 | IMAGE | 是 | Single image |
| `model` | 要使用的 Topaz 增強模型。所選模型會決定顯示哪些模型特定設定。 | DYNAMIC_COMBO | 是 | `"Reimagine"`<br>`"Bloom 2"`<br>`"Wonder 3.5"` |
| `output_width` | 值為零表示自動計算（通常會是原始尺寸，或若指定了 `output_height`，則依比例縮放至該高度）。Wonder 3.5 僅支援 1x 至 6x 的放大倍率。Bloom 2 和 Wonder 3.5 會保留輸入的長寬比，並將要求的尺寸視為目標。（預設值：0） | INT | 否 | 0 至 32000 |
| `output_height` | 值為零表示輸出與原始高度相同，或若指定了 `output_width`，則依比例縮放至該寬度。Wonder 3.5 僅支援 1x 至 6x 的放大倍率。Bloom 2 和 Wonder 3.5 會保留輸入的長寬比，並將要求的尺寸視為目標。（預設值：0） | INT | 否 | 0 至 32000 |

### Reimagine 輸入

當 `model` 設為 `"Reimagine"` 時，這些設定會生效。

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 用於引導創意放大的選用文字提示。（預設值：""） | STRING | 是 | Any text |
| `creativity` | 增強的創意程度。（預設值：3） | INT | 是 | 1 至 9 |
| `subject_detection` | 主體偵測模式（進階）。 | COMBO | 是 | `"All"`<br>`"Foreground"`<br>`"Background"` |
| `face_enhancement` | 處理期間增強臉部（若有）。（預設值：True） | BOOLEAN | 是 | true<br>false |
| `face_enhancement_creativity` | 設定臉部增強的創意程度。（預設值：0.0） | FLOAT | 是 | 0.0 至 1.0 |
| `face_enhancement_strength` | 控制增強後臉部相對於背景的銳利程度。（預設值：1.0） | FLOAT | 是 | 0.0 至 1.0 |
| `face_preservation` | 保留主體的面部身分特徵。（預設值：True） | BOOLEAN | 是 | true<br>false |
| `color_preservation` | 保留原始色彩。（預設值：True） | BOOLEAN | 是 | true<br>false |
| `crop_to_fill` | 預設情況下，當輸出長寬比不同時，影像會以黑邊填充。啟用後會裁切影像以填滿輸出尺寸。（預設值：False） | BOOLEAN | 是 | true<br>false |

### Bloom 2 輸入

當 `model` 設為 `"Bloom 2"` 時，這些設定會生效。

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 用於生成的選用文字提示。留空會從輸入影像自動生成提示。（預設值：""） | STRING | 是 | Any text |
| `creativity` | 1 為克制的增強，9 為明顯重新詮釋並生成新細節。（預設值：3） | INT | 是 | 1 至 9 |
| `seed` | 用於可重現生成的種子。（預設值：2） | INT | 是 | 1 至 2000 |
| `color_preservation` | 保留原始色彩。（預設值：True） | BOOLEAN | 是 | true<br>false |
| `grain` | 為輸出影像加入顆粒。（預設值：False） | BOOLEAN | 是 | true<br>false |
| `grain_model` | 要使用的顆粒模型。若停用顆粒，則會忽略。 | COMBO | 是 | `"silver"`<br>`"gaussian"`<br>`"grey"` |
| `grain_strength` | 顆粒效果的強度。若停用顆粒，則會忽略。（預設值：0.5） | FLOAT | 是 | 0.0 至 1.0 |
| `grain_size` | 顆粒的大小。若停用顆粒，則會忽略。（預設值：1.0） | FLOAT | 是 | 1.0 至 5.0 |
| `grain_density` | 顆粒效果的濃度。若停用顆粒，則會忽略。（預設值：0.5） | FLOAT | 是 | 0.0 至 1.0 |

### Wonder 3.5 輸入

當 `model` 設為 `"Wonder 3.5"` 時，這些設定會生效。

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `enhancement_strength` | 針對不同輸入條件的增強等級。（預設值："high"） | COMBO | 是 | `"low"`<br>`"medium"`<br>`"high"` |
| `grain` | 為輸出影像加入顆粒。（預設值：False） | BOOLEAN | 是 | true<br>false |
| `grain_model` | 要使用的顆粒模型。若停用顆粒，則會忽略。 | COMBO | 是 | `"silver"`<br>`"gaussian"`<br>`"grey"` |
| `grain_strength` | 顆粒效果的強度。若停用顆粒，則會忽略。（預設值：0.5） | FLOAT | 是 | 0.0 至 1.0 |
| `grain_size` | 顆粒的大小。若停用顆粒，則會忽略。（預設值：1.0） | FLOAT | 是 | 1.0 至 5.0 |
| `grain_density` | 顆粒效果的濃度。若停用顆粒，則會忽略。（預設值：0.5） | FLOAT | 是 | 0.0 至 1.0 |

**注意：** 僅支援一張輸入影像；若輸入批次包含多於一張影像，節點會拋出錯誤。除非啟用 `grain`，否則會忽略顆粒設定（`grain_model`、`grain_strength`、`grain_size`、`grain_density`）。對於 Bloom 2，將 `prompt` 留空會自動從輸入影像生成提示。Wonder 3.5 僅支援 1x 至 6x 的放大倍率；Bloom 2 和 Wonder 3.5 會保留輸入的長寬比，並將要求的尺寸視為目標。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `IMAGE` | Topaz API 傳回的增強與放大後影像。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TopazImageEnhanceV2/zh-TW.md)

---
**Source fingerprint (SHA-256):** `19bb03ca7354f1b0d1e559b742b83939678fce6d5f490b1030717b846043e0e6`
