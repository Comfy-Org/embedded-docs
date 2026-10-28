# VEED Dubbing

VEED Dubbing 會使用 VEED 將影片中的語音翻譯成另一種語言，複製每位說話者的聲音，並讓其嘴型與翻譯後的語音同步。系統會上傳影片片段、輪詢 VEED 工作狀態，然後回傳配音後的影片，其幀率為 25 fps，長度與新的音軌相同。可用於將已完成的影片片段在地化，無需重新拍攝或重新錄製語音。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | 配音模型。`"standard"` 較便宜且回傳單聲道音訊，支援拉丁美洲西班牙語與巴西葡萄牙語；`"pro"` 增加地區口音與立體聲音訊。選擇模型後會顯示 `video`、`target_language`、`source_language` 與 `seed`。 | DYNAMIC_COMBO | 是 | `"standard"`<br>`"pro"` |

### standard 輸入

當 `model` 設為 `"standard"` 時，會顯示這些輸入。

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `video` | 包含清晰可見的臉部並帶有語音的影片，最長 599 秒。輸出長度與其音軌相同，並以 25 fps 播放。 | VIDEO | 是 | 最長 599 秒 |
| `target_language` | 要配音成的語言，為 85 種語言之一。（預設：`"English"`） | COMBO | 是 | 85 種語言 |
| `source_language` | 影片中說的語言，或 `"auto"` 表示自動偵測。（預設：`"auto"`） | COMBO | 是 | `"auto"`<br>85 種語言 |
| `seed` | `seed` 控制節點是否應重新執行；無論 seed 為何，結果都是非確定性的。（預設：42） | INT | 是 | 0 至 2147483647 |

### pro 輸入

當 `model` 設為 `"pro"` 時，會顯示這些輸入。

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `video` | 包含清晰可見的臉部並帶有語音的影片，最長 599 秒。輸出長度與其音軌相同，並以 25 fps 播放。 | VIDEO | 是 | 最長 599 秒 |
| `target_language` | 要配音成的語言或地區口音：87 種語言加上 14 種口音，例如 `"English (UK)"`、`"Spanish (Mexico)"` 與 `"Portuguese (Brazil)"`。（預設：`"English (US)"`） | COMBO | 是 | 101 個選項 |
| `source_language` | 影片中說的語言，或 `"auto"` 表示自動偵測。（預設：`"auto"`） | COMBO | 是 | `"auto"`<br>91 種語言 |
| `seed` | `seed` 控制節點是否應重新執行；無論 seed 為何，結果都是非確定性的。（預設：42） | INT | 是 | 0 至 2147483647 |

當影片沒有音軌、影片片段長度超過 599 秒，或 VEED 工作失敗時，節點會停止並顯示錯誤。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `VIDEO` | 配音後的影片：原始畫面加上翻譯後的語音，以及與其匹配的嘴型動作。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VeedDubbingNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `fb818ca510e20bccffde61dca98c457984b8a110976e56f2a513f6c7f4d80c80`
