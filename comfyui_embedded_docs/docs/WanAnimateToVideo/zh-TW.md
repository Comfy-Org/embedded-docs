> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanAnimateToVideo/zh-TW.md)

WanAnimateToVideo 節點透過結合多個條件輸入（包括姿勢參考、面部表情和背景元素）來生成影片內容。它處理各種影片輸入以創建連貫的動畫序列，同時保持幀與幀之間的時間一致性。該節點處理潛空間操作，並可透過延續運動模式來擴展現有影片。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | 是 | - | 用於引導生成朝向期望內容的正向條件 |
| `negative` | CONDITIONING | 是 | - | 用於引導生成遠離不想要內容的負向條件 |
| `vae` | VAE | 是 | - | 用於編碼和解碼影像資料的 VAE 模型 |
| `width` | INT | 否 | 16 至 MAX_RESOLUTION | 輸出影片寬度（像素）（預設：832，間隔：16） |
| `height` | INT | 否 | 16 至 MAX_RESOLUTION | 輸出影片高度（像素）（預設：480，間隔：16） |
| `length` | INT | 否 | 1 至 MAX_RESOLUTION | 要生成的幀數（預設：77，間隔：4） |
| `batch_size` | INT | 否 | 1 至 4096 | 同時生成的影片數量（預設：1） |
| `clip_vision_output` | CLIP_VISION_OUTPUT | 否 | - | 用於附加條件的可選 CLIP 視覺模型輸出 |
| `reference_image` | IMAGE | 否 | - | 用作生成起點的參考影像 |
| `face_video` | IMAGE | 否 | - | 提供面部表情指導的影片輸入 |
| `pose_video` | IMAGE | 否 | - | 提供姿勢和運動指導的影片輸入 |
| `continue_motion_max_frames` | INT | 否 | 1 至 MAX_RESOLUTION | 從先前運動延續的最大幀數（預設：5，間隔：4） |
| `background_video` | IMAGE | 否 | - | 與生成內容合成的背景影片 |
| `character_mask` | MASK | 否 | - | 定義用於選擇性處理的角色區域遮罩 |
| `continue_motion` | IMAGE | 否 | - | 用於時間一致性的先前運動序列延續 |
| `video_frame_offset` | INT | 否 | 0 至 MAX_RESOLUTION | 在所有輸入影片中跳過的幀數。用於分段生成較長影片。連接到前一個節點的 video_frame_offset 輸出以擴展影片。（預設：0，間隔：1） |

**參數約束：**

- 當提供 `pose_video` 且 `trim_to_pose_video` 邏輯啟用時，輸出長度將調整以匹配姿勢影片的持續時間
- `face_video` 在處理時會自動調整為 512x512 解析度
- `continue_motion` 幀數受 `continue_motion_max_frames` 參數限制
- 輸入影片（`face_video`、`pose_video`、`background_video`、`character_mask`）在處理前會根據 `video_frame_offset` 進行偏移
- 如果 `character_mask` 僅包含一幀，它將在所有幀中重複使用
- 當提供 `clip_vision_output` 時，它會同時應用於正向和負向條件

## 輸出參數

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | 帶有附加影片上下文資訊的修改後正向條件 |
| `negative` | CONDITIONING | 帶有附加影片上下文資訊的修改後負向條件 |
| `latent` | LATENT | 以潛空間格式生成的影片內容 |
| `trim_latent` | INT | 用於下游處理的潛空間修剪資訊 |
| `trim_image` | INT | 用於參考運動幀的影像空間修剪資訊 |
| `video_frame_offset` | INT | 用於分段繼續影片生成的更新幀偏移量 |