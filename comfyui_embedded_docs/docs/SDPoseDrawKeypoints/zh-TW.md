> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SDPoseDrawKeypoints/zh-TW.md)

SDPoseDrawKeypoints 節點接收姿勢估計資料（關鍵點）並將其繪製為空白畫布上的視覺化骨架。它允許您選擇性地繪製姿勢的不同部分，例如身體、手部、臉部和腳部，並可自訂線條寬度和點的大小。生成的圖像可用於視覺化，或作為其他需要姿勢圖像的節點的輸入。

## 輸入參數

| 參數 | 資料類型 | 必填 | 範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `keypoints` | POSE_KEYPOINT | 是 | - | 要繪製的姿勢關鍵點資料。此資料通常來自姿勢檢測節點。 |
| `draw_body` | BOOLEAN | 否 | - | 控制是否繪製主體骨架（預設值：True）。 |
| `draw_hands` | BOOLEAN | 否 | - | 控制是否繪製手部關鍵點（預設值：True）。 |
| `draw_face` | BOOLEAN | 否 | - | 控制是否繪製臉部關鍵點（預設值：True）。 |
| `draw_feet` | BOOLEAN | 否 | - | 控制是否繪製腳部關鍵點（預設值：False）。 |
| `stick_width` | INT | 否 | 1 至 10 | 用於繪製身體骨架的線條寬度（預設值：4）。 |
| `face_point_size` | INT | 否 | 1 至 10 | 用於繪製臉部關鍵點的點的大小（預設值：3）。 |
| `score_threshold` | FLOAT | 否 | 0.0 至 1.0 | 關鍵點必須達到的最低置信度分數才會被繪製。分數低於此值的關鍵點將被忽略（預設值：0.3）。 |

**注意：** 如果 `keypoints` 輸入為空或 `None`，節點將輸出一個空白的 64x64 圖像。

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `output` | IMAGE | 包含已繪製姿勢關鍵點的圖像。圖像尺寸與輸入關鍵點資料中指定的 `canvas_height` 和 `canvas_width` 相符。 |