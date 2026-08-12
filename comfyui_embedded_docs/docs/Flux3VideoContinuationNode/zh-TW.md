# Flux3VideoContinuationNode

此節點使用 FLUX 3 延續現有的影片片段，因此新片段會從您提供的影片的最後幾幀繼續。它會上傳您的來源片段，將提示詞和設定傳送至生成服務，並在準備就緒後傳回產生的延續影片。

## 輸入

| 參數 | 描述 | 資料型別 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `video` | 要延續的影片片段。 | VIDEO | 是 | Single video clip |
| `prompt` | 延續片段應顯示的內容；提示詞會在生成前進行解譯與擴充。（預設值：""） | STRING | 是 | Non-empty text (minimum 1 character) |
| `aspect_ratio` | 輸出縱橫比。'auto' 會從提示詞和輸入中挑選一個。（預設值："auto"） | STRING | 是 | Multiple predefined options (default: "auto") |
| `duration` | 片段長度（秒）。'auto' 會根據內容調整長度。（預設值："auto"） | STRING | 是 | "auto" (default)<br>Numeric values in seconds |
| `resolution` | 輸出解析度。（預設值："720p"） | STRING | 是 | Multiple predefined options (default: "720p") |
| `generate_audio` | 生成同步音訊（環境音、語音、效果）。關閉會產生沒有音軌的影片。（預設值：true） | BOOLEAN | 是 | true<br>false |
| `safety_tolerance` | 審核容忍度，0 最嚴格。無論您在此設定什麼值，傳送圖片或影片的請求上限為 2。（進階參數，預設值：2） | INT | 是 | 0 - 4 (effective maximum: 2 for video requests) |
| `seed` | 用於決定節點是否重新執行的種子；FLUX 3 會選擇自己的種子，因此無論此值為何，實際結果都是非確定性的。（進階參數，預設值：42） | INT | 是 | 0 - 4294967295 (0xFFFFFFFF) |

### 注意事項

- `prompt` 必須至少包含一個字元，否則生成會失敗。雖然該欄位預設為空字串，但執行節點需要非空的提示詞。
- `safety_tolerance` 接受 0 到 4 的任何值，但由於此節點會傳送影片至 API，無論選擇哪個值，有效容忍度上限皆為 2。
- 當 `duration` 設定為數字時，會轉換為整數秒數。特殊值 "auto" 可讓服務根據內容調整長度。
- `aspect_ratio`、`duration` 和 `resolution` 的確切選項清單由節點內部定義。解析度選項至少包括 "720p"（預設）和 "1080p"，後者使用不同的計價費率。
- 驗證和節點識別欄位（`auth_token_comfy_org`、`api_key_comfy_org`、`unique_id`）會隱藏並由平台自動處理。

## 輸出

| 輸出名 | 描述 | 資料型別 |
|-------------|-------------|-----------|
| `video` | FLUX 3 產生的延續影片片段，從來源影片的結尾繼續。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux3VideoContinuationNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `4b3a3df86b870edd696d10d352c7123b9c6c60ce0b57910529fca60615efa9f9`
