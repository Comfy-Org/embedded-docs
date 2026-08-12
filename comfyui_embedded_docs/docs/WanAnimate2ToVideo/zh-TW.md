# WanAnimate2ToVideo

WanAnimate2ToVideo 透過從獨立的姿態影片中轉移臉部表情、身體動作和手勢，對參考影像中的角色進行動畫化。它會建立條件化資料與起始潛在表示，供影片生成取樣器用來建立動畫。

## 輸入
| 參數 | 說明 | 資料型別 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `positive` | 影片生成的正向條件化。 | CONDITIONING | 是 | N/A |
| `negative` | 影片生成的負向條件化。 | CONDITIONING | 是 | N/A |
| `vae` | 用於將參考影像和影片幀編碼至潛在空間的 VAE。 | VAE | 是 | N/A |
| `width` | 輸出影片的寬度（像素）。（預設值：832） | INT | 是 | 16 至 MAX_RESOLUTION (步長 16) |
| `height` | 輸出影片的高度（像素）。（預設值：480） | INT | 是 | 16 至 MAX_RESOLUTION (步長 16) |
| `length` | 要生成的幀數。（預設值：81） | INT | 是 | 1 至 MAX_RESOLUTION (步長 4) |
| `batch_size` | 同時生成的影片數量。（預設值：1） | INT | 是 | 1 至 4096 |
| `reference_image` | 要進行動畫化的角色。若省略，則使用黑色影像。 | IMAGE | 否 | N/A |
| `pose_video` | 其動作會被轉移到參考角色的影片。若幀數少於 `length`，會重複最後一幀以填補缺少的幀數。 | IMAGE | 否 | N/A |
| `clip_vision_output` | 參考影像的 CLIP vision 輸出。 | CLIP_VISION_OUTPUT | 否 | N/A |
| `positive_pose` | 姿態影片分支的提示詞，描述動作而非角色。預設為 `positive`。條件（cond）與非條件（uncond）傳遞都會使用。 | CONDITIONING | 否 | N/A |
| `clip_vision_output_pose` | 姿態影片第一幀的 CLIP vision 輸出。預設為 `clip_vision_output`。 | CLIP_VISION_OUTPUT | 否 | N/A |
| `continue_motion` | 要接續的先前動作序列，以維持時間一致性。此序列只會使用最後一幀作為起始動作幀。 | IMAGE | 否 | N/A |
| `video_frame_offset` | 姿態影片的幀偏移量。延伸時，連接到前一個節點的 `video_frame_offset` 輸出。（預設值：0） | INT | 是 | 0 至 MAX_RESOLUTION |
| `pose_strength` | 縮放姿態影片對動作的影響程度。1.0 為訓練時的行為；低於此值會降低遵循程度，高於此值則會增強。0.0 會將其靜音，但不會完全移除。（預設值：1.0） | FLOAT | 是 | 0.00 至 10.00 (步長 0.01) |
| `pose_start_percent` | 姿態影響開始時的取樣百分比。在此區間之外，姿態分支會被完全跳過，同時也能加速這些步驟。（預設值：0.0） | FLOAT | 是 | 0.00 至 1.00 (步長 0.01) |
| `pose_end_percent` | 姿態影響結束時的取樣百分比。動作大多在早期就已確立，因此例如 0.7 可以在保持編排的同時放寬細節。（預設值：1.0） | FLOAT | 是 | 0.00 至 1.00 (步長 0.01) |
| `reference_image_strength` | 縮放生成幀對參考影像潛在幀的關注強度。低於 1.0 會放寬身分/外觀的遵循度（例如讓提示詞重新造型），高於 1.0 則會加強遵循以防止漂移。（預設值：1.0） | FLOAT | 是 | 0.00 至 10.00 (步長 0.01) |

**驗證注意事項：**

- `pose_start_percent` 不得大於 `pose_end_percent`，否則節點會引發 ValueError。
- 若提供了 `pose_video`，其幀數必須大於 `video_frame_offset`，否則節點會引發 ValueError。

## 輸出
| 輸出名稱 | 說明 | 資料型別 |
|-------------|-------------|-----------|
| `positive` | 用於取樣的正向條件化，附帶參考影像、遮罩及可選的姿態資料。 | CONDITIONING |
| `negative` | 用於取樣的負向條件化，附帶相同的參考影像、遮罩及可選的姿態資料。 | CONDITIONING |
| `latent` | 供影片取樣器使用的零填充起始潛在表示；解碼前應移除前 `trim_latent` 幀。 | LATENT |
| `trim_latent` | 解碼前應修剪的潛在幀數。 | INT |
| `trim_image` | 延伸影片時重疊的影像幀數。 | INT |
| `video_frame_offset` | 姿態影片的幀偏移量；等於調整後的輸入偏移量加上已生成的幀數。 | INT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanAnimate2ToVideo/zh-TW.md)

---
**Source fingerprint (SHA-256):** `7e1f497983ab63a68e5ef5439b3ef4e9295f79f78530c9dc5de16a8238475f05`
