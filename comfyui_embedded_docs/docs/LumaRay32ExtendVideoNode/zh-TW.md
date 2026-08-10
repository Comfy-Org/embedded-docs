# LumaRay32ExtendVideoNode

Luma Ray 3.2 Extend Video 透過建立新的 5 秒片段來延續先前的 Luma Ray 3.2 影片生成，該片段可位於原始片段之後（正向）或之前（反向）。連接較早 Luma Ray 3.2 節點的 `generation_id` 輸出，將該片段用作擴展的起始影格（正向）或結束影格（反向）。

## ## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `source_generation_id` | 待擴展的先前 Ray 3.2 影片的生成 ID。連接另一個 Luma Ray 3.2 節點的 `generation_id` 輸出。此值為必填，不能為空。 | STRING | 是 | - |
| `direction` | 正向表示在先前片段之後繼續；反向表示在先前片段之前添加。選擇"正向（之後繼續）"還會新增 `loop` 選項。 | COMBO | 是 | "Forward (continue after)"<br>"Backward (lead-in before)" |
| `loop` | 使擴展後的影片無縫循環（僅限正向擴展）。僅當 `direction` 為"正向（之後繼續）"時可用。預設值：False。 | BOOLEAN | 否 | True<br>False |
| `prompt` | 描述要生成的新內容的文字提示。長度必須介於 1 到 6000 個字元之間。 | STRING | 是 | - |
| `resolution` | 擴展影片片段的輸出解析度。預設值："720p"。 | COMBO | 是 | "540p"<br>"720p"<br>"1080p" |
| `seed` | 用於可重現生成結果的隨機種子。 | INT | 是 | - |

**注意：** `loop` 參數僅在 `direction` 設定為「向前（在之後繼續）」時可用。使用「向後（在之前引導）」時，循環選項不可用。`prompt` 必須介於 1 到 6000 個字元之間。

## ## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `VIDEO` | 生成的 5 秒擴展影片片段。 | VIDEO |
| `generation_id` | 此生成的唯一識別碼，可連接到另一個 Luma Ray 3.2 擴展影片節點以進行進一步擴展。 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaRay32ExtendVideoNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `a67ca53d4bcb9f3fd82bc0482b579f5f7fe4bf866f8d83cb922e1082ad320057`
