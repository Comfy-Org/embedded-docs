# Google Gemini Omni（影片）

Google Gemini Omni (Video) 使用 Google 的 Gemini Omni Flash 模型，從文字提示生成帶有音訊的影片。您可以選擇性地附加參考圖片和／或影片來引導結果，或編輯現有素材。請直接在提示中描述所需的長度（3-10 秒）。

## 輸入

### 通用輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `模型` | 用於生成影片的 Gemini 影片模型。 | DYNAMIC_COMBO | 是 | "Omni Flash 1.1"<br>"Omni Flash" |

### Omni Flash 1.1 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 描述要生成的影片，或要套用於所附加影片的編輯。請直接在提示中指定長度，例如「a 6-second clip」；或用於「extend」任務的「extend by 5 seconds」。生成的長度可為 3-10 秒，預設為 10。輸出包含音訊。（預設值：""） | STRING | 是 | - |
| `resolution` | 輸出解析度。（預設值："720p"） | COMBO | 是 | "360p"<br>"720p"<br>"1080p"<br>"4k" |
| `aspect_ratio` | 輸出長寬比：16:9（橫向）或 9:16（直向）。「edit」和「extend」任務則會保留輸入影片的長寬比。（預設值："16:9"） | COMBO | 是 | "16:9"<br>"9:16" |
| `task_type` | 提示與所附加媒體的處理方式。使用「auto」時，由模型自行決定。「text_to_video」僅根據提示生成，並拒絕附加媒體。「image_to_video」將單張圖片動畫化，若附加兩張圖片，則會從起始幀插值到結束幀。「reference_to_video」將所附加的媒體視為主體參考。「edit」會改寫恰好一段附加的影片，而「extend」會在該影片後附加新素材，因此輸出會以輸入影片開頭。（預設值："auto"） | COMBO | 是 | "auto"<br>"text_to_video"<br>"image_to_video"<br>"reference_to_video"<br>"edit"<br>"extend" |
| `seed` | 種子控制節點是否應重新執行；無論種子為何，結果皆為非確定性。（預設值：42） | INT | 是 | 0 至 2147483647 |

### Omni Flash 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 描述要生成的影片，或要套用於所附加影片的編輯。請直接在提示中指定長度，例如「a 6-second clip」；長度可為 3-10 秒。輸出為 720p、24 FPS，並包含音訊。（預設值：""） | STRING | 是 | - |
| `aspect_ratio` | 輸出長寬比：16:9（橫向）或 9:16（直向）。「edit」任務則會保留輸入影片的長寬比。（預設值："16:9"） | COMBO | 是 | "16:9"<br>"9:16" |
| `task_type` | 提示與所附加媒體的處理方式。使用「auto」時，由模型自行決定。「text_to_video」僅根據提示生成，並拒絕附加媒體。「image_to_video」將單張圖片動畫化，若附加兩張圖片，則會從起始幀插值到結束幀。「reference_to_video」將所附加的媒體視為主體參考。「edit」會改寫恰好一段附加的影片。（預設值："auto"） | COMBO | 是 | "auto"<br>"text_to_video"<br>"image_to_video"<br>"reference_to_video"<br>"edit" |
| `temperature` | 控制隨機性。數值越低越集中／確定，數值越高越多變。（預設值：1.0） | FLOAT | 是 | 0.0 至 2.0 (step 0.01) |
| `top_p` | 核採樣：從累積機率達到 top_p 的最小 token 集合中進行採樣。（預設值：0.95） | FLOAT | 是 | 0.0 至 1.0 (step 0.01) |
| `seed` | 種子控制節點是否應重新執行；無論種子為何，結果皆為非確定性。（預設值：42） | INT | 是 | 0 至 2147483647 |

### 參考輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `images` | 可擴充插槽：最多可連接 14 張圖片（`image_1`...`image_14`）。可選的參考圖片，用於引導或動畫化影片。在「image_to_video」任務中，第一張為起始幀，可選的第二張為結束幀。 | IMAGE | 否 | 0 至 14 images |
| `videos` | 可擴充插槽：最多可連接 3 段影片（`video_1`...`video_3`）。可選的參考影片，用於引導或編輯。每段最長 10 秒。 | VIDEO | 否 | 0 至 3 videos |

**注意事項：**

- `prompt` 不得為空；若為空，節點會引發錯誤。
- 「text_to_video」任務僅根據提示生成——附加圖片或影片會引發錯誤。
- 「image_to_video」任務僅接受圖片（不接受影片），且需要恰好 1 或 2 張圖片：第一張為起始幀，可選的第二張為結束幀。
- 「edit」任務（兩種模型）與「extend」任務（僅 Omni Flash 1.1）需要恰好一段輸入影片，並保留該輸入影片的長寬比，覆寫 `aspect_ratio`。
- 最多可附加 14 張圖片與 3 段影片，且每段附加影片不得超過 10 秒。
- Omni Flash 一律輸出 720p 24 FPS 且含音訊的影片；解析度選擇僅在 Omni Flash 1.1 提供。
- `temperature` 與 `top_p` 控制參數僅在 Omni Flash 模型中提供；Omni Flash 1.1 使用固定的生成設定。

## 輸出

| 輸出名 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `video`（第一個輸出） | 生成且帶有音訊的影片。Omni Flash：720p、24 FPS。Omni Flash 1.1：在 `resolution` 輸入中選擇的解析度。 | VIDEO |
| `text`（第二個輸出） | 模型隨影片一同生成的文字內容（可能為空）。 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiVideoOmniV2/zh-TW.md)

---
**Source fingerprint (SHA-256):** `7a0dda4bcd662c9df3c680297ec9de7886d35e618de8b3ce0cd95b9afd13a892`
