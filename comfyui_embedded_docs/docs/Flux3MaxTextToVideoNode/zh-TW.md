# FLUX 3 Max Text to Video

FLUX 3 Max Text to Video 可根據文字提示生成具有同步音訊的影片。提示會在渲染前由 FLUX 3 Max 解讀並擴展，節點會等待渲染完成，並返回完成的片段。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 片段應呈現的內容，以自然語言描述。若要分層音訊，請分別描述環境音、音樂與語音（預設：空白）。 | STRING | 是 | 多行文字 |
| `aspect_ratio` | 輸出長寬比。文字提示下，`"auto"` 為 16:9（預設：`"auto"`）。 | COMBO | 是 | `"auto"`<br>`"21:9"`<br>`"2:1"`<br>`"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"` |
| `duration` | 片段長度，以秒為單位（預設：`"5"`）。 | COMBO | 是 | `"5"`<br>`"6"`<br>`"7"`<br>`"8"`<br>`"9"`<br>`"10"`<br>`"11"`<br>`"12"`<br>`"13"`<br>`"14"`<br>`"15"`<br>`"16"`<br>`"17"`<br>`"18"`<br>`"19"`<br>`"20"` |
| `resolution` | 輸出解析度（預設：`"720p"`）。 | COMBO | 是 | `"720p"`<br>`"1080p"` |
| `reasoning_level` | 模型在生成前對提示進行推理與擴展的程度。`"high"` 耗時較長；價格相同（預設：`"high"`）。 | COMBO | 是 | `"low"`<br>`"high"` |
| `generate_audio` | 生成同步音訊。關閉時會產生沒有音軌的影片（預設：true）。 | BOOLEAN | 是 | `true`<br>`false` |
| `seed` | 控制節點是否重新執行的種子。無論此值為何，結果皆不具確定性（預設：42）。 | INT | 是 | 0 到 2147483646 |

注意：`prompt` 必須至少包含一個字元。顯示的價格取決於 `resolution` 與 `duration`：在 2026 年 11 月 7 日之前，720p 每秒收費 $0.060775，1080p 每秒收費 $0.103675；該日期之後，每秒分別為 $0.2431 與 $0.4147。UI 中會顯示該片段預估總成本。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `video` | 生成的影片片段；啟用 `generate_audio` 時包含同步音訊。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux3MaxTextToVideoNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `6dcb11e7aa7f1592169ede449c4092740db43e635501205eba02a066f03a967f`
