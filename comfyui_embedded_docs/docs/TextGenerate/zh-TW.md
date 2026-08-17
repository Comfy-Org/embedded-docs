# TextGenerate

TextGenerate 節點使用 CLIP 模型，根據使用者的提示詞產生文字。它也可以選擇性地使用影像、影片或音訊作為額外上下文，以引導文字產生。您可以控制輸出的長度、為支援的模型啟用思考模式，並選擇要使用各種設定的隨機取樣，或是在沒有取樣的情況下產生文字。

## 輸入

### 通用輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `clip` | 用於將提示詞轉換為 token 並產生文字的 CLIP 模型。 | CLIP | 是 | N/A |
| `prompt` | 引導產生的文字提示詞。此欄位支援多行及動態提示詞。預設值為空字串。 | STRING | 是 | N/A |
| `image` | 可與文字提示詞一同使用以影響產生文字的可選影像。 | IMAGE | 否 | N/A |
| `video` | 以影像批次表示的影片幀。假定為 24 FPS；內部會降採樣至 1 FPS。 | IMAGE | 否 | N/A |
| `audio` | 可與文字提示詞一同使用以影響產生文字的可選音訊輸入。 | AUDIO | 否 | N/A |
| `max_length` | 模型將產生的最大 token 數。預設值為 512。 | INT | 是 | 1 to 32768 |
| `sampling_mode` | 控制文字產生期間是否使用隨機取樣。設為 "on" 時，會啟用控制取樣的額外參數。預設值為 "on"。 | DYNAMIC_COMBO | 是 | "on"<br>"off" |
| `thinking` | 如果模型支援，則以思考模式運作。預設值為 False。 | BOOLEAN | 否 | True or False |
| `use_default_template` | 若模型具有內建的系統提示詞/範本，則使用之。預設值為 True。這是進階參數。 | BOOLEAN | 否 | True or False |

### "on" 輸入

當 `sampling_mode` 設為 "on" 時，可使用下列取樣參數：

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `temperature` | 控制輸出的隨機性。數值越低，輸出越可預測；數值越高，輸出越有創意。預設值為 0.7。 | FLOAT | 否 | 0.01 to 2.0 |
| `top_k` | 將取樣池限制為前 K 個最可能的下一個 token。值為 0 時停用此篩選器。預設值為 64。 | INT | 否 | 0 to 1000 |
| `top_p` | 使用核取樣（nucleus sampling），將選擇限制為累積機率小於此值的 token。預設值為 0.95。 | FLOAT | 否 | 0.0 to 1.0 |
| `min_p` | 設定 token 被考慮時所需的最低機率門檻。預設值為 0.05。 | FLOAT | 否 | 0.0 to 1.0 |
| `repetition_penalty` | 對已產生的 token 施以懲罰，以減少重複。值為 1.0 時不施以懲罰。預設值為 1.05。 | FLOAT | 否 | 0.0 to 5.0 |
| `presence_penalty` | 根據新 token 到目前為止是否已在文字中出現來施以懲罰，鼓勵模型討論新主題。預設值為 0.0。 | FLOAT | 否 | 0.0 to 5.0 |
| `seed` | 用於初始化亂數產生器的數字，可在取樣為 "on" 時重現結果。預設值為 0。 | INT | 否 | 0 to 18446744073709551615 |

### "off" 輸入

當 `sampling_mode` 設為 "off" 時，沒有額外的取樣參數可用，節點會在沒有隨機取樣的情況下產生文字。

**注意：** 參數 `temperature`、`top_k`、`top_p`、`min_p`、`repetition_penalty`、`presence_penalty` 和 `seed` 僅在 `sampling_mode` 設為 "on" 時，才會在節點介面中啟用並顯示。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `generated_text` | 模型根據輸入的提示詞以及可選的影像、影片或音訊所產生的文字。 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextGenerate/zh-TW.md)

---
**Source fingerprint (SHA-256):** `6274a2db7c9a963304daf6df494b2b20879155e918d73429fd2ce7f3b5b9da02`
