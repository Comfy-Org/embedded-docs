# BriaExpandImage

Bria Expand Image 透過使用 Bria 生成新內容，將影像擴展到原始邊界之外。它讓您選擇目標寬高比、自訂比例，或透過手動放置原始影像來定義畫布。擴展過程可由文字提示引導；若提示留空，Bria 將自動生成提示。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `image` | 要擴展的輸入影像。 | IMAGE | 是 | — |
| `expand_mode` | 擴展影像的目標形狀：預設寬高比、自訂比例，或在畫布上手動放置原始影像。手動是唯一能達到高於 1:2 的畫布的模式。選擇 `custom_ratio` 會顯示 `ratio_width` 和 `ratio_height`。選擇 `manual` 會顯示畫布和影像放置參數。 | COMBO | 是 | `"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"4:5"`<br>`"5:4"`<br>`"9:16"`<br>`"16:9"`<br>`"custom_ratio"`<br>`"manual"` |
| `ratio_width` | 目標比例的寬邊：21 和 9 表示 21:9。預設值：21。 | INT | 條件 | 1–100 |
| `ratio_height` | 目標比例的高邊：21 和 9 表示 21:9。Bria 僅接受寬高比在 0.5 到 3.0 之間，因此任何高於 1:2 的比例都需要使用手動模式。預設值：9。 | INT | 條件 | 1–100 |
| `canvas_width` | 輸出畫布的寬度（像素）。預設值：1000。 | INT | 條件 | 64–5000 |
| `canvas_height` | 輸出畫布的高度（像素）。預設值：1000。 | INT | 條件 | 64–5000 |
| `image_width` | 畫布中原始影像的寬度。預設值：500。 | INT | 條件 | 1–5000 |
| `image_height` | 畫布中原始影像的高度。預設值：500。 | INT | 條件 | 1–5000 |
| `image_x` | 影像左上角在畫布內的 X 位置；可能落在畫布外，導致影像被裁切。預設值：250。 | INT | 條件 | -5000–5000 |
| `image_y` | 影像左上角在畫布內的 Y 位置；可能落在畫布外，導致影像被裁切。預設值：250。 | INT | 條件 | -5000–5000 |
| `prompt` | 擴展場景的選用描述；若為空，Bria 會根據影像自動生成。預設值：空字串。 | STRING | 否 | 任何字串 |
| `negative_prompt` | 擴展的選用負面提示。預設值：空字串。 | STRING | 否 | 任何字串 |
| `seed` | 隨機生成過程的種子。預設值：42。 | INT | 否 | 1–2147483647 |
| `moderation` | 審核設定。設為 `true` 時，會顯示額外的審核選項。 | COMBO | 否 | `"false"`<br>`"true"` |
| `prompt_content_moderation` | 若啟用，會審核提示內容。預設值：false。僅在 `moderation` 為 `true` 時可用。 | BOOLEAN | 條件 | true/false |
| `visual_input_moderation` | 若啟用，會審核視覺輸入。預設值：false。僅在 `moderation` 為 `true` 時可用。 | BOOLEAN | 條件 | true/false |
| `visual_output_moderation` | 若啟用，會審核視覺輸出。預設值：false。僅在 `moderation` 為 `true` 時可用。 | BOOLEAN | 條件 | true/false |

當 `expand_mode` 為 `custom_ratio` 時，`ratio_width` 和 `ratio_height` 定義目標寬高比。Bria 僅接受寬高比在 0.5 到 3.0 之間。若比例超出此範圍，系統會報錯，此時應改用 `manual` 模式。

當 `expand_mode` 為 `manual` 時，原始影像會以指定的大小和位置放置在畫布上。影像可能超出畫布，此時超出部分將被裁切。

當 `moderation` 為 `true` 時，三個審核布林值會傳送給 Bria。當 `moderation` 為 `false` 時，這些值會被忽略。

## 輸出

| 輸出名 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `image` | 由 Bria 生成的擴展影像。 | IMAGE |
| `prompt` | 用於擴展的提示；當提示輸入為空時，由 Bria 自動生成。 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaExpandImage/zh-TW.md)

---
**Source fingerprint (SHA-256):** `d2c9431837f200ccbcb39037f7b26013494c4dea3d40d899db4e717ddbbea71c`
