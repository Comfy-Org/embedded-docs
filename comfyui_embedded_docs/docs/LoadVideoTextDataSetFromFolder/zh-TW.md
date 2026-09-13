# 載入影片-文字（資料夾）

此節點會從 ComfyUI 輸入目錄中的資料夾載入影片檔案及其對應的文字標註，並以兩個清單回傳：影片與標註。影片項目是惰性引用，因此只有在 downstream 節點需要時才會解碼影格。支援的格式為 MP4、AVI、MOV、WEBM、MKV 和 FLV，並且也支援帶有重複次數前綴的巢狀資料夾（例如 `5_classname/`，如 kohya-ss/sd-scripts 等工具所使用）。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `資料夾` | 包含影片檔案與 .txt 標註的資料夾。 | COMBO | 是 | 動態列出 ComfyUI 輸入目錄內的所有子資料夾 |

所選資料夾必須是 ComfyUI 輸入目錄的子資料夾；若資料夾名稱解析後位於該目錄之外，會引發錯誤。若所選資料夾中沒有任何支援的影片副檔名檔案（MP4、AVI、MOV、WEBM、MKV、FLV），此節點會引發錯誤。對於名稱以數字後接底線開頭的巢狀資料夾（例如 `5_classname`），該資料夾內的每部影片會依照該前綴指定的次數納入資料集。每部影片的標註會從相同主檔名的 `.txt` 檔案讀取；若沒有相符的 `.txt` 檔案，則標註為空字串。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `videos` | 惰性影片引用；只有在 downstream 需要時才會解碼影格。資料夾中找到的每個影片檔案各一項。 | VIDEO (list) |
| `texts` | 文字標註清單。每部影片一個標註；若影片沒有相符的 `.txt` 檔案，其標註為空字串。 | STRING (list) |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadVideoTextDataSetFromFolder/zh-TW.md)

---
**Source fingerprint (SHA-256):** `21ed21bc3189e96be5c7f0415c65e8749d6591cf19bddf4350a3b0af48b92841`
