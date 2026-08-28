# Flux 3 影片續接

此節點使用 FLUX 3 延續現有的影片片段：新的片段會從您提供的影片最後幾幀繼續。它會上傳您的來源片段，將提示詞與設定傳送至生成服務，並在準備就緒時回傳產生的續接影片。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `video` | 要續接的片段。 | VIDEO | 是 | 單一影片片段 |
| `prompt` | 續接片段應顯示的內容；提示詞在生成前會被解讀與擴充。（預設值：""） | STRING | 是 | 非空文字（最少 1 個字元） |
| `aspect_ratio` | 輸出長寬比。'auto' 會從提示詞與輸入中挑選一個。（預設值："auto"） | COMBO | 是 | "auto"（預設）<br>多個預先定義的選項 |
| `duration` | 片段長度（秒）。'auto' 會根據內容調整長度。（預設值："auto"） | COMBO | 是 | "auto"（預設）<br>以秒為單位的數值 |
| `resolution` | 輸出解析度。（預設值："720p"） | COMBO | 是 | "720p"（預設）<br>"1080p"<br>其他預先定義的選項 |
| `generate_audio` | 生成同步音訊（環境音、語音、特效）。關閉時產生的影片不含音訊軌。（預設值：true） | BOOLEAN | 是 | true<br>false |
| `safety_tolerance` | 審核容忍度，0 為最嚴格。無論此處設定為何，傳送影像或影片的要求上限為 2。（進階參數，預設值：2） | INT | 是 | 0 - 4（有效上限：影片要求為 2） |
| `seed` | 決定節點是否重新執行的種子；FLUX 3 會自行選擇種子，因此無論此值為何，實際結果皆非確定性。（進階參數，預設值：42） | INT | 是 | 0 - 4294967295 (0xFFFFFFFF) |

### 注意事項

- `prompt` 必須包含至少一個字元，否則生成將失敗。雖然欄位預設為空字串，但執行節點仍需非空的提示詞。
- `safety_tolerance` 接受 0 到 4 之間的任何值，但由於此節點會傳送影片至 API，因此無論選取何值，有效容忍度皆以 2 為上限。
- 當 `duration` 設定為數字時，會轉換為整數秒數。'auto' 這個特殊值可讓服務根據內容調整長度。
- `aspect_ratio`、`duration` 與 `resolution` 的完整選項清單由節點內部定義。解析度選項至少包含 "720p"（預設）與 "1080p"。價格依據所選的 `resolution` 與 `duration` 計算；"1080p" 每秒收費 0.7579 美元，其他解析度每秒收費 0.5863 美元。
- 驗證與節點識別欄位（`auth_token_comfy_org`、`api_key_comfy_org`、`unique_id`）為隱藏狀態，並由平台自動處理。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `video` | 由 FLUX 3 產生的續接片段，會從來源影片的結尾繼續延續。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux3VideoContinuationNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `129ad0eb62c368854cebb010cc886aecac4caab00f9111143b883d028d7c30d9`
