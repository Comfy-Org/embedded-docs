# 載入 MediaPipe Face Landmarker

此節點載入 MediaPipe Face Landmarker v2 模型，可偵測影像中的人臉與臉部特徵點（例如眼睛、鼻子與嘴巴）。載入的模型包含兩種偵測變體（short 與 full），以及共享的網格資料、混合變形（blendshapes）與用於臉部分析的標準幾何結構。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model_name` | 來自 `models/detection/` 的人臉偵測模型。 | COMBO | 是 | `models/detection/` 目錄中可用的模型清單 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `FACE_DETECTION_MODEL` | 已載入的 MediaPipe Face Landmarker 模型物件，包含兩種偵測變體（short/full）、共享網格與混合變形資料、標準幾何結構、臉部拓撲連接集，以及用於 GPU 管理的模型修補器（patchers）。 | FACE_DETECTION_MODEL |

**注意：** 此輸出是一個複雜物件，可供其他節點用於人臉偵測與特徵點擷取任務。它包含兩種偵測變體：「short」用於近距離偵測，「full」用於全範圍偵測。

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadMediaPipeFaceLandmarker/zh-TW.md)

---
**Source fingerprint (SHA-256):** `33dda845b572ccffc1bd4b64fb9c338ce4313783b092fe311d89741a211f18c9`
