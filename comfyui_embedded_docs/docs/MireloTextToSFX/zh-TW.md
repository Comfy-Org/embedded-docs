# Mirelo Text to SFX

使用 Mirelo SFX 從文字描述產生音效。請描述聲音本身，而不是聲音所屬的畫面；此節點會傳回單一音軌，長度為所要求的長度。可用於擬音、環境音、衝擊音與短音樂紋理，無需拍攝或上傳影片。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 要使用的模型。選取模型後會顯示其專屬參數：`prompt`、`negative_prompt`、`duration` 與 `seed`。 | DYNAMIC_COMBO | 是 | `"sfx-2.0"` |
| `prompt` | 描述聲音，而不是畫面。1 到 2000 個字元。 | STRING | 是 | 1 至 2000 個字元 |
| `negative_prompt` | 要避免的聲音，以簡短的逗號分隔清單表示。可留空（預設：空白）。最多 1000 個字元。 | STRING | 是 | 最多 1000 個字元 |
| `duration` | 聲音長度，以秒為單位。（預設：5.0） | FLOAT | 是 | 0.1 至 600.0 （步進值：0.1） |
| `seed` | 用於請求的隨機種子。結果不具確定性，因此相同的種子不會重複產生相同的聲音。（預設：42） | INT | 是 | 0 至 4294967295 |

當 `prompt` 為空或超過 2000 個字元，以及 `negative_prompt` 超過 1000 個字元時，節點會停止並回報錯誤。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `AUDIO` | 產生的音效，長度與 `duration` 相同。 | AUDIO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MireloTextToSFX/zh-TW.md)

---
**Source fingerprint (SHA-256):** `b09a9562cea636702acd9fc50feb38b272a558f8b8509da21f5fada2abd9fd48`
