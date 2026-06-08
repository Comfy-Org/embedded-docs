SDPoseFaceBBoxes 節點處理姿態關鍵點資料，以偵測並生成人臉周圍的邊界框。它分析畫面中每個人的 2D 臉部關鍵點，根據這些點計算邊界框，並可調整框的大小與形狀。生成的邊界框格式與 SDPose 工作流程中的其他節點（如 SDPoseKeypointExtractor）相容。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `keypoints` | 包含每幀畫面中偵測到的人物及其身體/臉部關鍵點資訊的姿態關鍵點資料。 | POSE_KEYPOINT | 是 | - |
| `scale` | 每個偵測到的人臉周圍邊界框面積的倍數。數值越大，生成的框越大。（預設值：1.5） | FLOAT | 否 | 1.0 - 10.0 |
| `force_square` | 擴展較短的邊界框軸，使裁切區域始終為正方形。（預設值：True） | BOOLEAN | 否 | - |

**注意：** `keypoints` 輸入必須採用 SDPoseKeypointExtractor 等節點生成的特定格式，其中包含 `canvas_height`、`canvas_width` 以及每個人物的 `face_keypoints_2d` 資料。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `bboxes` | 每幀畫面的人臉邊界框列表。每個邊界框由其左上角座標（`x`、`y`）、`width`（寬度）和 `height`（高度）定義。此輸出與 SDPoseKeypointExtractor 節點的 `bboxes` 輸入相容。 | BOUNDINGBOX |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SDPoseFaceBBoxes/zh-TW.md)

---
**Source fingerprint (SHA-256):** `bffbcddb882f6743a6cace6a4884fa5a257b746897c79ba9260c15260fab874e`
