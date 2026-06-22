# 載入 MediaPipe Face Landmarker

## 概述

此節點載入 MediaPipe Face Landmarker v2 模型，可偵測影像中的人臉及臉部特徵點（如眼睛、鼻子和嘴巴）。它包含兩種偵測變體（短距離與全距離），以及共享的網格資料、混合形狀和用於臉部分析的標準幾何結構。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `model_name` | 來自 `models/detection/` 目錄的人臉偵測模型。 | STRING | 是 | `models/detection/` 目錄中可用的模型清單 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `FACE_DETECTION_MODEL` | 一個已載入的 FaceLandmarker 模型物件，包含兩種偵測變體（短距離/全距離）、臉部拓撲連接集、標準資料以及用於 GPU 管理的模型修補器。 | FACE_DETECTION_MODEL |

**注意：** 輸出是一個複雜物件，可供其他節點用於人臉偵測和特徵點提取任務。它包含兩種偵測變體：「short」用於近距離偵測，「full」用於全距離偵測。

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadMediaPipeFaceLandmarker/zh-TW.md)

---
**Source fingerprint (SHA-256):** `b30bf4d04aa06a227f3661c0e1346d3dab3ea1e25d6627fce5b6480198203c26`
