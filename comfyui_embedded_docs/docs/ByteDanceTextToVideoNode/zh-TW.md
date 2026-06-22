# 字節跳動文字轉影片

ByteDance 文字轉影片節點透過 API 使用 ByteDance 模型，根據文字提示生成影片。它接收文字描述和各種影片設定作為輸入，然後建立符合指定規格的影片。該節點負責處理 API 通訊，並將生成的影片作為輸出回傳。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `模型` | 用於生成的 ByteDance 模型（預設值：`"seedance-1-0-pro-fast-251015"`）。 | STRING | 是 | `"seedance-1-5-pro-251215"`<br>`"seedance-1-0-pro-250528"`<br>`"seedance-1-0-lite-t2v-250428"`<br>`"seedance-1-0-pro-fast-251015"` |
| `提示詞` | 用於生成影片的文字提示。 | STRING | 是 | - |
| `解析度` | 輸出影片的解析度。 | STRING | 是 | `"480p"`<br>`"720p"`<br>`"1080p"` |
| `長寬比` | 輸出影片的長寬比。 | STRING | 是 | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"` |
| `持續時間` | 輸出影片的長度，以秒為單位（預設值：5）。 | INT | 是 | 3 到 12 |
| `種子值` | 用於生成的種子值（預設值：0）。 | INT | 否 | 0 到 2147483647 |
| `固定攝影機` | 指定是否固定攝影機。平台會在您的提示中附加固定攝影機的指令，但不保證實際效果（預設值：False）。 | BOOLEAN | 否 | - |
| `浮水印` | 是否在影片中添加「AI 生成」浮水印（預設值：False）。 | BOOLEAN | 否 | - |
| `generate_audio` | 此參數僅對 `seedance-1-5-pro-251215` 模型有效，其他模型將忽略此參數（預設值：False）。 | BOOLEAN | 否 | - |

**參數限制：**

- `prompt` 參數在去除空白字元後必須至少包含 1 個字元。
- `prompt` 參數不能包含以下文字參數："resolution"、"ratio"、"duration"、"seed"、"camerafixed"、"watermark"。
- `duration` 參數限制在 3 到 12 秒之間。對於 `seedance-1-5-pro-251215` 模型，支援的最小長度為 4 秒。
- `seed` 參數接受 0 到 2,147,483,647 之間的值。
- `generate_audio` 參數僅在 `model` 設定為 `seedance-1-5-pro-251215` 時有效；對於所有其他模型，此參數將被忽略。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `output` | 生成的影片檔案 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceTextToVideoNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `44ea3e40b99b337340cc39be1c5b6c903680591f1de49b1f2e82f398979355c5`
