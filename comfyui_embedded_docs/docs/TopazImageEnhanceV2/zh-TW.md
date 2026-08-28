# Topaz 影像增強

Topaz Image Enhance 使用 Topaz 模型對單一輸入影像套用業界標準的升頻與影像增強處理。它將影像傳送至 Topaz API，以選定的模型進行處理，並回傳增強後的結果。您可以從三種模型中選擇：Reimagine、Bloom 2 和 Wonder 3.5。

## 輸入

### 通用輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `image` | 要增強的輸入影像。僅支援一張輸入影像。 | IMAGE | 是 | 單張影像 |
| `model` | 要使用的 Topaz 增強模型。所選模型決定會顯示哪些模型特定設定。 | DYNAMIC_COMBO | 是 | `"Reimagine"`<br>`"Bloom 2"`<br>`"Wonder 3.5"` |
| `output_width` | 零值表示自動計算（通常會是原始大小，或若指定 `output_height` 則按比例縮放）。Wonder 3.5 僅支援 1x 至 6x 的放大倍率。Bloom 2 和 Wonder 3.5 會保留輸入影像的長寬比，並將要求的尺寸視為目標。（預設值：0） | INT | 否 | 0 至 32000 |
| `output_height` | 零值表示輸出與原始高度相同，或若指定 `output_width` 則按比例縮放。Wonder 3.5 僅支援 1x 至 6x 的放大倍率。Bloom 2 和 Wonder 3.5 會保留輸入影像的長寬比，並將要求的尺寸視為目標。（預設值：0） | INT | 否 | 0 至 32000 |

### Reimagine 輸入

這些設定在 `model` 設定為 `"Reimagine"` 時套用。

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 選擇性的文字提示，用於創意升頻引導。（預設值：""） | STRING | 是 | 任何文字 |
| `creativity` | 增強效果的創意程度。（預設值：3） | INT | 是 | 1 至 9 |
| `subject_detection` | 主體偵測模式。 | COMBO | 是 | `"All"`<br>`"Foreground"`<br>`"Background"` |
| `face_enhancement` | 在處理期間增強臉部（若存在）。（預設值：True） | BOOLEAN | 是 | true<br>false |
| `face_enhancement_creativity` | 設定臉部增強的創意程度。（預設值：0.0） | FLOAT | 是 | 0.0 至 1.0 |
| `face_enhancement_strength` | 控制增強後的臉部相對於背景的銳利程度。（預設值：1.0） | FLOAT | 是 | 0.0 至 1.0 |
| `face_preservation` | 保留主體的面部身份。（預設值：True） | BOOLEAN | 是 | true<br>false |
| `color_preservation` | 保留原始色彩。（預設值：True） | BOOLEAN | 是 | true<br>false |
| `crop_to_fill` | 預設情況下，當輸出長寬比不同時，影像會加上黑邊。啟用此選項可裁切影像以填滿輸出尺寸。（預設值：False） | BOOLEAN | 是 | true<br>false |

### Bloom 2 輸入

這些設定在 `model` 設定為 `"Bloom 2"` 時套用。

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 選擇性的生成文字提示。留空會從輸入影像自動產生提示。（預設值：""） | STRING | 是 | 任何文字 |
| `creativity` | 1 為保守增強，9 為以新生成的細節進行明顯重新詮釋。（預設值：3） | INT | 是 | 1 至 9 |
| `seed` | 用於可重現生成的種子。（預設值：2） | INT | 是 | 1 至 2000 |
| `color_preservation` | 保留原始色彩。（預設值：True） | BOOLEAN | 是 | true<br>false |
| `grain` | 為輸出影像增加顆粒感。（預設值：False） | BOOLEAN | 是 | true<br>false |
| `grain_model` | 要使用的顆粒模型。若停用顆粒效果則忽略。 | COMBO | 是 | `"silver"`<br>`"gaussian"`<br>`"grey"` |
| `grain_strength` | 顆粒效果的強度。若停用顆粒效果則忽略。（預設值：0.5） | FLOAT | 是 | 0.0 至 1.0 |
| `grain_size` | 顆粒粒子的大小。若停用顆粒效果則忽略。（預設值：1.0） | FLOAT | 是 | 1.0 至 5.0 |
| `grain_density` | 顆粒效果的密度。若停用顆粒效果則忽略。（預設值：0.5） | FLOAT | 是 | 0.0 至 1.0 |

### Wonder 3.5 輸入

這些設定在 `model` 設定為 `"Wonder 3.5"` 時套用。

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `enhancement_strength` | 針對不同輸入條件的增強等級。（預設值："high"） | COMBO | 是 | `"low"`<br>`"medium"`<br>`"high"` |
| `grain` | 為輸出影像增加顆粒感。（預設值：False） | BOOLEAN | 是 | true<br>false |
| `grain_model` | 要使用的顆粒模型。若停用顆粒效果則忽略。 | COMBO | 是 | `"silver"`<br>`"gaussian"`<br>`"grey"` |
| `grain_strength` | 顆粒效果的強度。若停用顆粒效果則忽略。（預設值：0.5） | FLOAT | 是 | 0.0 至 1.0 |
| `grain_size` | 顆粒粒子的大小。若停用顆粒效果則忽略。（預設值：1.0） | FLOAT | 是 | 1.0 至 5.0 |
| `grain_density` | 顆粒效果的密度。若停用顆粒效果則忽略。（預設值：0.5） | FLOAT | 是 | 0.0 至 1.0 |

**注意：** 僅支援一張輸入影像。除非啟用 `grain`，否則顆粒設定（`grain_model`、`grain_strength`、`grain_size`、`grain_density`）會被忽略。對於 Bloom 2，將 `prompt` 留空會自動從輸入影像產生提示。Wonder 3.5 僅支援 1x 至 6x 的放大倍率；Bloom 2 和 Wonder 3.5 會保留輸入影像的長寬比，並將要求的尺寸視為目標。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `IMAGE` | Topaz API 回傳的增強且升頻後的影像。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TopazImageEnhanceV2/zh-TW.md)

---
**Source fingerprint (SHA-256):** `19bb03ca7354f1b0d1e559b742b83939678fce6d5f490b1030717b846043e0e6`
