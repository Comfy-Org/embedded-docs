> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SDPoseFaceBBoxes/zh-TW.md)

SDPoseFaceBBoxes 節點處理姿勢關鍵點資料，以偵測並生成人臉周圍的邊界框。它會分析畫面中每個人的 2D 臉部關鍵點，根據這些點計算邊界框，並可調整框的大小和形狀。產生的邊界框格式與 SDPose 工作流程中的其他節點（例如 SDPoseKeypointExtractor）相容。

## 輸入參數

| 參數 | 資料類型 | 必填 | 範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `keypoints` | POSE_KEYPOINT | 是 | - | 包含每幀偵測到的人員及其身體/臉部特徵點資訊的姿勢關鍵點資料。 |
| `scale` | FLOAT | 否 | 1.0 - 10.0 | 每個偵測到的人臉周圍邊界框面積的倍數。數值越大，框的範圍越大。(預設值: 1.5) |
| `force_square` | BOOLEAN | 否 | - | 擴展較短的邊界框軸線，使裁切區域始終為正方形。(預設值: True) |

**注意：** `keypoints` 輸入必須是 SDPoseKeypointExtractor 等節點產生的特定格式，包含 `canvas_height`、`canvas_width` 以及每個人的 `face_keypoints_2d` 資料。

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `bboxes` | BOUNDINGBOX | 每幀的人臉邊界框列表。每個邊界框由其左上角座標 (`x`, `y`)、`width` 和 `height` 定義。此輸出與 SDPoseKeypointExtractor 節點的 `bboxes` 輸入相容。 |