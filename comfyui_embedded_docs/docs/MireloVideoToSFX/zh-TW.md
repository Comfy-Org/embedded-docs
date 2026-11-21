# Mirelo 影片轉音效

使用 Mirelo SFX 產生跟隨影片的音效。上傳片段後，模型會跟隨螢幕上的動作，回傳一份音效混音，以及一條獨立的語音分軌，其中包含從聲軌抽出的對話。可用於為無聲或部分無聲的片段加入擬音、環境音與衝擊音效。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 要使用的模型。選取模型後會顯示其專屬參數：`video`、`audio`、`prompt`、`negative_prompt`、`preserve_speech`、`seed` 與 `auto_downscale`。 | DYNAMIC_COMBO | 是 | `"sfx-2.0"` |
| `video` | 要為其產生音效的影片。會為整段片段產生音效，長度為 1 至 600 秒。 | VIDEO | 是 | 1 至 600 秒 |
| `audio` | 用於 `preserve_speech` 與 `speech` 輸出的對話音軌，取代影片本身的聲軌。若保持未連接，則使用影片內嵌的聲音。 | AUDIO | 否 | - |
| `prompt` | 音效應該是什麼樣子。可留空（預設：空），因為模型會自行描述影片，且不一定總是遵循提示詞。最多 2000 個字元。 | STRING | 是 | 最多 2000 個字元 |
| `negative_prompt` | 要避免的聲音，以簡短的逗號分隔清單表示。可留空（預設：空）。最多 1000 個字元。 | STRING | 是 | 最多 1000 個字元 |
| `preserve_speech` | 將對話混入產生的音效之下。關閉時僅回傳音效。（預設：True） | BOOLEAN | 是 | false<br>true |
| `seed` | 請求的種子值。結果不具確定性，因此相同的種子不會重現相同的片段。（預設：42） | INT | 是 | 0 至 4294967295 |
| `auto_downscale` | 若片段較短邊高於 2160 像素，在上傳前將其縮小，並保持長寬比；較小的片段不會變動（預設：True）。 | BOOLEAN | 否 | `True`<br>`False` |

當片段短於 1 秒或長於 600 秒時，節點會停止並顯示錯誤。連接的 `audio` 音軌會設定 `preserve_speech` 保留、且由 `speech` 輸出分離的對話；若未連接，則對話來自影片本身的聲軌。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `audio` | 片段的音效混音；當 `preserve_speech` 開啟時，對話會混入其下。 | AUDIO |
| `speech` | 從聲軌分離出的對話。若未找到語音或語音分離未回傳任何內容，則為靜音，且取樣率與 `audio` 相同。 | AUDIO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MireloVideoToSFX/zh-TW.md)

---
**Source fingerprint (SHA-256):** `a6bd749a902d5ca2e91863fd6c4df57cdeba7fd9505026053b72b29d588587fa`
