# Flux 3 影片續接

此節點會使用 FLUX 3 延續現有影片片段：新片段會從您提供影片的最後幾個畫面繼續。它會上傳您的來源片段，將提示詞與設定傳送至生成服務，並在完成後回傳生成的續接影片。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `video` | 要延續的片段。 | VIDEO | 是 | 單一影片片段 |
| `prompt` | 續接內容應顯示什麼；`prompt` 會在生成前被解讀並擴展。（預設：""） | STRING | 是 | 非空文字（至少 1 個字元） |
| `aspect_ratio` | 輸出長寬比。'auto' 會根據提示詞與輸入選擇一個。（預設："auto"） | COMBO | 是 | "auto"（預設）<br>多個預定義選項 |
| `duration` | 片段長度（秒）。'auto' 會讓長度配合內容。（預設："auto"） | COMBO | 是 | "auto"（預設）<br>以秒為單位的數值 |
| `resolution` | 輸出解析度。（預設："720p"） | COMBO | 是 | "720p"（預設）<br>"1080p"<br>其他預定義選項 |
| `generate_audio` | 生成同步音訊（環境音、語音、效果）。關閉時會產生沒有音軌的影片。（預設：true） | BOOLEAN | 是 | true<br>false |
| `safety_tolerance` | 內容審核容許度，0 最嚴格。傳送圖片或影片的請求，無論此處設定為何，上限均為 2。（進階參數，預設：2） | INT | 是 | 0 - 4（影片請求的有效上限：2） |
| `seed` | 用來決定節點是否應重新執行的種子；FLUX 3 會自行選擇種子，因此無論此值為何，實際結果都是非確定性的。（預設：42） | INT | 是 | 0 - 4294967295 (0xFFFFFFFF) |

### 注意事項

- `prompt` 必須至少包含一個字元，否則生成會失敗。雖然此欄位預設為空字串，但執行節點時必須提供非空的提示詞。
- `safety_tolerance` 接受 0 到 4 之間的任何值，但由於此節點會將影片傳送到 API，因此無論選取的值為何，有效容許度上限均為 2。
- 當 `duration` 設為數字時，會轉換為整數秒數。特殊值 "auto" 會讓服務將長度配合內容。
- `aspect_ratio`、`duration` 和 `resolution` 的確切選項清單由節點內部定義。解析度選項至少包含 "720p"（預設）和 "1080p"。價格會根據所選的 `resolution` 和 `duration` 計算；"1080p" 以每秒 $0.7579 計費，其他解析度則以每秒 $0.5863 計費。
- `seed` 只控制節點是否重新執行；它不會被傳送到生成服務。
- 驗證與節點識別欄位（`auth_token_comfy_org`、`api_key_comfy_org`、`unique_id`）為隱藏欄位，並由平台自動處理。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `video` | 由 FLUX 3 產生的續接片段，會從來源影片結尾處繼續。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux3VideoContinuationNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `129ad0eb62c368854cebb010cc886aecac4caab00f9111143b883d028d7c30d9`
