> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextGenerate/zh-TW.md)

TextGenerate 節點使用 CLIP 模型，根據使用者的提示詞來產生文字。它也可以選擇性地使用圖片、影片或音訊作為額外的上下文來引導文字生成。您可以控制輸出的長度、為支援的模型啟用思考模式，以及選擇是否使用帶有各種設定的隨機採樣，或是不經採樣直接生成文字。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `clip` | CLIP | 是 | 不適用 | 用於將提示詞進行分詞並生成文字的 CLIP 模型。 |
| `prompt` | STRING | 是 | 不適用 | 引導文字生成的文字提示詞。此欄位支援多行和動態提示詞。預設值為空字串。 |
| `image` | IMAGE | 否 | 不適用 | 可選的圖片，可與文字提示詞一起使用，以影響生成的文字。 |
| `video` | IMAGE | 否 | 不適用 | 作為圖片批次處理的影片幀。假設為 24 FPS；內部會降採樣至 1 FPS。 |
| `audio` | AUDIO | 否 | 不適用 | 可選的音訊輸入，可與文字提示詞一起使用，以影響生成的文字。 |
| `max_length` | INT | 是 | 1 至 2048 | 模型將生成的最大 token 數量。預設值為 256。 |
| `sampling_mode` | COMBO | 是 | `"on"`<br>`"off"` | 控制文字生成過程中是否使用隨機採樣。設定為 "on" 時，將啟用控制採樣的其他參數。預設值為 "on"。 |
| `thinking` | BOOLEAN | 否 | True 或 False | 如果模型支援，則以思考模式運作。預設值為 False。 |
| `use_default_template` | BOOLEAN | 否 | True 或 False | 如果模型有內建的系統提示詞/模板，則使用它。預設值為 True。這是一個進階參數。 |
| `temperature` | FLOAT | 否 | 0.01 至 2.0 | 控制輸出的隨機性。數值越低，輸出越可預測；數值越高，輸出越有創造性。此參數僅在 `sampling_mode` 為 "on" 時可用。預設值為 0.7。 |
| `top_k` | INT | 否 | 0 至 1000 | 將採樣池限制為可能性最高的前 K 個下一個 token。值為 0 時停用此過濾器。此參數僅在 `sampling_mode` 為 "on" 時可用。預設值為 64。 |
| `top_p` | FLOAT | 否 | 0.0 至 1.0 | 使用核採樣，將選擇限制在累積機率小於此值的 token 範圍內。此參數僅在 `sampling_mode` 為 "on" 時可用。預設值為 0.95。 |
| `min_p` | FLOAT | 否 | 0.0 至 1.0 | 設定 token 被納入考慮的最小機率閾值。此參數僅在 `sampling_mode` 為 "on" 時可用。預設值為 0.05。 |
| `repetition_penalty` | FLOAT | 否 | 0.0 至 5.0 | 對已經生成過的 token 進行懲罰，以減少重複。值為 1.0 時不施加懲罰。此參數僅在 `sampling_mode` 為 "on" 時可用。預設值為 1.05。 |
| `presence_penalty` | FLOAT | 否 | 0.0 至 5.0 | 根據新 token 是否已在當前文字中出現過對其進行懲罰，鼓勵模型談論新主題。此參數僅在 `sampling_mode` 為 "on" 時可用。預設值為 0.0。 |
| `seed` | INT | 否 | 0 至 18446744073709551615 | 用於初始化隨機數生成器的數字，以便在採樣模式為 "on" 時獲得可重現的結果。預設值為 0。 |

**注意：** 參數 `temperature`、`top_k`、`top_p`、`min_p`、`repetition_penalty`、`presence_penalty` 和 `seed` 僅在 `sampling_mode` 設定為 "on" 時，才會在節點介面中啟用並顯示。

## 輸出

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `generated_text` | STRING | 模型根據輸入提示詞以及可選的圖片、影片或音訊所生成的文字。 |

---
**Source fingerprint (SHA-256):** `dc6868bd7ebb63c485a4346113834f845416d7359759b2d428525398bdedf343`
