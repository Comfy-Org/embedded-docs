# 載入 MoGe 模型

從檔案載入 MoGe（單眼幾何，Monocular Geometry）模型，並為其做好幾何估計任務的使用準備。此節點會從 `geometry_estimation` 資料夾讀取所選的模型檔案，並以其儲存的權重初始化 MoGe 模型。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model_name` | 要載入的 MoGe 模型檔案名稱。請從 ComfyUI 安裝目錄中 `geometry_estimation` 資料夾內可用的模型檔案中選擇。 | COMBO | 是 | `geometry_estimation` 資料夾中可用模型檔案的清單 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `MOGE_MODEL` | 已載入的 MoGe 模型實例，可直接用於幾何估計工作流程。 | MOGE_MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadMoGeModel/zh-TW.md)

---
**Source fingerprint (SHA-256):** `b5b55f94d3762852d5a1480c0b00d15da4e534adbeb544bf7c47da012e5a6353`
