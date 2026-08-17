# SDPoseDrawKeypoints

SDPoseDrawKeypoints 節點接收姿態估計資料（關鍵點），並將它們繪製為空白畫布上的視覺骨架。它允許您選擇性地繪製姿態的不同部分，例如身體、頭部、手部、臉部和腳部，並可自訂線條寬度和點大小。產生的影像可用於視覺化，或作為其他需要姿態影像的節點的輸入。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `keypoints` | 要繪製的姿態關鍵點資料。此資料通常來自姿態偵測節點。 | POSE_KEYPOINT | 是 | - |
| `draw_body` | 控制是否繪製主要身體骨架（預設值：True）。 | BOOLEAN | 否 | - |
| `draw_hands` | 控制是否繪製手部關鍵點（預設值：True）。 | BOOLEAN | 否 | - |
| `draw_face` | 控制是否繪製臉部關鍵點（預設值：True）。 | BOOLEAN | 否 | - |
| `draw_feet` | 控制是否繪製腳部關鍵點（預設值：False）。 | BOOLEAN | 否 | - |
| `stick_width` | 用於繪製身體骨架的線條寬度（預設值：4）。 | INT | 否 | 1 到 10 |
| `face_point_size` | 用於繪製臉部關鍵點的點大小（預設值：3）。 | INT | 否 | 1 到 10 |
| `score_threshold` | 關鍵點必須達到的最低信心分數才會被繪製。分數低於此值的關鍵點將被忽略（預設值：0.3）。 | FLOAT | 否 | 0.0 到 1.0 |
| `draw_head` | 控制是否繪製頭部關鍵點（鼻子、眼睛、耳朵）和頭部連接（預設值：True）。 | BOOLEAN | 否 | - |

**注意：** 如果 `keypoints` 輸入為空或 `None`，此節點將輸出一個空白的 64x64 影像。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `output` | 一個包含繪製姿態關鍵點的影像。影像尺寸與輸入關鍵點資料中指定的 `canvas_height` 和 `canvas_width` 相符。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SDPoseDrawKeypoints/zh-TW.md)

---
**Source fingerprint (SHA-256):** `2b2b9530b55c56e278666bd5d139bb6a1bb503b75b948a89266b9982b5a295e4`
