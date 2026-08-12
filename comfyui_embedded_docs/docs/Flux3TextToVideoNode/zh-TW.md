# Flux3TextToVideoNode

使用 FLUX 3 根據文字提示生成帶有同步音訊的影片。此節點會將您的提示傳送至 FLUX 3 服務，等待生成完成，然後傳回完成的影片剪輯。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 您想要的內容，以通俗語言表達；提示在生成前會被解讀和擴充。請分別描述環境音、音樂和語音，以實現分層音訊。（預設值：""） | STRING | 是 | 多行文字 |
| `aspect_ratio` | 輸出寬高比。`auto` 會從提示和輸入中選擇一個。（預設值："auto"） | STRING | 是 | 多個可用選項，包括 `"auto"` |
| `duration` | 影片長度（秒）。`auto` 會讓長度配合內容。（預設值："auto"） | STRING | 是 | 多個可用選項，包括 `"auto"` |
| `resolution` | 輸出解析度。（預設值："720p"） | STRING | 是 | `"720p"`<br>`"1080p"` |
| `generate_audio` | 生成同步音訊（環境音、語音、效果）。關閉會產生沒有音軌的影片。（預設值：True） | BOOLEAN | 是 | True<br>False |
| `safety_tolerance` | 審核容忍度，0 最嚴格。傳送圖片或影片的請求上限為 2，無論您在此設定什麼。（預設值：2） | INT | 是 | 0 到 4 |
| `seed` | 決定節點是否重新執行的種子；FLUX 3 自己選擇種子，因此無論此值為何，實際結果都是非確定性的。（預設值：42） | INT | 是 | 0 到 4294967295 |

注意：`seed` 輸入在 UI 中包含「生成後控制」（Control After Generate）控件。顯示的價格基於 `resolution` 和 `duration`：HD (720p) 每秒收費 $0.2431，FHD (1080p) 每秒收費 $0.4147。選擇固定長度時，會顯示影片剪輯的估計總成本；當 `duration` 為 "auto" 時，會顯示每秒費率。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `video` | 生成的影片剪輯，當啟用 `generate_audio` 時包含同步音訊。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux3TextToVideoNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `35f5e5b1c6dd737afab78f53700997a458781d38149cb64fc60d86a86858b2e6`
