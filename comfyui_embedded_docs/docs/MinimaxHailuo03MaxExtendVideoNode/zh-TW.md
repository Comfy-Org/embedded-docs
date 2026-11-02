# MiniMax H3 Max Extend Video

此節點會以提示詞及選用的音訊參考為引導，使用新影片內容續寫一段影片。您上傳來源影片後，系統會生成續寫內容，並依設定回傳整段重新渲染的影片，或僅回傳新的影片內容。提供兩種模型：「MiniMax H3 Max」與「MiniMax H3 Max Turbo」，後者每單位價格更便宜。

## 輸入

### 通用輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 用於續寫影片的模型。兩種模型皆提供下列相同的輸入。 | DYNAMIC_COMBO | 是 | "MiniMax H3 Max"<br>"MiniMax H3 Max Turbo" |

### 模型輸入

這些輸入適用於兩種模型。

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `video` | 要延伸的影片，長度為 1.625 至 60 秒，最大 50 MB。長寬比必須介於 0.4 與 2.5 之間。 | VIDEO | 是 | 1.625 至 60 秒 |
| `prompt` | 接下來發生什麼事。請描述續寫內容，而非來源影片。以 `@Audio1`..`@Audio3` 參照參考音訊，例如 "@Audio1 for the voice"。 | STRING | 是 | 1 至 50000 個字元 |
| `reference_audios` | 可增長的插槽：最多可連接 3 段音訊片段（`audio_1`...`audio_3`）供新的影片內容使用，每段至少 2 秒，總計 14.5 秒。 | AUDIO | 否 | 0 至 3 段音訊 |
| `duration` | 要新增的新影片秒數（預設值：5）。 | INT | 是 | 1 至 15 |
| `resolution` | 輸出影片的解析度（預設值："768P"）。 | COMBO | 是 | "480P"<br>"768P"<br>"1080P"<br>"2K" |
| `aspect_ratio` | 輸出的長寬比。"auto" 會跟隨來源影片；其他值會將影片裁切為所選比例（預設值："auto"）。 | COMBO | 是 | "auto"<br>"21:9"<br>"16:9"<br>"4:3"<br>"1:1"<br>"3:4"<br>"9:16" |
| `output` | "extended" 會回傳整段影片，以所選解析度重新渲染並包含新的影片內容。"continuation" 僅回傳新的影片內容，開頭為來源影片結尾重複 1.6 秒（預設值："extended"）。 | COMBO | 是 | "extended"<br>"continuation" |
| `prompt_expansion` | 使用來源影片改寫提示詞，以維持續寫內容的一致性。關閉此選項後，相同的 seed 可得到可重現的結果（預設值：true）。 | BOOLEAN | 否 | true<br>false |
| `seed` | 隨機種子。相同請求搭配相同種子會得到相似但不保證完全相同的結果（預設值：42）。 | INT | 是 | 0 至 4294967295 |

### 參數限制

- 在 2K 解析度下，"extended" 輸出的影片總長限制為 45 秒，包含來源影片與新的影片內容。若需要更長的片段，請使用 "continuation" 或較低的解析度。
- 每段參考音訊片段至少須為 2 秒，且所有片段合計不得超過 14.5 秒。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `video` | 依 `output` 設定，回傳延伸後的影片或僅新的影片內容。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03MaxExtendVideoNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `db41a14db392fa450689c8d0d73d38b4ce9ea59ee30cfe4d6d2b0501cf0fc9a8`
