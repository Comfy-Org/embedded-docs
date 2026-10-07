# Vidu Q4 Reference-to-Video Generation

使用參考圖片、可選的參考音訊與提示詞，並搭配 Vidu Q4 模型生成影片。這是 Vidu Q4 生成節點的參考圖轉影片變體。

選取 `model` 會顯示該模型專屬的參數。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | 用於影片生成的模型。選取模型後會顯示其專屬參數：`reference_images`、`reference_audios`、`prompt`、`aspect_ratio`、`resolution`、`duration`、`audio` 和 `seed`。 | DYNAMIC_COMBO | 是 | `"Vidu Q4 Preview"` |
| `reference_images` | 可增長插槽：連接一或多張參考圖片（`image_1`、`image_2`、...）用於生成的影片；批次中的每張圖片都會計入總數。請在提示詞中依序引用它們：image 1、image 2，依此類推。 | IMAGE | 是 | 最多 15 張圖片 |
| `reference_audios` | 可增長插槽：連接可選的語音參考（`audio_1`、`audio_2`、`audio_3`），每段 3 到 12 秒。只會使用聲音，不會使用字詞：在提示詞中撰寫對話，並依序指派聲音，例如 `image 1 says "Hello!" in the voice from audio 1`。需要啟用 `audio`。 | AUDIO | 否 | 最多 3 個片段 |
| `prompt` | 用於影片生成的文字描述，最多 5000 個字元。需要用它來描述你想使用的參考內容。 | STRING | 是 | 任意文字 |
| `aspect_ratio` | 輸出影片的長寬比。 | COMBO | 是 | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"3:4"`<br>`"4:3"` |
| `resolution` | 輸出影片的解析度（預設：`"720p"`）。 | COMBO | 是 | `"540p"`<br>`"720p"`<br>`"1080p"`<br>`"2K"`<br>`"4K"` |
| `duration` | 輸出影片的長度，以秒為單位（預設：5）。 | INT | 是 | 3 至 16 |
| `audio` | 啟用時，輸出包含聲音的影片，包括對話與音效（預設：True）。 | BOOLEAN | 是 | `True`<br>`False` |
| `seed` | `seed` 控制節點是否應重新執行；無論 `seed` 為何，結果都是非確定性的。此參數具有「生成後控制」功能（預設：42）。 | INT | 是 | 1 至 2147483647 |

**注意：** 總共最多可使用 15 張參考圖片，且會計入批次中的每張圖片。每張圖片必須至少為 128x128 像素，且長寬比介於 1:5 與 5:1 之間。參考音訊需要啟用 `audio`，否則會引發錯誤。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `VIDEO` | 生成的影片檔案。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu4ReferenceVideoNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `f37ceec93a6140d69332415b8fd748d55e6a608177430975b4b42ab33e593489`
