# Luma Ray 3.2 延伸影片

Luma Ray 3.2 Extend Video 可延續先前的 Luma Ray 3.2 影片生成，建立一個新的 5 秒片段，可接續在原始片段之後（前向）或之前（後向）。連接先前 Luma Ray 3.2 節點的 `generation_id` 輸出，即可將該片段用作擴展的起始幀（前向）或結束幀（後向）。

## 輸入

### 通用輸入

| 參數 | 描述 | 資料型別 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `direction` | 前向會在先前的片段之後繼續；後向則會附加在其之前。前向使用來源片段作為起始幀；後向則將其作為結束幀。選擇「Forward (continue after)」會新增 `loop` 選項。 | DYNAMIC_COMBO | 是 | "Forward (continue after)"<br>"Backward (lead-in before)" |
| `source_generation_id` | 要擴展的先前的 Ray 3.2 影片的生成 ID。連接另一個 Luma Ray 3.2 節點的 `generation_id` 輸出。此值為必填，且不得為空。 | STRING | 是 | – |
| `prompt` | 新內容的文字提示。必須介於 1 到 6000 個字元之間。 | STRING | 是 | 1 到 6000 個字元 |
| `resolution` | 擴展影片片段的輸出解析度。預設值："720p"。 | COMBO | 是 | "540p"<br>"720p"<br>"1080p" |
| `seed` | 用於決定節點是否重新執行的種子；無論種子為何，結果都是非確定性的。預設值：0。 | INT | 是 | 0 到 0xFFFFFFFFFFFFFFFF |

### 前向（接續）輸入

| 參數 | 描述 | 資料型別 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `loop` | 無縫循環擴展的影片（僅限前向擴展）。預設值：False。 | BOOLEAN | 否 | True<br>False |

### 後向（導入之前）輸入

此方向不會新增額外參數。

**注意：** 擴展片段一律為 5 秒。`loop` 參數僅在 `direction` 為「Forward (continue after)」時可用；使用「Backward (lead-in before)」時，`loop` 選項不可用。`prompt` 必須介於 1 到 6000 個字元之間。`source_generation_id` 為必填項，且必須連接自先前 Luma Ray 3.2 節點的 `generation_id` 輸出。

## 輸出

| 輸出名 | 描述 | 資料型別 |
|-------------|-------------|-----------|
| `VIDEO` | 生成的 5 秒擴展影片片段。 | VIDEO |
| `generation_id` | 此世代的唯一識別碼，可連接到另一個 Luma Ray 3.2 Extend Video 節點以進行進一步擴展。 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaRay32ExtendVideoNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `a67ca53d4bcb9f3fd82bc0482b579f5f7fe4bf866f8d83cb922e1082ad320057`
