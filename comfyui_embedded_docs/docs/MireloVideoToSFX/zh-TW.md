# Mirelo Video to SFX

使用 Mirelo SFX 為影片生成跟隨畫面內容的音效。上傳影片片段後，模型會跟隨畫面中的動作，回傳一組音效混音，以及一條另行分離出來、從原聲帶中抽出對白的語音軌。可用於為無聲或部分無聲的影片片段加入擬音、環境音與衝擊音效。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 要使用的模型。選取模型後會顯示其專屬參數：`video`、`audio`、`prompt`、`negative_prompt`、`preserve_speech` 與 `seed`。 | DYNAMIC_COMBO | 是 | `"sfx-2.0"` |
| `video` | 要為其生成音效的影片。音效會針對整段影片生成，長度為 1 至 600 秒。 | VIDEO | 是 | 1 至 600 秒 |
| `audio` | 用於 `preserve_speech` 與 `speech` 輸出的對白軌，取代影片自身的原聲帶。若保持未連接，則使用影片內嵌的聲音。 | AUDIO | 否 | - |
| `prompt` | 描述希望音效聽起來如何。可留空（預設：空白），因為模型會自行描述影片內容，且不一定會遵循提示詞。上限 2000 個字元。 | STRING | 是 | 最多 2000 個字元 |
| `negative_prompt` | 要避免的聲音，以簡短的逗號分隔清單表示。可留空（預設：空白）。上限 1000 個字元。 | STRING | 是 | 最多 1000 個字元 |
| `preserve_speech` | 將對白混合在生成的音效之下。關閉時僅回傳音效。（預設：True） | BOOLEAN | 是 | false<br>true |
| `seed` | 請求使用的隨機種子。結果並非確定性，因此相同的種子不會重現同一段影片。（預設：42） | INT | 是 | 0 至 4294967295 |

當影片片段短於 1 秒或長於 600 秒時，節點會停止並回報錯誤。若有連接 `audio` 軌，則會設定 `preserve_speech` 所保留、以及 `speech` 輸出所分離的對白；若未連接，對白則來自影片自身的原聲帶。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `audio` | 該影片片段的音效混音；當 `preserve_speech` 開啟時，對白會混合於其下。 | AUDIO |
| `speech` | 從原聲帶中分離出來的對白。若未偵測到語音，或語音分離未回傳任何結果，則為靜音，取樣率與 `audio` 相同。 | AUDIO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MireloVideoToSFX/zh-TW.md)

---
**Source fingerprint (SHA-256):** `fa09525e6c9b10412823e358652220850fbc7109d81cc207d31ffa8921956495`
