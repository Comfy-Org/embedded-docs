# 載入影片（資料夾）

從 ComfyUI 輸入目錄內的所選資料夾載入所有支援的影片檔案，並將其作為影片參考清單回傳。此節點回傳延遲影片參考，因此僅在其他節點實際需要時才解碼影格。支援的格式：MP4、AVI、MOV、WEBM、MKV 和 FLV。

## 輸入

| 參數 | 說明 | 資料型態 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `folder` | 包含影片檔案的資料夾。從 ComfyUI 輸入目錄內可用的子資料夾中選擇。 | COMBO | Yes | ComfyUI 輸入目錄中所有可用的子資料夾 |

**注意：** 所選資料夾必須至少包含一個受支援的影片檔案。支援的副檔名為 MP4、AVI、MOV、WEBM、MKV 和 FLV。如果找不到受支援的影片檔案，節點會引發錯誤。資料夾必須解析為 ComfyUI 輸入目錄內的位置；嘗試逸出該目錄的資料夾名稱（例如使用「..」）將被拒絕並產生錯誤。

## 輸出

| 輸出名稱 | 說明 | 資料型態 |
|-------------|-------------|-----------|
| `videos` | 延遲影片參考清單，對應所選資料夾中的每個影片檔案。僅當輸出被另一個節點使用時，才會解碼影格。 | VIDEO (list) |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadVideoDataSetFromFolder/zh-TW.md)

---
**Source fingerprint (SHA-256):** `6a7e6115872bb994fa554bb9de84bcd419106485403a3d2db654cbdd6c72bbe5`
