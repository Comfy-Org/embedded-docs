# Creatify Boreal-H3 Reference to Video

Creatify Boreal-H3 Reference to Video 會根據參考影像、影片與音訊生成帶聲音的影片，使用 Creatify 為影片廣告後訓練的 H3 模型。在提示詞中將參考命名為 `@Image1`、`@Video1` 與 `@Audio1`，以控制各參考的貢獻。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `reference_images` | 可擴充的插槽，最多可放 9 張參考影像（`image_1` ... `image_9`），在提示詞中依連接順序以 `@Image1` ... `@Image9` 指稱。至少需要一張影像或一部影片，且參考總數最多為 12 個。 | IMAGE | 否 | 最多 9 張影像 |
| `reference_videos` | 可擴充的插槽，最多可放 3 部參考影片（`video_1` ... `video_3`），每部長度至少 1 秒。當提示詞要求延續其聲音時，會重複使用這些影片的聲音；提示詞中的新一行會取代它。參考影片總計最多計費 15 秒。 | VIDEO | 否 | 最多 3 部影片 |
| `reference_audios` | 可擴充的插槽，最多可放 3 段參考音訊片段（`audio_1` ... `audio_3`）。語音會引導聲音表現，而非字詞內容；器樂音樂則可成為配樂。 | AUDIO | 否 | 最多 3 段音訊片段 |
| `prompt` | 描述影片並指涉所連接參考的文字提示詞。必須至少包含一個非空白字元。 | STRING | 是 | 任意非空文字 |
| `resolution` | 輸出影片的解析度（預設：`"768p"`）。 | COMBO | 是 | `"768p"`<br>`"1088p"`<br>`"2k"` |
| `aspect_ratio` | 輸出影片的長寬比。`"auto"` 會跟隨第一張參考影像；若未連接影像，則跟隨第一部參考影片（預設：`"auto"`）。 | COMBO | 是 | `"auto"`<br>`"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"` |
| `duration` | 影片長度，單位為秒（預設：5）。使用 `"2k"` 時，最大值為 14 秒。 | INT | 是 | 1 至 15（步進值：1） |
| `prompt_enhancement` | Creatify 在渲染前如何改寫提示詞：`"auto"` 與 `"ads"` 會將其轉為影片廣告提示詞，並可能加入口播台詞；`"general"` 會針對其他任何影片改寫；`"none"` 則依原文渲染（預設：`"auto"`）。 | COMBO | 是 | `"auto"`<br>`"ads"`<br>`"general"`<br>`"none"` |
| `seed` | `seed` 控制此節點是否重新執行。Creatify 會自行選擇隨機性，因此只有在 `prompt_enhancement` 設為 `"none"` 時，相同輸入才會產生相同影片（預設：42）。 | INT | 是 | 0 至 2147483647 |

**限制：** 至少連接一張參考影像或一部參考影片；不接受僅有音訊。若參考標籤指向的編號超過該類型已連接的參考數量，會引發錯誤；參考總數超過 12 個時也會引發錯誤。使用 `"1088p"` 與 `"auto"` 且未連接參考影像時，長寬比會取自第一部參考影片。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `VIDEO` | 生成的帶聲音影片。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreatifyBorealH3ReferenceVideoNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `c6e60b83a8e02262fcbae7c04f4f379cf665a9e25b2fa00836047fe56d0fa064`
