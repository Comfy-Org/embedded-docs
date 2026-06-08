## ## 概述

從檔案載入 MoGe（單眼幾何）模型，並將其準備好用於幾何估計任務。此節點會從 `geometry_estimation` 資料夾讀取模型檔案，並以訓練好的權重初始化 MoGe 模型。

## ## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `model_name` | 要載入的 MoGe 模型檔案名稱。從您的 ComfyUI 安裝中可用的模型檔案中選擇。 | STRING | 是 | `geometry_estimation` 資料夾中可用的模型檔案列表 |

## ## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `MOGE_MODEL` | 已載入的 MoGe 模型實例，準備好用於幾何估計工作流程。 | MOGE_MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadMoGeModel/zh-TW.md)

---
**Source fingerprint (SHA-256):** `4707002565181ca17936ecf87ea8059630c97c44c17facfecd04053d9581b7d1`
