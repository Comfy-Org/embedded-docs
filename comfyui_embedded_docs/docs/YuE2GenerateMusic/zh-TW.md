# YuE2 生成音樂

從風格、歌詞與 ABC 記譜產生音樂 token 與聲學條件。它會傳回條件與產生的持續時間（秒），應提供給 Empty YuE2 Latent Audio 節點。若 ABC 輸入留空，則會忽略所選模式，並自動使用 off 模式。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `clip` | 用於對音樂輸入進行 token 化與編碼的 CLIP 模型。 | CLIP | 是 | - |
| `風格` | 描述音樂風格的文字。支援多行輸入與動態提示詞。 | STRING | 是 | Multiline text |
| `歌詞` | 產生音樂的歌詞。支援多行輸入與動態提示詞。 | STRING | 是 | Multiline text |
| `abc` | 連接 ABC 產生器，或提供編輯過的樂譜。留空以自動使用 off 模式。預設："" | STRING | 是 | Multiline text |
| `種子` | 產生所用的隨機種子。預設：0 | INT | 是 | 0 至 18446744073709551615 |
| `模式` | `full`：產生旋律與和弦；`melody`：僅產生旋律，建議用於翻唱。預設："full" | COMBO | 是 | "full"<br>"melody" |
| `max_duration` | 最大持續時間（秒）。長提示詞會自動縮短；產生可能提前停止。預設：360.0 | FLOAT | 是 | 0.04 至 900.0 |
| `溫度` | 產生所用的取樣溫度。預設：1.0（進階） | FLOAT | 是 | 0.0 至 5.0 |
| `top_p` | Nucleus 取樣機率閾值。預設：0.95（進階） | FLOAT | 是 | 0.01 至 1.0 |
| `top_k` | Top-k 取樣限制。預設：100（進階） | INT | 是 | 1 至 32768 |
| `repetition_penalty` | 對重複 token 施加的懲罰。預設：1.2（進階） | FLOAT | 是 | 0.01 至 10.0 |
| `cfg_scale` | 針對風格與歌詞的自迴歸引導。1.0 會停用 CFG，與 ABC 工作流程相符。使用 1.01 可符合原始 off 模式引導。預設：1.0（進階，選填） | FLOAT | 否 | 0.0 至 100.0 |

注意：若 `abc` 為空或僅包含空白，則會忽略 `mode` 選擇，並自動使用 off 模式。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `CONDITIONING` | 從音樂 token 產生的聲學條件。 | CONDITIONING |
| `seconds` | 產生的音訊持續時間（秒）。請將此值提供給 Empty YuE2 Latent Audio 節點。 | FLOAT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/YuE2GenerateMusic/zh-TW.md)

---
**Source fingerprint (SHA-256):** `5a88e185d2998c51acff7f0c76c8c35ca30b80b88cb541d97f9ab91566b5a3ed`
