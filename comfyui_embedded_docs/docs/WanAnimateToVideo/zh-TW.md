> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanAnimateToVideo/zh-TW.md)

# WanAnimateToVideo 節點

WanAnimateToVideo 節點透過結合多個條件輸入（包括姿勢參考、面部表情和背景元素）來生成影片內容。它處理各種影片輸入以創建連貫的動畫序列，同時保持跨幀的時間一致性。該節點處理潛在空間操作，並可透過延續運動模式來擴展現有影片。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `正面提示詞` | CONDITIONING | 是 | - | 正向條件，用於引導生成朝向期望內容 |
| `負面提示` | CONDITIONING | 是 | - | 負向條件，用於引導生成遠離不需要的內容 |
| `VAE` | VAE | 是 | - | 用於編碼和解碼圖像資料的 VAE 模型 |
| `寬度` | INT | 是 | 16 至 MAX_RESOLUTION | 輸出影片寬度（像素）（預設值：832，步長：16） |
| `高度` | INT | 是 | 16 至 MAX_RESOLUTION | 輸出影片高度（像素）（預設值：480，步長：16） |
| `長度` | INT | 是 | 1 至 MAX_RESOLUTION | 要生成的幀數（預設值：77，步長：4） |
| `批次大小` | INT | 是 | 1 至 4096 | 同時生成的影片數量（預設值：1） |
| `CLIP視覺輸出` | CLIP_VISION_OUTPUT | 否 | - | 可選的 CLIP 視覺模型輸出，用於額外條件設定 |
| `參考圖像` | IMAGE | 否 | - | 用作生成起始點的參考圖像 |
| `臉部影片` | IMAGE | 否 | - | 提供面部表情引導的影片輸入 |
| `姿勢影片` | IMAGE | 否 | - | 提供姿勢和運動引導的影片輸入 |
| `連續動作最大幀數` | INT | 是 | 1 至 MAX_RESOLUTION | 從先前運動繼續的最大幀數（預設值：5，步長：4） |
| `背景影片` | IMAGE | 否 | - | 與生成內容合成的背景影片 |
| `角色遮罩` | MASK | 否 | - | 定義角色區域以進行選擇性處理的遮罩 |
| `連續動作` | IMAGE | 否 | - | 用於時間一致性的先前運動序列，從此處繼續 |
| `影片幀偏移` | INT | 是 | 0 至 MAX_RESOLUTION | 在所有輸入影片中搜尋的幀偏移量。用於分塊生成更長的影片。連接到前一個節點的 `影片幀偏移` 輸出以擴展影片。（預設值：0，步長：1） |

**參數約束：**

- 當提供 `pose_video` 時，如果 `trim_to_pose_video` 邏輯處於啟用狀態（目前在原始碼中設定為 `False`），輸出長度將調整為匹配姿勢影片的持續時間
- `face_video` 在處理時會自動調整為 512x512 解析度，並歸一化到 -1.0 到 1.0 的範圍
- `continue_motion` 幀受 `continue_motion_max_frames` 參數限制；僅使用輸入中的最後 `continue_motion_max_frames` 幀
- 輸入影片（`face_video`、`pose_video`、`background_video`、`character_mask`）在處理前會根據 `video_frame_offset` 進行偏移；如果偏移超過影片長度，則忽略該輸入
- 如果 `character_mask` 僅包含一幀，則會在所有幀中重複使用
- 當提供 `clip_vision_output` 時，它會同時應用於正向和負向條件
- 如果未提供 `reference_image`，則使用黑色圖像（全零）作為預設參考
- 如果未提供 `continue_motion`，則初始幀會填充灰色（0.5 強度）噪聲

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `負面提示` | CONDITIONING | 修改後的正向條件，包含額外的影片上下文，包括 CLIP 視覺輸出、姿勢影片潛在空間、面部影片像素、串聯的潛在圖像和串聯的遮罩 |
| `潛在空間` | CONDITIONING | 修改後的負向條件，包含額外的影片上下文，包括 CLIP 視覺輸出、姿勢影片潛在空間、面部影片像素（反轉）、串聯的潛在圖像和串聯的遮罩 |
| `修剪潛在空間` | LATENT | 以潛在空間格式生成的影片內容，形狀為 [batch_size, 16, latent_length + trim_latent, latent_height, latent_width] |
| `修剪圖像` | INT | 潛在空間修剪資訊，指示從開頭修剪的潛在幀數（對應於參考圖像潛在幀） |
| `影片幀偏移` | INT | 參考運動幀的圖像空間修剪資訊，指示從開頭修剪的圖像幀數 |
| `影片幀偏移` | INT | 用於分塊繼續影片生成的更新幀偏移量，計算方式為先前的偏移量加上生成的長度 |

---
**Source fingerprint (SHA-256):** `c2ca90f4963f629d51cdd7f4bdb67e01c32ce5ca7d916b1f992ccd220f57566c`
