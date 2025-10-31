> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImage/zh-TW.md)

**節點功能：** `Save Image` 節點主要用於將圖片儲存至 ComfyUI 的 **output** 資料夾。若您僅想在處理過程中預覽圖片而不需儲存，可使用 `Preview Image` 節點。
預設儲存位置：`ComfyUI/output/`

## 輸入參數

| 參數名稱 | 資料類型 | 描述 |
|-----------|-------------|-------------|
| `影像` | `IMAGE` | 要儲存的圖片。此參數至關重要，因為它直接包含將被處理並儲存至磁碟的圖片資料。 |
| `檔名前綴` | STRING   | 儲存至 `ComfyUI/output/` 資料夾的圖片檔案名稱前綴。預設為 `ComfyUI`，但您可以自訂此名稱。 |

## 右鍵選單選項

圖片生成完成後，在對應選單上點擊右鍵可提供以下節點專用選項與功能：

| 選項名稱 | 功能 |
|-------------|----------|
| `Save Image` | 將圖片儲存至本機 |
| `Copy Image` | 將圖片複製到剪貼簿 |
| `Open Image` | 在新瀏覽器分頁中開啟圖片 |

儲存的圖片通常為 PNG 格式，並包含所有圖片生成資料。若您想使用對應的工作流程進行重新生成，只需將對應圖片載入至 ComfyUI 即可載入工作流程。