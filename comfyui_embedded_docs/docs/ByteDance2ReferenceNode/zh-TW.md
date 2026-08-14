# ByteDance Seedance 2.0 參考轉影片

此節點使用 ByteDance 的 Seedance 2.5 或 2.0 AI 模型來生成、編輯或擴展影片。您可以透過文字提示來描述影片，並可添加參考圖片、影片和音訊來引導結果。它支援多模態參考輸入、影片編輯和影片擴展。

## 輸入
選擇 `model` 會決定以下哪些參數可用。僅在選取 Seedance 2.5 時，才會顯示 `video_editing` 和 `output_format`。

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|------|------|----------|------|------|
| `model` | 用於生成影片的 AI 模型。Seedance 2.5 是最新模型，可生成長達 30 秒的影片，並輸出 mp4/mov 格式；Seedance 2.0 提供最高品質與 1080p/4k 解析度；Fast 版為速度最佳化；Mini 版則是最快且成本最低的生成選項。選取模型後，下方會顯示該模型專屬的輸入項目。 | COMBO | 是 | `"Seedance 2.5"`<br>`"Seedance 2.0"`<br>`"Seedance 2.0 Fast"`<br>`"Seedance 2.0 Mini"` |
| `seed` | 種子控制節點是否應重新執行；無論種子值為何，結果都是非確定性的（預設值：0）。 | INT | 是 | 0 至 2147483647 |
| `watermark` | 是否在影片中添加浮水印（預設值：False）。 | BOOLEAN | 是 | `True`<br>`False` |
| `prompt` | 用於影片生成的文字提示。對於 Seedance 2.5，請將口語台詞放入雙引號中以引導生成的對話。必須包含至少一個非空白字元。 | STRING | 是 | Any text |
| `resolution` | 輸出影片的解析度。Seedance 2.5、2.0 Fast 和 2.0 Mini 提供 480p 與 720p；Seedance 2.0 另提供 1080p 與 4k（Seedance 2.5 預設值：720p）。 | COMBO | 是 | `"480p"`<br>`"720p"`<br>`"1080p"`<br>`"4k"` |
| `ratio` | 輸出影片的長寬比（Seedance 2.5 預設值：`"16:9"`；Seedance 2.0 模型預設值：`"adaptive"`）。 | COMBO | 是 | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | 輸出影片的持續時間（秒）（Seedance 2.5：4-30，預設值 5；Seedance 2.0 模型：4-15，預設值 7）。 | INT | 是 | 4 至 30 (Seedance 2.5)<br>4 至 15 (Seedance 2.0)<br>Step: 1 |
| `generate_audio` | 是否為輸出影片啟用音訊生成（預設值：True）。 | BOOLEAN | 是 | `True`<br>`False` |
| `video_editing` | 僅限 Seedance 2.5。當提示詞要編輯已連接的參考影片時（例如替換其中的物件），請啟用此選項。輸出將保留來源剪輯自身的長度與長寬比，且 `duration` 和 `ratio` 控制項會被忽略。保持停用以生成新影片，或將影片擴展到您設定的持續時間（預設值：False）。 | BOOLEAN | 是 | `True`<br>`False` |
| `output_format` | 僅限 Seedance 2.5。輸出影片的容器格式（預設值：`"mp4"`）。 | COMBO | 是 | `"mp4"` |
| `reference_images` | 用於引導影片生成的參考圖片。圖片會自動縮小至最大邊長 6000 像素，且必須至少為 300x300 像素，長寬比介於 0.4 與 2.5 之間。 | IMAGE | 否 | Up 至 30 (Seedance 2.5)<br>Up 至 9 (Seedance 2.0) |
| `reference_videos` | 用於引導影片生成的參考影片；可用於影片編輯與擴展。 | VIDEO | 否 | Up 至 10 (Seedance 2.5)<br>Up 至 3 (Seedance 2.0) |
| `reference_audios` | 用於引導影片生成的參考音訊片段。 | AUDIO | 否 | Up 至 10 (Seedance 2.5)<br>Up 至 3 (Seedance 2.0) |
| `auto_downscale` | 自動縮小超過所選解析度之模型像素預算的參考影片。保留長寬比；已在限制內的影片不會被變更（預設值：True）。 | BOOLEAN | 否 | `True`<br>`False` |
| `auto_upscale` | 自動放大低於所選解析度之模型最小像素數的參考影片。保留長寬比；已達到最小值的影片不會被變更。注意：放大低解析度來源不會增加真實細節，並可能產生品質較低的生成結果（預設值：False）。 | BOOLEAN | 否 | `True`<br>`False` |
| `reference_assets` | 先前建立之 Seedance 虛擬庫資產（Image、Video 或 Audio）的 ID，用於作為參考。每個資產必須存在且狀態為 Active。在提示詞中，可以將資產稱為 asset1、asset 2 等；節點會將這些標記替換為如 Image 2 的標籤。 | STRING | 否 | Up 至 30 (Seedance 2.5)<br>Up 至 9 (Seedance 2.0) |

**重要約束：**

* 至少需要一個參考。對於 Seedance 2.0、2.0 Fast 和 2.0 Mini，您必須提供至少一個圖片或影片參考（透過 `reference_images`、`reference_videos`，或 `reference_assets` 中的圖片/影片條目）。Seedance 2.5 另外接受僅含音訊的參考。
* 參考數量取決於模型：Seedance 2.5 最多允許 30 個 `reference_images`、10 個 `reference_videos`、10 個 `reference_audios` 和 30 個 `reference_assets`；Seedance 2.0 模型最多允許 9 張圖片、3 個影片、3 個音訊片段和 9 個資產。總數會將直接輸入與資產參考合併計算，並在生成前進行驗證。
* 每個參考影片的長度必須至少為 1.8 秒，每個參考音訊片段的長度也必須至少為 1.8 秒。所有參考影片和所有參考音訊的總持續時間必須保持在所選模型的限制內（Seedance 2.0 模型為 15.1 秒）。
* 參考影片也必須符合所選解析度的模型像素數限制。啟用 `auto_downscale`（預設）時，過大的影片會自動調整大小；啟用 `auto_upscale` 時，過小的影片會被放大。若停用任一自動調整功能，超出對應限制的影片會引發錯誤。
* 在 Seedance 2.5 上啟用 `video_editing` 時，`duration` 和 `ratio` 輸入會被忽略；輸出將符合參考影片自身的長度與長寬比。

## 輸出
| 輸出名稱 | 描述 | 資料類型 |
|----------|------|----------|
| `video` | 生成的影片檔案。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2ReferenceNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `4429306ac40b0f04ce7176cd805b34164de5e4e2b7204b008ea076b57663c200`
