# TopazImageEnhanceV2

Topaz Image Enhance 使用 Topaz 模型對單一輸入圖片套用業界標準的放大與影像增強處理。它會將圖片傳送到 Topaz API，以所選模型進行處理，並回傳增強後的結果。您可以從三種模型中選擇：Reimagine、Bloom 2 和 Wonder 3.5。

## 輸入
| 參數 | 描述 | 資料型別 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `image` | 要增強的輸入圖片。僅支援單一輸入圖片。 | IMAGE | 是 | Single image |
| `model` | 要使用的 Topaz 增強模型。所選模型會決定顯示哪些模型專屬設定。 | STRING | 是 | `"Reimagine"`<br>`"Bloom 2"`<br>`"Wonder 3.5"` |
| `output_width` | 值為零時表示自動計算（通常會保持原始尺寸，或若指定了 `output_height` 則按比例縮放）。Wonder 3.5 僅支援 1x 到 6x 的放大倍率。Bloom 2 和 Wonder 3.5 會保留輸入圖片的長寬比，並將要求的尺寸視為目標。（預設值：0） | INT | 否 | 0 to 32000 |
| `output_height` | 值為零時表示輸出與原始高度相同，或若指定了 `output_width` 則按比例縮放。Wonder 3.5 僅支援 1x 到 6x 的放大倍率。Bloom 2 和 Wonder 3.5 會保留輸入圖片的長寬比，並將要求的尺寸視為目標。（預設值：0） | INT | 否 | 0 to 32000 |

### Reimagine 設定

當 `model` 設定為 `"Reimagine"` 時，這些設定會套用。

| 參數 | 描述 | 資料型別 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 用於創意放大引導的選用文字提示。（預設值：""） | STRING | 是 | Any text |
| `creativity` | 增強效果的創意程度。（預設值：3） | INT | 是 | 1 to 9 |
| `subject_detection` | 主體偵測模式。 | STRING | 是 | `"All"`<br>`"Foreground"`<br>`"Background"` |
| `face_enhancement` | 在處理期間增強臉部（若有的話）。（預設值：True） | BOOLEAN | 是 | true<br>false |
| `face_enhancement_creativity` | 設定臉部增強的創意程度。（預設值：0.0） | FLOAT | 是 | 0.0 to 1.0 |
| `face_enhancement_strength` | 控制增強後臉部相對於背景的銳利程度。（預設值：1.0） | FLOAT | 是 | 0.0 to 1.0 |
| `face_preservation` | 保留主體的面部特徵。（預設值：True） | BOOLEAN | 是 | true<br>false |
| `color_preservation` | 保留原始色彩。（預設值：True） | BOOLEAN | 是 | true<br>false |
| `crop_to_fill` | 預設情況下，當輸出長寬比不同時，圖片會以信箱模式（letterbox）呈現。啟用此選項會裁切圖片以填滿輸出尺寸。（預設值：False） | BOOLEAN | 是 | true<br>false |

### Bloom 2 設定

當 `model` 設定為 `"Bloom 2"` 時，這些設定會套用。

| 參數 | 描述 | 資料型別 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 用於生成的選用文字提示。留空則會從輸入圖片自動產生提示。（預設值：""） | STRING | 是 | Any text |
| `creativity` | 1 為保守增強，9 為明顯的重新詮釋並產生新的細節。（預設值：3） | INT | 是 | 1 to 9 |
| `seed` | 用於可重現生成的種子。（預設值：2） | INT | 是 | 1 to 2000 |
| `color_preservation` | 保留原始色彩。（預設值：True） | BOOLEAN | 是 | true<br>false |
| `grain` | 為輸出圖片添加顆粒效果。（預設值：False） | BOOLEAN | 是 | true<br>false |
| `grain_model` | 要使用的顆粒模型。若停用顆粒效果，則此設定會被忽略。 | STRING | 是 | `"silver"`<br>`"gaussian"`<br>`"grey"` |
| `grain_strength` | 顆粒效果的強度。若停用顆粒效果，則此設定會被忽略。（預設值：0.5） | FLOAT | 是 | 0.0 to 1.0 |
| `grain_size` | 顆粒粒子的大小。若停用顆粒效果，則此設定會被忽略。（預設值：1.0） | FLOAT | 是 | 1.0 to 5.0 |
| `grain_density` | 顆粒效果的密度。若停用顆粒效果，則此設定會被忽略。（預設值：0.5） | FLOAT | 是 | 0.0 to 1.0 |

### Wonder 3.5 設定

當 `model` 設定為 `"Wonder 3.5"` 時，這些設定會套用。

| 參數 | 描述 | 資料型別 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `enhancement_strength` | 針對不同輸入條件的增強程度。（預設值："high"） | STRING | 是 | `"low"`<br>`"medium"`<br>`"high"` |
| `grain` | 為輸出圖片添加顆粒效果。（預設值：False） | BOOLEAN | 是 | true<br>false |
| `grain_model` | 要使用的顆粒模型。若停用顆粒效果，則此設定會被忽略。 | STRING | 是 | `"silver"`<br>`"gaussian"`<br>`"grey"` |
| `grain_strength` | 顆粒效果的強度。若停用顆粒效果，則此設定會被忽略。（預設值：0.5） | FLOAT | 是 | 0.0 to 1.0 |
| `grain_size` | 顆粒粒子的大小。若停用顆粒效果，則此設定會被忽略。（預設值：1.0） | FLOAT | 是 | 1.0 to 5.0 |
| `grain_density` | 顆粒效果的密度。若停用顆粒效果，則此設定會被忽略。（預設值：0.5） | FLOAT | 是 | 0.0 to 1.0 |

## 輸出
| 輸出名稱 | 描述 | 資料型別 |
|-------------|-------------|-----------|
| `IMAGE` | 由 Topaz API 回傳的增強且放大後的圖片。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TopazImageEnhanceV2/zh-TW.md)

---
**Source fingerprint (SHA-256):** `4301abb7cbab5122490b2ed3b328b199a29409da0dcc5ea5201570c2acbc2a58`
