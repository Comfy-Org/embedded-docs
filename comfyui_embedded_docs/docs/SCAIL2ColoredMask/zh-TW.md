# SCAIL2ColoredMask

此節點將 SAM3 追蹤資料渲染為彩色遮罩，供 WanSCAILToVideo 節點使用。它處理來自驅動姿態影片及可選參考圖像的追蹤資料，為兩個輸出中每個被追蹤的人物分配一致的顏色。

## ## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `驅動追蹤資料` | 驅動姿態影片的 SAM3 追蹤資料。將被渲染為 pose_video_mask 輸出。 | SAM3_TRACK_DATA | 是 | - |
| `參考追蹤資料` | 參考圖像的 SAM3 追蹤資料。 | SAM3_TRACK_DATA | 否 | - |
| `物件索引` | 要包含的人物索引，以逗號分隔（例如 '0,2,3'）。同時應用於參考圖像和姿態影片遮罩。空白 = 全部。 | STRING | 是 | - |
| `排序方式` | 調色板顏色分配給追蹤物件的順序（同時應用於參考圖像和姿態影片，使每個身份保持相同顏色）。left_to_right = 最左側物件（以第一幀質心為準）獲得第一個顏色；area = 最大物件（以第一幀遮罩面積為準）獲得第一個顏色；none = 保留 SAM3 的順序。（預設值："left_to_right"） | COMBO | 是 | `"none"`<br>`"left_to_right"`<br>`"area"` |
| `替換模式` | False = 動畫模式（pose_video_mask 背景為黑色，reference_image_mask 背景為白色）。True = 替換模式（pose_video_mask 背景為白色，reference_image_mask 背景為黑色）。（預設值：False） | BOOLEAN | 是 | False<br>True |

## ## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `pose_video_mask` | 從驅動姿態影片追蹤資料渲染的彩色遮罩。背景顏色遵循 replacement_mode 設定。 | IMAGE |
| `reference_image_mask` | 從參考圖像追蹤資料渲染的彩色遮罩。根據模型慣例，始終以黑色背景渲染。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SCAIL2ColoredMask/zh-TW.md)

---
**Source fingerprint (SHA-256):** `c9f6d87410b8bd4082ffb06ef1cf973829566ed222be643db3528cbc241d3c14`
