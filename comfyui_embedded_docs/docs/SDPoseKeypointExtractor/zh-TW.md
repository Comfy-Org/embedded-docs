# SDPose關鍵點提取器

SDPose關鍵點提取器節點使用SDPose模型從輸入圖像中檢測人體姿勢關鍵點。它可以處理完整圖像或由邊界框定義的特定區域，並以OpenPose格式輸出檢測到的關鍵點，其中包括每個人的座標以及每個關鍵點的置信度分數。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 用於關鍵點檢測的SDPose模型。必須是具有`heatmap_head`屬性的模型，特別是來自SDPose儲存庫的模型。 | MODEL | 是 | - |
| `vae` | 用於將輸入圖像編碼為潛在空間以進行處理的VAE模型。 | VAE | 是 | - |
| `image` | 要從中提取姿勢關鍵點的輸入圖像或圖像批次。 | IMAGE | 是 | - |
| `batch_size` | 在全圖像模式下運行時（即未提供`bboxes`時）一次處理的圖像數量。這可以加快處理速度。（預設值：16） | INT | 否 | 1 至 10000 |
| `bboxes` | 可選的邊界框，用於更準確的檢測。多人檢測時需要。如果提供，節點將從每個指定區域提取關鍵點。 | BOUNDINGBOX | 否 | - |

**參數限制：**
*   `model`輸入必須是特定的SDPose模型。如果提供的模型沒有`heatmap_head`屬性，節點將引發錯誤。
*   節點根據`bboxes`輸入以兩種不同的模式運行：
    1.  **邊界框模式：** 當提供`bboxes`時，它會單獨處理每個指定區域。這是在單個圖像中檢測多個人時所需的模式。
    2.  **全圖像模式：** 當未提供`bboxes`時，它會將整個圖像作為批次處理。`batch_size`參數僅在此模式下適用。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `keypoints` | OpenPose框架格式的關鍵點（canvas_width, canvas_height, people）。輸出包含檢測到的人員，每個人員都有一個關鍵點座標陣列（x, y）及其對應的置信度分數。 | POSE_KEYPOINT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SDPoseKeypointExtractor/zh-TW.md)

---
**Source fingerprint (SHA-256):** `7903b51c9137aa08bb8843362740fcf93cea9c09d142bd1db3b5eee945c853e4`
