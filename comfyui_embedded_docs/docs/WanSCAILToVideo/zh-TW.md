# WanSCAILToVideo

WanSCAILToVideo 節點為 SCAIL 與 SCAIL-2 視訊模型的視訊生成準備條件與空潛在空間。它會處理可選輸入，例如參考圖片、姿勢視訊、CLIP 視覺輸出、彩色身分遮罩及先前幀區塊，並將它們嵌入正向與負向條件中。此節點會輸出修改後的條件，以及一個指定視訊尺寸的空白潛在張量，可供取樣使用。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `正向` | 正向條件輸入。 | CONDITIONING | 是 | - |
| `負向` | 負向條件輸入。 | CONDITIONING | 是 | - |
| `vae` | 用於編碼圖片和視訊幀的 VAE 模型。 | VAE | 是 | - |
| `寬度` | 輸出視訊的寬度（像素，預設值：512）。數值以 32 為步進。 | INT | 是 | 32 to MAX_RESOLUTION |
| `高度` | 輸出視訊的高度（像素，預設值：896）。數值以 32 為步進。 | INT | 是 | 32 to MAX_RESOLUTION |
| `長度` | 視訊中的幀數（預設值：81）。數值以 4 為步進。 | INT | 是 | 1 to MAX_RESOLUTION |
| `批次大小` | 每批生成的視訊數量（預設值：1）。 | INT | 是 | 1 至 4096 |
| `姿勢影片` | 用於姿勢條件的視訊。會縮小至主視訊解析度的一半。 | IMAGE | 否 | - |
| `pose_video_mask` | 僅限 SCAIL-2。對應各身分之彩色 SAM3 遮罩視訊，解析度與 `pose_video` 相同。 | IMAGE | 否 | - |
| `replacement_mode` | 僅限 SCAIL-2。False = 動畫模式（`pose_video_mask` 的背景應為黑色）。True = 替換模式（`pose_video_mask` 的背景應為白色）。（預設值：False） | BOOLEAN | 否 | - |
| `姿勢強度` | 姿勢潛在變量的強度。（預設值：1.0） | FLOAT | 是 | 0.0 至 10.0 |
| `姿勢起始步驟` | 姿勢條件的起始步。（預設值：0.0） | FLOAT | 是 | 0.0 至 1.0 |
| `姿勢結束步驟` | 姿勢條件的結束步。（預設值：1.0） | FLOAT | 是 | 0.0 至 1.0 |
| `參考圖片` | 參考圖片。第一張圖片是主要參考（將所有身分合成到它上面）。SCAIL-2：批次中額外的圖片用作附加視角（背面、特寫、被遮擋的背景），每張都需要以該身分顏色表示的對應 `reference_image_mask`。 | IMAGE | 否 | - |
| `reference_image_mask` | 僅限 SCAIL-2。批次與 `reference_image` 對應的彩色參考遮罩（第一個 = 主要參考遮罩，其餘 = 額外 `reference_image` 的身分遮罩）。 | IMAGE | 否 | - |
| `clip_vision_output` | 用於條件的 CLIP 視覺特徵。模型訓練時使用拉伸調整至長寬比的方式。 | CLIP_VISION_OUTPUT | 否 | - |
| `video_frame_offset` | 此區塊開始時的累積輸出幀。從前一個區塊的 `video_frame_offset` 輸出接入。（預設值：0） | INT | 是 | 0 to MAX_RESOLUTION |
| `previous_frame_count` | `previous_frames` 中用於錨定的尾端幀數。SCAIL-2 以 5 幀訓練（81 幀區塊、76 幀步進）。（預設值：5） | INT | 是 | 1 to MAX_RESOLUTION |
| `previous_frames` | 僅限 SCAIL-2。前一個區塊的完整解碼輸出。只有最後的 `previous_frame_count` 個幀用作延伸錨點。 | IMAGE | 否 | - |

**注意：** `pose_video` 和 `pose_video_mask` 輸入會一起截斷至兩者中較短的長度，且只會處理前 `length` 個幀。若任一輸入的長度小於或等於 `video_frame_offset`，該輸入會被完全忽略。`pose_video` 在編碼前會縮小至主視訊解析度的一半，編碼後的姿勢潛在變量會乘以 `pose_strength`，並且只會在 `pose_start` 與 `pose_end` 時間步之間套用至條件。若提供了 `pose_video_mask`，彩色遮罩視訊會縮小至半解析度，並轉換為 28 通道的驅動遮罩，添加到正向與負向條件中。

**注意：** 當提供了 `reference_image` 時，批次中的每張圖片會個別編碼為潛在變量，並嵌入至正向與負向條件中。第一張圖片是主要參考；其他圖片用作附加視角，每張圖片都需要一個對應的 `reference_image_mask`。`reference_image_mask` 只有在同時提供 `reference_image` 時才會使用；當兩者皆提供時，也會從遮罩建立一個 28 通道的參考遮罩，將參考幀綁定至各身分，並加入到條件中。在替換模式（`replacement_mode=True`）下，會使用參考圖片遮罩作為 alpha 遮罩，將參考圖片合成到黑色背景上。當提供了 `clip_vision_output` 時，它會套用至正向與負向條件。

**注意：** 當提供了 `previous_frames` 時，只有最後 `previous_frame_count` 個幀會用作延伸錨點，且 `video_frame_offset` 會相應調整（減去已錨定的幀數，最小值限制為 0）。已錨定的幀會經過編碼並寫入輸出潛在變量的開頭，同時包含一個雜訊遮罩，使這些幀在生成期間保持不變。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `正向` | 修改後的正向條件，可能包含嵌入的參考圖片潛在變量、CLIP 視覺輸出、姿勢視訊潛在變量、驅動遮罩、參考遮罩或先前幀潛在變量。 | CONDITIONING |
| `負向` | 修改後的負向條件，可能包含嵌入的參考圖片潛在變量、CLIP 視覺輸出、姿勢視訊潛在變量、驅動遮罩、參考遮罩或先前幀潛在變量。 | CONDITIONING |
| `latent` | 形狀為 `[batch_size, 16, ((length - 1) // 4) + 1, height // 8, width // 8]` 的空潛在張量。當提供了 `previous_frames` 時，潛在張量會部分填入已編碼的先前幀，並包含一個雜訊遮罩。 | LATENT |
| `video_frame_offset` | 調整後的偏移量 + 長度。接入下一個區塊，以進行循序視訊生成。 | INT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanSCAILToVideo/zh-TW.md)

---
**Source fingerprint (SHA-256):** `4a1a2201dfa94bd2f1330db02ec18a5e0a6aae9e9ac5ae97d456b7af1aa84b7b`
