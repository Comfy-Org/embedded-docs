# Generate Text

Generate Text 節點使用 CLIP 模型根據提示詞產生文字。與較舊的單一附加節點不同，它接受可增長的影像、影片和音訊檔案堆疊作為額外上下文，因此您可以在單一節點中送入整組參考資料。您可以控制輸出長度、是否使用取樣，以及是否套用模型自身的聊天範本和思考模式。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `clip` | 用於將提示詞分詞並產生文字的 CLIP 模型。 | CLIP | 是 | - |
| `prompt` | 引導產生的提示詞。支援多行和動態提示詞（預設：空字串）。 | STRING | 是 | - |
| `images` | 最多 50 張影像的可增長群組，`image1` 至 `image50`，用作模型的視覺上下文。 | AUTOGROW | 否 | 0 至 50 張影像 |
| `videos` | 最多 100 個影片輸入的可增長群組，`video1` 至 `video100`。每部影片是假設為 24 FPS 的影格批次，並在內部子取樣至 模型的影格率。 | AUTOGROW | 否 | 0 至 100 部影片 |
| `audios` | 最多 100 個音訊輸入的可增長群組，`audio1` 至 `audio100`，用作模型的音訊上下文。 | AUTOGROW | 否 | 0 至 100 個音訊檔案 |
| `max_length` | 要產生的最大 token 數（預設：512）。 | INT | 是 | 1 至 32768 |
| `sampling_mode` | `on` 會對輸出取樣並顯示下方的取樣參數。`off` 則以貪婪方式產生，不進行隨機取樣。 | DYNAMIC_COMBO | 是 | `"on"`<br>`"off"` |
| `thinking` | 若模型支援，則以思考模式運作（預設：False）。 | BOOLEAN | 否 | True 或 False |
| `use_default_template` | 若模型具有內建的系統提示詞或聊天範本，則使用之（預設：True）。進階參數。 | BOOLEAN | 否 | True 或 False |
| `mtp` | 使用檢查點的多 token 預測頭進行推測解碼。在沒有 MTP 權重時無效。`"auto"` 會根據觀察到的 token 匹配和執行成本調整草稿深度與廣度，`"2"` 到 `"5"` 固定草稿深度，而 `tree` 模式同時固定廣度與深度。取樣輸出仍保持正確分佈，但相同種子下與非 MTP 輸出不同（預設：`"auto"`）。 | COMBO | 否 | `"auto"`<br>`"off"`<br>`"2"`<br>`"3"`<br>`"4"`<br>`"5"`<br>`"tree2s1"`<br>`"tree2s2"`<br>`"tree3s1"`<br>`"tree4s1m8"` |
| `system_prompt` | 取代模型聊天範本中的系統提示詞。未使用預設範本時忽略。請連接 STRING 輸入而非在節點中輸入（預設：空）。 | STRING | 否 | - |

### 取樣參數（當 `sampling_mode` 為 `"on"` 時）

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `temperature` | 控制輸出的隨機性。較低的值使輸出更可預測，較高的值使其更具創造力（預設：0.7）。 | FLOAT | 是 | 0.01 至 2.0 |
| `top_k` | 將取樣池限制在 K 個最可能的下一個 token。值為 0 會停用篩選（預設：64）。 | INT | 是 | 0 至 1000 |
| `top_p` | 核心取樣：保留累積機率達到此值的最小最可能 token 集合（預設：0.95）。 | FLOAT | 是 | 0.0 至 1.0 |
| `min_p` | token 必須達到的最低機率才能留在池中（預設：0.05）。 | FLOAT | 是 | 0.0 至 1.0 |
| `repetition_penalty` | 懲罰已產生的 token 以減少重複。值為 1.0 時不施加懲罰（預設：1.05）。 | FLOAT | 是 | 0.0 至 5.0 |
| `presence_penalty` | 根據新 token 是否已在目前文字中出現來懲罰它們，鼓勵模型轉向新主題（預設：0.0）。 | FLOAT | 是 | 0.0 至 5.0 |
| `seed` | 用於初始化隨機數產生器以獲得可重現結果的數字（預設：0）。 | INT | 是 | 0 至 18446744073709551615 |

**注意：** 上述取樣參數僅在 `sampling_mode` 為 `"on"` 時存在。當為 `"off"` 時，節點不進行隨機取樣產生文字，且這些參數會隱藏。

**注意：** 當模型的輸出以 `<think>` 開啟推理區塊時，節點會將其拆分：`generated_text` 承載答案，`thinking` 承載移除開頭標籤的推理內容。否則，`generated_text` 承載模型產生的所有內容，而 `thinking` 為空。被 `max_length` 截斷的推理內容會保留在 `generated_text` 中。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `generated_text` | 模型產生的文字，任何推理區塊會分離到 `thinking` 輸出中。 | STRING |
| `thinking` | 模型產生的推理區塊，已移除開頭的 `<think>` 標籤。當模型未產生推理區塊時為空。 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextGenerateV2/zh-TW.md)

---
**Source fingerprint (SHA-256):** `b61210726faa495a342a5eaaebe64f800ec1d2af4e2fc1321d8c3d7c594bd9ca`
