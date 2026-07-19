# Tripo P1：文字轉模型

## 概述

此節點使用 Tripo P1 API 從文字描述生成 3D 模型。它針對創建低多邊形、可直接用於遊戲的網格進行了優化，具有穩定的拓撲結構，適用於即時應用程式。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `提示詞` | 您想要生成的 3D 模型的文字描述。 | STRING | 是 | 最多 1024 個字元 |
| `負面提示詞` | 您不希望出現在生成模型中的文字描述。 | STRING | 否 | 最多 255 個字元 |
| `輸出模式` | 控制輸出模型的品質和紋理設定。此參數是一個字典，包含以下鍵值：<br><br>`texture_quality`：STRING，範圍：`"standard"`<br>`pbr`：BOOLEAN，預設值：True<br>`texture`：BOOLEAN，預設值：True<br>`subdivision`：INT，預設值：0，範圍：0 到 2<br>`texture_size`：INT，預設值：2048，範圍：512 到 4096（必須為 2 的冪次方）<br>`texture_format`：STRING，範圍：`"png"`<br>`texture_clean`：BOOLEAN，預設值：False<br>`texture_seamless`：BOOLEAN，預設值：False<br><br>預設值：`{"texture_quality": "standard", "pbr": True, "texture": True, "subdivision": 0, "texture_size": 2048, "texture_format": "png", "texture_clean": False, "texture_seamless": False}` | DICT | 是 | 請見說明 |
| `圖像種子` | 用於影像生成的種子值，用於控制隨機性。預設值：42。 | INT | 否 |  |
| `面數上限` | 生成網格的最大面數。值為 -1 表示無限制。預設值：-1。 | INT | 否 |  |
| `模型種子` | 用於模型生成的種子值，用於控制隨機性。 | INT | 否 |  |
| `自動尺寸` | 若啟用，節點將自動決定最佳模型大小。預設值：False。 | BOOLEAN | 否 |  |
| `匯出 UV` | 若啟用，模型將包含用於紋理映射的 UV 座標。預設值：True。 | BOOLEAN | 否 |  |
| `壓縮幾何` | 若啟用，幾何體將被壓縮以減少檔案大小。預設值：False。 | BOOLEAN | 否 |  |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `模型檔案` | 生成的 3D 模型檔案路徑（僅為向後相容性保留）。 | STRING |
| `模型任務 ID` | 模型生成請求的唯一任務 ID。 | MODEL_TASK_ID |
| `GLB` | 以 GLB 格式生成的 3D 模型。 | FILE3DGLB |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoP1TextToModelNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `154e75209d65c823d5681b74cd12fe7b2ed37d7b94bf51cac86f343c68f85722`
