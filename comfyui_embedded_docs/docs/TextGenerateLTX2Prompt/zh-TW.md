# TextGenerateLTX2Prompt

The TextGenerateLTX2Prompt 節點是文字生成節點的專門版本。它接收使用者的文字提示，並在將其傳送至語言模型進行增強或補全之前，自動以 LTX2 專用的系統指令進行格式化。此節點可在純文字或影像參考模式下運作，並會根據所連接的 CLIP 模型自動調整其格式化方式：對於 Gemma 4 模型使用 LTX 2.4 提示格式，對於 Gemma 3 模型則使用 LTX 2.0 格式。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `clip` | 用於文字編碼的 CLIP 模型。此模型決定提示格式：Gemma 4 模型使用 LTX 2.4 格式，Gemma 3 模型使用 LTX 2.0 格式。 | CLIP | 是 |  |
| `prompt` | 使用者提供的原始文字輸入，將被增強或補全。 | STRING | 是 |  |
| `max_length` | 語言模型允許生成的最大 token 數量。 | INT | 是 |  |
| `sampling_mode` | 在文字生成期間用於選擇下一個 token 的取樣策略。 | COMBO | 是 | `"greedy"`<br>`"top_k"`<br>`"top_p"`<br>`"temperature"` |
| `image` | 可選的輸入影像。提供時，節點會使用包含影像上下文的不同系統提示，用於影像轉影片生成。 | IMAGE | 否 |  |
| `thinking` | 啟用時，模型會在最終答案之前輸出其推理過程。推理區塊會從最終結果中移除。 | BOOLEAN | 否 |  |
| `use_default_template` | 啟用時，節點將使用預設的聊天模板進行格式化。 | BOOLEAN | 否 |  |
| `video` | 可選的影片輸入，可作為生成時的額外上下文。 | VIDEO | 否 |  |
| `audio` | 可選的音訊輸入，可作為生成時的額外上下文。 | AUDIO | 否 |  |

**備註：** 節點的行為會根據 `image` 輸入是否存在而改變。若提供了影像，提示會格式化為影像轉影片任務，使用根據影像內容擴充提示的系統提示。若未提供影像，則格式化為文字轉影片任務，使用將提示擴充為詳細影片生成描述的系統提示。

所連接的 `clip` 模型也會影響格式化方式：當 CLIP tokenizer 是 Gemma 4 模型時，節點使用 LTX 2.4 聊天格式和系統提示；否則使用 Gemma 3 / LTX 2.0 聊天格式。生成之後，任何推理區塊（例如 `<think>...</think>`）都會從輸出中移除，若產生的文字為空，則會回傳原始的 `prompt`。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `output` | 語言模型生成的增強或補全文字字串，已移除任何推理內容。若模型未產生文字，則回傳原始提示。 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextGenerateLTX2Prompt/zh-TW.md)

---
**Source fingerprint (SHA-256):** `8f524ea60a247217dde8a1edaf7a689e253ae05acc9eb52ad47b91e879dba1df`
