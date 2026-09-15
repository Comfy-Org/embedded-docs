# 載入 MediaPipe Face Landmarker

此節點會載入 MediaPipe Face Landmarker v2 模型，該模型可偵測影像中的人臉與臉部特徵點（例如眼睛、鼻子和嘴巴）。載入的模型會將兩種偵測變體（短距離與全範圍）與共用網格資料、混合形狀（blendshapes），以及用於臉部分析的標準幾何資料打包在一起。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model_name` | 來自 models/detection/ 的人臉偵測模型。 | COMBO | 是 | 在 `models/detection/` 目錄中找到的可用模型檔案名稱清單 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `FACE_DETECTION_MODEL` | 已載入的 FaceLandmarker 模型物件，包含兩種偵測變體（short/full）、臉部拓撲的連接集、標準資料，以及用於 GPU 管理的模型修補器。 | FACE_DETECTION_MODEL |

**注意：** 輸出是一個複雜物件，可供其他節點用於人臉偵測與特徵點擷取任務。它包含兩種偵測變體：「short」用於近距離偵測，「full」用於全範圍偵測。

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadMediaPipeFaceLandmarker/zh-TW.md)

---
**Source fingerprint (SHA-256):** `33dda845b572ccffc1bd4b64fb9c338ce4313783b092fe311d89741a211f18c9`
