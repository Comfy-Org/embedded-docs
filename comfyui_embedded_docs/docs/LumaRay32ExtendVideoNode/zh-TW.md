# Luma Ray 3.2 延伸影片

Luma Ray 3.2 Extend Video 會延續先前的 Luma Ray 3.2 影片生成，透過在原始片段之後（forward）或之前（backward）建立新的 5 秒片段。連接較早的 Luma Ray 3.2 節點的 `generation_id` 輸出，即可將該片段用作擴展的起始影格（forward）或結束影格（backward）。擴展片段長度一律為 5 秒。

## 輸入

### 通用輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `source_generation_id` | 要擴展之先前 Ray 3.2 影片的 Generation ID。連接另一個 Luma Ray 3.2 節點的 `generation_id` 輸出。預設值：""（空）。此值為必填，且不得為空。 | STRING | 是 | – |
| `direction` | Forward 會接續在先前的片段之後；backward 會前置在它之前。Forward 會將來源片段用作起始影格；backward 會將其用作結束影格。選取 "Forward (continue after)" 會新增 `loop` 選項。 | DYNAMIC_COMBO | 是 | "Forward (continue after)"<br>"Backward (lead-in before)" |
| `prompt` | 新內容的文字提示。預設值：""（空）。長度必須介於 1 到 6000 個字元之間。 | STRING | 是 | 1 至 6000 characters |
| `resolution` | 擴展影片片段的輸出解析度。預設值："720p"。 | COMBO | 是 | "540p"<br>"720p"<br>"1080p" |
| `seed` | 決定節點是否應重新執行的種子；無論種子為何，結果皆不具確定性。預設值：0。 | INT | 是 | 0 至 0xFFFFFFFFFFFFFFFF (18446744073709551615) |

### Forward (continue after) 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `loop` | 將擴展影片無縫循環（僅限 forward 擴展）。預設值：False。 | BOOLEAN | 否 | True<br>False |

### Backward (lead-in before) 輸入

此方向不會新增任何額外參數。

**注意：** 擴展片段一律為 5 秒。`loop` 參數僅在 `direction` 為 "Forward (continue after)" 時可用；使用 "Backward (lead-in before)" 時，無法使用 `loop` 選項。`prompt` 長度必須介於 1 到 6000 個字元之間。`source_generation_id` 為必填，且必須從先前的 Luma Ray 3.2 節點之 `generation_id` 輸出連接。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-----------|-----------|
| `VIDEO` | 產生的 5 秒擴展影片片段。 | VIDEO |
| `generation_id` | 此生成的唯一識別碼，可連接到另一個 Luma Ray 3.2 Extend Video 節點以進行進一步擴展。 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaRay32ExtendVideoNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `a67ca53d4bcb9f3fd82bc0482b579f5f7fe4bf866f8d83cb922e1082ad320057`
