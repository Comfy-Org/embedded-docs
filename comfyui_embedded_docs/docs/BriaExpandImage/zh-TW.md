# BriaExpandImage

Bria Expand Image 會透過 Bria 生成新內容，將影像擴展到原始邊界之外。您可以選擇目標長寬比、自訂比例，或在畫布上手動放置原始影像。擴展過程可由文字提示詞引導；若提示詞留空，Bria 會自動生成提示詞。

## 輸入

| 參數 | 描述 | 資料型別 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `影像` | 要擴展的輸入影像。 | IMAGE | 是 | — |
| `擴展模式` | 擴展後影像的目標形狀：預設長寬比、自訂比例，或在畫布上手動放置原始影像。只有 `manual` 模式能達到高於 1:2 的畫布。選取 `custom_ratio` 會顯示 `ratio_width` 和 `ratio_height`。選取 `manual` 會顯示畫布與影像放置參數。 | DYNAMIC_COMBO | 是 | `"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"4:5"`<br>`"5:4"`<br>`"9:16"`<br>`"16:9"`<br>`"custom_ratio"`<br>`"manual"` |
| `ratio_width` | 目標比例的寬邊：21 和 9 即為 21:9。預設值：21。 | INT | 條件式 | 1–100 |
| `ratio_height` | 目標比例的高邊：21 和 9 即為 21:9。Bria 僅接受 0.5 到 3.0 之間的寬高比，因此任何高於 1:2 的比例都需要使用 `manual` 模式。預設值：9。 | INT | 條件式 | 1–100 |
| `canvas_width` | 輸出畫布的寬度（像素）。預設值：1000。 | INT | 條件式 | 64–5000 |
| `canvas_height` | 輸出畫布的高度（像素）。預設值：1000。 | INT | 條件式 | 64–5000 |
| `image_width` | 原始影像在畫布中的寬度。預設值：500。 | INT | 條件式 | 1–5000 |
| `image_height` | 原始影像在畫布中的高度。預設值：500。 | INT | 條件式 | 1–5000 |
| `image_x` | 影像左上角在畫布內的 X 座標；可能落在畫布之外，導致影像被裁切。預設值：250。 | INT | 條件式 | -5000–5000 |
| `image_y` | 影像左上角在畫布內的 Y 座標；可能落在畫布之外，導致影像被裁切。預設值：250。 | INT | 條件式 | -5000–5000 |
| `提示詞` | 擴展場景的選用描述；若為空白，Bria 會根據影像自動生成描述。預設值：空字串。 | STRING | 否 | Any string |
| `負面提示詞` | 擴展的選用負面提示詞。預設值：空字串。 | STRING | 否 | Any string |
| `種子` | 隨機生成過程的種子。預設值：42。 | INT | 否 | 1–2147483647 |
| `內容審核` | 內容審核設定。設為 `true` 時，會顯示額外的內容審核選項。 | DYNAMIC_COMBO | 否 | `"false"`<br>`"true"` |
| `prompt_content_moderation` | 若啟用，會審核提示詞內容。預設值：false。僅在 `moderation` 為 `true` 時可用。 | BOOLEAN | 條件式 | true/false |
| `visual_input_moderation` | 若啟用，會審核視覺輸入。預設值：false。僅在 `moderation` 為 `true` 時可用。 | BOOLEAN | 條件式 | true/false |
| `visual_output_moderation` | 若啟用，會審核視覺輸出。預設值：false。僅在 `moderation` 為 `true` 時可用。 | BOOLEAN | 條件式 | true/false |

當 `expand_mode` 為 `custom_ratio` 時，`ratio_width` 和 `ratio_height` 會定義目標長寬比。Bria 僅接受 0.5 到 3.0 之間的寬高比。若比例超出此範圍，系統會回報錯誤，此時應改用 `manual` 模式。

當 `expand_mode` 為 `manual` 時，原始影像會以指定的尺寸與位置放置在畫布上。影像可能超出畫布範圍，超出部分將被裁切。

當 `moderation` 為 `true` 時，會將三個內容審核布林值傳送給 Bria。當 `moderation` 為 `false` 時，則會忽略這些值。

## 輸出

| 輸出名 | 描述 | 資料型別 |
|-------------|-------------|-----------|
| `image` | Bria 生成的擴展後影像。 | IMAGE |
| `提示詞` | 用於擴展的提示詞；當提示詞輸入為空時，由 Bria 自動生成。 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaExpandImage/zh-TW.md)

---
**Source fingerprint (SHA-256):** `d2c9431837f200ccbcb39037f7b26013494c4dea3d40d899db4e717ddbbea71c`
