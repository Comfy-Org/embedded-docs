# 載入 MoGe 模型

從檔案載入 MoGe（單目幾何）模型，並為幾何估計任務做好準備。此節點從 `geometry_estimation` 資料夾讀取模型檔案，並使用其訓練好的權重初始化 MoGe 模型。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model_name` | 要載入的 MoGe 模型檔案名稱。請從您的 ComfyUI 安裝中可用的模型檔案中選擇。 | COMBO | 是 | `geometry_estimation` 資料夾中可用的模型檔案清單 |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `MOGE_MODEL` | 已載入的 MoGe 模型實例，可用於幾何估計工作流程。 | MOGE_MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadMoGeModel/zh-TW.md)

---
**Source fingerprint (SHA-256):** `b5b55f94d3762852d5a1480c0b00d15da4e534adbeb544bf7c47da012e5a6353`
