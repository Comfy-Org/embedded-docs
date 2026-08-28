# 載入 MediaPipe Face Landmarker

載入臉部偵測模型（MediaPipe）

## 概述

此節點載入 MediaPipe Face Landmarker v2 模型，該模型可偵測影像中的臉部與臉部特徵點（如眼睛、鼻子和嘴巴）。它包含兩種偵測變體（短距離與全距離），以及共享的網格資料、混合形狀（blendshapes）和用於臉部分析的標準幾何資料。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model_name` | 來自 `models/detection/` 的臉部偵測模型。 | COMBO | 是 | `models/detection/` 目錄中可用模型的列表 |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `FACE_DETECTION_MODEL` | 一個已載入的 FaceLandmarker 模型物件，包含兩種偵測變體（short/full）、臉部拓撲的連線集合、標準資料，以及用於 GPU 管理的模型修補程式。 | FACE_DETECTION_MODEL |

**注意：** 此輸出是一個複雜物件，可供其他節點用於臉部偵測和特徵點提取任務。它包含兩種偵測變體：「short」用於近距離偵測，「full」用於全距離偵測。

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadMediaPipeFaceLandmarker/zh-TW.md)

---
**Source fingerprint (SHA-256):** `33dda845b572ccffc1bd4b64fb9c338ce4313783b092fe311d89741a211f18c9`
