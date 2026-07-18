## 概述

此節點使用 Tripo P1 API 將單張 2D 影像轉換為 3D 模型。它專為生成低多邊形、可直接用於遊戲的網格而最佳化。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `圖片` | 要轉換為 3D 模型的輸入影像。 | IMAGE | 是 | - |
| `輸出模式` | 一個字典，指定輸出模式和品質設定。此參數控制生成的模型類型及其紋理品質。可用選項由 `_build_p1_output_mode` 輔助函數定義，包括 `texture_quality`（例如 "standard"、"high"、"ultra"）和 `image_alignment` 的設定。 | DICT | 是 | 請參閱說明 |
| `啟用圖片自動修正` | 預處理輸入影像以獲得更好的生成品質。（預設值：False） | BOOLEAN | 否 | True<br>False |
| `面數上限` | 限制生成網格中的面數。值為 -1 表示無限制。（預設值：-1） | INT | 否 | - |
| `模型種子` | 用於可重複模型生成的種子值。若未提供，則使用隨機種子。（預設值：None） | INT | 否 | - |
| `自動尺寸` | 自動決定生成模型的最佳尺寸。（預設值：False） | BOOLEAN | 否 | True<br>False |
| `匯出 UV` | 匯出模型的 UV 座標。（預設值：True） | BOOLEAN | 否 | True<br>False |
| `壓縮幾何` | 壓縮幾何資料以減少檔案大小。（預設值：False） | BOOLEAN | 否 | True<br>False |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `模型檔案` | 生成的 3D 模型檔案路徑。此輸出僅為向後相容性而提供。 | STRING |
| `模型任務 ID` | 模型生成請求的唯一任務 ID。 | MODEL_TASK_ID |
| `GLB` | 以 GLB 格式生成的 3D 模型。 | FILE3DGLB |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoP1ImageToModelNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `2ac611603dd6eb88700a8105c19f97a8c4eefe5f4efb23d8854ccc27af590626`
