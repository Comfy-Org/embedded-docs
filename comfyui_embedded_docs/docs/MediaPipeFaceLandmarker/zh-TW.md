> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MediaPipeFaceLandmarker/zh-TW.md)

## 概述

使用 MediaPipe 的 BlazeFace 和 FaceMesh 模型偵測影像中的人臉，並識別每張臉上的 468 個面部特徵點（關鍵點）。同時計算 ARKit-52 混合變形係數以進行臉部表情分析。此節點可批次處理多張影像，並為每個偵測到的人臉輸出特徵點資料和邊界框。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `face_detection_model` | FACE_DETECTION_MODEL | 是 | | 用於特徵點偵測的 MediaPipe 人臉偵測模型。 |
| `image` | IMAGE | 是 | | 要偵測人臉的輸入影像或影像批次。 |
| `detector_variant` | COMBO | 是 | `"short"`<br>`"full"`<br>`"both"` | 人臉偵測器範圍。`"short"` 針對近距離人臉（距離相機約 2 公尺內）進行最佳化；`"full"` 涵蓋較遠/較小的人臉（距離約 5 公尺內），但速度較慢。`"both"` 同時執行兩種偵測器，並保留每幀中偵測到較多人臉的結果（偵測成本約為兩倍）。預設值：`"short"`。 |
| `num_faces` | INT | 是 | 0 至 16 | 每幀返回的最大人臉數量。0 表示無上限（返回所有偵測到的人臉）。預設值：1。 |
| `min_confidence` | FLOAT | 否 | 0.00 至 1.00 | BlazeFace 分數閾值。較低的值有助於捕捉較小或被遮擋的人臉。預設值：0.5。 |
| `missing_frame_fallback` | COMBO | 否 | `"empty"`<br>`"previous"`<br>`"interpolate"` | 批次中偵測失敗時的每幀處理行為。`"empty"` 使該幀無人臉資料。`"previous"` 複製最近一次成功的偵測結果。`"interpolate"` 在成功偵測的幀之間對特徵點/邊界框/混合變形進行線性插值。多人臉：透過貪婪邊界框中心最近鄰演算法跨幀配對人臉。預設值：`"empty"`。 |

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `bboxes` | FACE_LANDMARKS | 結構化輸出，包含每幀的人臉偵測結果，包括 468 個面部特徵點、ARKit-52 混合變形係數、轉換矩陣以及用於網格視覺化的連線集合。 |
| `bboxes` | BOUNDING_BOX | 每個偵測到的人臉的邊界框列表，包含座標 (x, y, width, height)、標籤 "face" 和信心分數。每個輸入幀對應一個列表。 |

---
**Source fingerprint (SHA-256):** `f60ed6201288a59d65d62cc98c12f227a353870c36decea8da81a063cfdf2bba`
