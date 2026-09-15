# WanSCAILToVideo

The WanSCAILToVideo 節點會為使用 SCAIL 與 SCAIL-2 影片模型進行影片生成準備條件與空的 latent 空間。它會處理選用輸入，例如參考影像、姿勢影片、CLIP 視覺輸出、彩色身分遮罩及先前影格區塊，並將它們嵌入正向與負向條件中。此節點會輸出修改後的條件，以及指定影片尺寸的空 latent 張量，可供取樣使用。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `正向` | 正向條件輸入。 | CONDITIONING | 是 | - |
| `負向` | 負向條件輸入。 | CONDITIONING | 是 | - |
| `vae` | 用於編碼影像與影片影格的 VAE 模型。 | VAE | 是 | - |
| `寬度` | 輸出影片的寬度，單位為像素（預設：512）。數值步進為 32。 | INT | 是 | 32 至 MAX_RESOLUTION |
| `高度` | 輸出影片的高度，單位為像素（預設：896）。數值步進為 32。 | INT | 是 | 32 至 MAX_RESOLUTION |
| `長度` | 影片中的影格數（預設：81）。數值步進為 4。 | INT | 是 | 1 至 MAX_RESOLUTION |
| `批次大小` | 批次中要生成的影片數量（預設：1）。 | INT | 是 | 1 至 4096 |
| `姿勢影片` | 用於姿勢條件的影片。會縮小為主影片解析度的一半。 | IMAGE | 否 | - |
| `pose_video_mask` | 僅適用於 SCAIL-2。與 `pose_video` 相同解析度的彩色逐身分 SAM3 遮罩影片。 | IMAGE | 否 | - |
| `replacement_mode` | 僅適用於 SCAIL-2。False = 動畫模式（`pose_video_mask` 應為黑色背景）。True = 替換模式（`pose_video_mask` 應為白色背景）。（預設：False） | BOOLEAN | 否 | - |
| `姿勢強度` | 姿勢 latent 的強度。（預設：1.0） | FLOAT | 是 | 0.0 至 10.0 |
| `姿勢起始步驟` | 姿勢條件的起始步數。（預設：0.0） | FLOAT | 是 | 0.0 至 1.0 |
| `姿勢結束步驟` | 姿勢條件的結束步數。（預設：1.0） | FLOAT | 是 | 0.0 至 1.0 |
| `參考圖片` | 參考影像。第一張影像為主要參考（將所有身分合成到其上）。SCAIL-2：額外的批次影像會用作附加視圖（背面視圖、特寫、被遮擋的背景），每張都需要在該身分對應顏色中有一個相符的 `reference_image_mask`。 | IMAGE | 否 | - |
| `reference_image_mask` | 僅適用於 SCAIL-2。彩色參考遮罩，批次與 `reference_image` 相符（第一個 = 主要參考遮罩，其餘 = 附加 `reference_image` 的身分遮罩）。 | IMAGE | 否 | - |
| `clip_vision_output` | 用於條件的 CLIP 視覺特徵。模型是以拉伸縮放至長寬比的方式訓練。 | CLIP_VISION_OUTPUT | 否 | - |
| `video_frame_offset` | 此區塊開始的累積輸出影格。從上一個區塊的 `video_frame_offset` 輸出連接而來。（預設：0） | INT | 是 | 0 至 MAX_RESOLUTION |
| `previous_frame_count` | 要用來錨定的 `previous_frames` 尾端影格。SCAIL-2 以 5 訓練（81 影格區塊，76 影格步進）。（預設：5）。數值步進為 4。 | INT | 是 | 1 至 MAX_RESOLUTION |
| `previous_frames` | 僅適用於 SCAIL-2。上一個區塊的完整解碼輸出。只會使用最後 `previous_frame_count` 個影格作為擴展錨點。 | IMAGE | 否 | - |

**注意：** `pose_video` 與 `pose_video_mask` 輸入會一起截斷至兩者中較短者，且僅會針對前 `length` 個影格進行處理。若任一輸入短於或等於 `video_frame_offset`，則會完全忽略。`pose_video` 在編碼前會縮小為主影片解析度的一半，且編碼後的姿勢 latent 會乘以 `pose_strength`，僅在 `pose_start` 與 `pose_end` 時間步之間套用至條件。若提供 `pose_video_mask`，彩色遮罩影片會縮小為一半解析度，並轉換為 28 通道的驅動遮罩，該遮罩會加入正向與負向條件。

**注意：** 當提供 `reference_image` 時，批次中的每張影像都會個別編碼為 latent，並嵌入正向與負向條件。第一張影像為主要參考；額外影像會用作附加視圖，每張都需要有相符的 `reference_image_mask`。只有在同時提供 `reference_image` 時才會使用 `reference_image_mask`；當兩者都提供時，也會從遮罩建立一個將參考影格綁定至身分的 28 通道參考遮罩，並加入條件中。在替換模式（`replacement_mode=True`）下，參考影像會以參考影像遮罩作為 alpha 遮罩，合成到黑色背景上。當提供 `clip_vision_output` 時，它會套用至正向與負向條件。

**注意：** 當提供 `previous_frames` 時，只會使用最後 `previous_frame_count` 個影格作為擴展錨點，並據此調整 `video_frame_offset`（減去錨定影格數，並以 0 為下限）。錨定影格會編碼並寫入輸出 latent 的開頭，且會包含雜訊遮罩，以便這些影格在生成期間保持不變。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `positive` | 修改後的正向條件，可能包含嵌入式參考影像 latent、CLIP 視覺輸出、姿勢影片 latent、驅動遮罩、參考遮罩或先前影格 latent。 | CONDITIONING |
| `negative` | 修改後的負向條件，可能包含嵌入式參考影像 latent、CLIP 視覺輸出、姿勢影片 latent、驅動遮罩、參考遮罩或先前影格 latent。 | CONDITIONING |
| `latent` | 形狀為 `[batch_size, 16, ((length - 1) // 4) + 1, height // 8, width // 8]` 的空 latent 張量。當提供 `previous_frames` 時，latent 會部分填入編碼後的先前影格，並包含雜訊遮罩。 | LATENT |
| `video_frame_offset` | 調整後的偏移 + 長度。連接到下一個區塊，以進行連續影片生成。 | INT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanSCAILToVideo/zh-TW.md)

---
**Source fingerprint (SHA-256):** `4a1a2201dfa94bd2f1330db02ec18a5e0a6aae9e9ac5ae97d456b7af1aa84b7b`
