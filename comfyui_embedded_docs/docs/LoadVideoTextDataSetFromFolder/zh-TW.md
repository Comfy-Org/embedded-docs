# 載入影片-文字（資料夾）

此節點從 ComfyUI 輸入目錄內的指定子資料夾加載一組影片檔案及其對應的文字說明。它回傳兩個列表：延遲影片參考（僅在下游節點需要時才解碼影格）及其關聯的說明。節點支援常見影片格式，如 MP4、AVI、MOV、WEBM、MKV 與 FLV，並可處理巢狀資料夾結構，以及 kohya‑ss/sd‑scripts 等工具使用的重複計數前綴（例如 `5_classname/`）。

## 輸入
| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `資料夾` | 包含影片檔案與 `.txt` 說明檔案的子資料夾。從 ComfyUI 輸入目錄中可用的子資料夾中選取。 | STRING | 是 | Combo：ComfyUI 輸入資料夾內所有子目錄的動態列表 |

## 輸出
| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `影片` | 已加載影片檔案的延遲參考。僅在連接到處理它們的下游節點時才解碼影格。每個元素對應輸入資料夾中的一個影片。 | VIDEO (list) |
| `文字` | 文字說明列表，每個影片對應一個說明。若影片沒有匹配的 `.txt` 檔案，其說明為空字串。 | STRING (list) |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadVideoTextDataSetFromFolder/zh-TW.md)

---
**Source fingerprint (SHA-256):** `91236fcb1e42b8de1a1100b0aecaad49bd49c159d7d8f502032cd7f5b2b54845`
