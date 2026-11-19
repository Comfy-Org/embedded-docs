# SenseNova Interleave Decode

將 SenseNova Conditioning 留下的交錯歷史記錄轉換為可用的文字、影像與思考內容。請在迴圈末端執行此節點，並停用 End Loop accumulate，以便一次收集模型在該次執行中產生的所有內容。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `clip` | 用於解碼所產生 token 的 SenseNova CLIP 模型。 | CLIP | 是 | - |
| `conditioning` | 來自 SenseNova Conditioning 的交錯條件。 | CONDITIONING | 是 | - |
| `samples` | 最後一個 KSampler 像素 latent，當迴圈因影像請求而結束時需要。 | LATENT | 否 | - |

**限制與行為：**

* `conditioning` 必須來自 `interleave` 或 `self-correction` 任務中的 SenseNova Conditioning；其他任何來源都會引發錯誤。
* 當模型正在等待影像時，將取樣器的 LATENT 輸出連接到 `samples`。
* 在執行開始時連接的參考影像會從輸出中排除；若未生成任何影像，則會跳過影像取用端。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `text` | 從交錯歷史記錄解碼出的文字，其中影像標記會以空白行取代。 | STRING |
| `images` | 模型在執行期間生成的影像。 | IMAGE |
| `thinking` | 模型的推理文字（若有產生）。 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SenseNovaInterleaveDecode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `62c7ded50c1348e2242319209729a17d543d80e4d01ddf173cf8b77e4fd0be50`
