> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan2VideoContinuationApi/zh-TW.md)

Wan 2.7 影片延續節點能生成一個新的影片片段，從輸入影片剪輯的結尾處無縫延續。它使用 Wan 2.7 模型，根據文字提示來合成延續內容，並可選擇性地引導結尾朝向特定的目標畫面。

## 輸入參數

| 參數 | 資料類型 | 必填 | 範圍 | 描述 |
| :--- | :--- | :--- | :--- | :--- |
| `model` | COMBO | 是 | `"wan2.7-i2v"` | 要使用的影片生成模型。 |
| `model.prompt` | STRING | 是 | - | 描述元素和視覺特徵的提示詞。支援英文和中文。（預設：空字串） |
| `model.negative_prompt` | STRING | 是 | - | 描述需要避免內容的負向提示詞。（預設：空字串） |
| `model.resolution` | COMBO | 是 | `"720P"`<br>`"1080P"` | 輸出影片的解析度。 |
| `model.duration` | INT | 是 | 2 到 15 | 輸出影片的總時長（單位：秒）。模型會生成延續內容來填補輸入剪輯之後的剩餘時間。（預設：5） |
| `first_clip` | VIDEO | 是 | - | 要從其結尾開始延續的輸入影片。時長：2秒至10秒。輸出影片的長寬比將由此影片決定。 |
| `last_frame` | IMAGE | 否 | - | 最終畫面影像。延續內容將向此畫面過渡。 |
| `seed` | INT | 是 | 0 到 2147483647 | 用於生成的種子值。（預設：0） |
| `prompt_extend` | BOOLEAN | 是 | - | 是否使用 AI 輔助來增強提示詞。（預設：True） |
| `watermark` | BOOLEAN | 是 | - | 是否在結果中添加 AI 生成的水印。（預設：False） |

**注意：** `first_clip` 輸入影片的時長必須在 2 到 10 秒之間。

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
| :--- | :--- | :--- |
| `output` | VIDEO | 生成的影片延續片段。 |