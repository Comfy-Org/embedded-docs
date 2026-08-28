# SDPoseDrawKeypoints

SDPoseDrawKeypoints 節點接收姿勢估計資料（關鍵點），並將其作為視覺骨架繪製在空白畫布上。它允許您選擇性地繪製姿勢的不同部分，例如身體、頭部、手部、臉部和腳部，並可自訂線條寬度和點的大小。產生的影像可用於視覺化，或作為需要姿勢影像的其他節點的輸入。

## 輸入

| 參數 | 描述 | 資料型別 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `keypoints` | 要繪製的姿勢關鍵點資料。此資料通常來自姿勢偵測節點，且可能包含一或多個影格。 | POSE_KEYPOINT | 是 | - |
| `draw_body` | 控制是否繪製主要身體骨架（預設值：True）。 | BOOLEAN | 否 | - |
| `draw_hands` | 控制是否繪製手部關鍵點（預設值：True）。 | BOOLEAN | 否 | - |
| `draw_face` | 控制是否繪製臉部關鍵點（預設值：True）。 | BOOLEAN | 否 | - |
| `draw_feet` | 控制是否繪製腳部關鍵點（預設值：False）。 | BOOLEAN | 否 | - |
| `stick_width` | 用於繪製身體和頭部骨架的線條寬度（預設值：4）。 | INT | 否 | 1 至 10 |
| `face_point_size` | 用於繪製臉部關鍵點的點的大小（預設值：3）。 | INT | 否 | 1 至 10 |
| `score_threshold` | 關鍵點必須達到的最低信心分數才會被繪製。分數低於此值的關鍵點將被忽略（預設值：0.3）。 | FLOAT | 否 | 0.0 至 1.0 |
| `繪製頭部` | 控制是否繪製頭部關鍵點（鼻子、眼睛、耳朵）（預設值：True）。 | BOOLEAN | 否 | - |

**注意：** 如果 `keypoints` 輸入為空或 `None`，節點將輸出一個空白的 64x64 影像。

**注意：** `draw_body` 和 `draw_head` 獨立運作。當 `draw_head` 停用時，即使 `draw_body` 啟用，也不會繪製頭部關鍵點。當 `draw_body` 停用但 `draw_head` 啟用時，只會繪製頭部關鍵點和頸部點。如果兩者皆停用，則不會繪製任何身體或頭部關鍵點。

## 輸出

| 輸出名稱 | 描述 | 資料型別 |
| --- | --- | --- |
| `output` | 含有已繪製姿勢關鍵點的影像。影像尺寸與輸入關鍵點資料中指定的 `canvas_height` 和 `canvas_width` 相符。當輸入包含多個影格時，會傳回一批影像。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SDPoseDrawKeypoints/zh-TW.md)

---
**Source fingerprint (SHA-256):** `2b2b9530b55c56e278666bd5d139bb6a1bb503b75b948a89266b9982b5a295e4`
