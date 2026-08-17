# WanSCAILToVideo

WanSCAILToVideo 節點會為影片生成準備條件與空的潛在空間。它會處理選用輸入，例如參考影像、姿態影片、CLIP 視覺輸出與先前幀區塊，並將它們嵌入影片模型的正向與負向條件中。此節點輸出修改後的條件，以及指定影片尺寸的空白潛在張量。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `positive` | 正向條件輸入。 | CONDITIONING | 是 | - |
| `negative` | 負向條件輸入。 | CONDITIONING | 是 | - |
| `vae` | 用於對影像與影片幀進行編碼的 VAE 模型。 | VAE | 是 | - |
| `width` | 輸出影片的寬度（像素，預設值：512）。可依 32 的步長調整。 | INT | 是 | 32 to MAX_RESOLUTION |
| `height` | 輸出影片的高度（像素，預設值：896）。可依 32 的步長調整。 | INT | 是 | 32 to MAX_RESOLUTION |
| `length` | 影片中的幀數（預設值：81）。可從 1 開始依 4 的步長調整。 | INT | 是 | 1 to MAX_RESOLUTION |
| `batch_size` | 一個批次中要生成的影片數量（預設值：1）。 | INT | 是 | 1 to 4096 |
| `pose_strength` | 姿態潛在張量的強度（預設值：1.0）。 | FLOAT | 是 | 0.0 to 10.0 |
| `pose_start` | 姿態條件的起始步（預設值：0.0）。 | FLOAT | 是 | 0.0 to 1.0 |
| `pose_end` | 姿態條件的結束步（預設值：1.0）。 | FLOAT | 是 | 0.0 to 1.0 |
| `video_frame_offset` | 此區塊開始時的累計輸出幀編號。請從前一個區塊的 `video_frame_offset` 輸出接續（預設值：0）。 | INT | 是 | 0 to MAX_RESOLUTION |
| `previous_frame_count` | 用於錨定的 `previous_frames` 尾部幀數。SCAIL-2 訓練時使用 5（81 幀區塊、76 幀步長）（預設值：5）。 | INT | 是 | 1 to MAX_RESOLUTION |
| `pose_video` | 用於姿態條件的影片。會縮小至主影片解析度的一半。 | IMAGE | 否 | - |
| `pose_video_mask` | 僅限 SCAIL-2。與 `pose_video` 同解析度、依身分著色的 SAM3 遮罩影片。 | IMAGE | 否 | - |
| `replacement_mode` | 僅限 SCAIL-2。False = 動畫模式（`pose_video_mask` 應為黑色背景）。True = 替換模式（`pose_video_mask` 應為白色背景）。預設值：False。 | BOOLEAN | 否 | - |
| `reference_image` | 參考影像。第一張影像為主要參考（將所有身分合成到該影像上）。SCAIL-2：額外的批次影像會作為附加視角使用（背面視角、特寫、被遮擋的背景），每一張都需要一個以該身分顏色表示的對應 `reference_image_mask`。 | IMAGE | 否 | - |
| `reference_image_mask` | 僅限 SCAIL-2。與 `reference_image` 批次對應的著色參考遮罩（第一張 = 主要參考遮罩，其餘 = 額外 `reference_image` 的身分遮罩）。 | IMAGE | 否 | - |
| `clip_vision_output` | 用於條件的 CLIP 視覺特徵。模型訓練時使用拉伸調整至長寬比的方式。 | CLIP_VISION_OUTPUT | 否 | - |
| `previous_frames` | 僅限 SCAIL-2。前一個區塊的完整解碼輸出。僅會使用最後的 `previous_frame_count` 個幀作為延伸錨定。 | IMAGE | 否 | - |

**注意：**

- `pose_video` 與 `pose_video_mask` 輸入會從 `video_frame_offset` 開始裁切；如果影片在該偏移之後沒有幀，則會忽略該影片。接著兩者會一併截斷至較短者的長度，並以 `length` 幀為上限。`pose_video` 會在編碼前縮小至主影片解析度的一半。
- `reference_image_mask` 輸入僅在同時提供 `reference_image` 時才生效。`reference_image` 批次中的每張影像都會個別編碼為單幀潛在參考。在替換模式（`replacement_mode=True`）中，會以參考影像遮罩作為 Alpha 遮罩，將參考影像合成到黑色背景上。
- 當提供 `clip_vision_output` 時，它會同時套用至正向與負向條件。
- 當提供 `previous_frames` 時，僅會使用最後的 `previous_frame_count` 個幀作為延伸錨定。輸出的潛在張量會部分填入這些幀的編碼，潛在輸出中會包含雜訊遮罩，且 `video_frame_offset` 會減去保留的幀數來調整（不會低於 0）。

## 輸出

| 輸出名 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `positive` | 修改後的正向條件，可能包含嵌入的參考影像潛在張量、CLIP 視覺輸出、姿態影片潛在張量、驅動遮罩、參考遮罩或先前幀潛在張量。 | CONDITIONING |
| `negative` | 修改後的負向條件，可能包含嵌入的參考影像潛在張量、CLIP 視覺輸出、姿態影片潛在張量、驅動遮罩、參考遮罩或先前幀潛在張量。 | CONDITIONING |
| `latent` | 形狀為 `[batch_size, 16, ((length - 1) // 4) + 1, height // 8, width // 8]` 的空白潛在張量。當提供 `previous_frames` 時，潛在張量會部分填入已編碼的先前幀，並包含雜訊遮罩。 | LATENT |
| `video_frame_offset` | 調整後的偏移量 + `length`。請接入下一個區塊，以進行連續影片生成。 | INT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanSCAILToVideo/zh-TW.md)

---
**Source fingerprint (SHA-256):** `4a1a2201dfa94bd2f1330db02ec18a5e0a6aae9e9ac5ae97d456b7af1aa84b7b`
