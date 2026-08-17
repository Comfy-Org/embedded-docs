# WanInfiniteTalkToVideo

WanInfiniteTalkToVideo 節點可從音訊生成一段說話者頭像影片。它會以一位或兩位說話者的音訊特徵作為條件，引導影片擴散模型；可選擇性地使用起始影像或先前幀作為上下文，並回傳經修補的模型、條件（conditioning）以及用於取樣的潛在影片（latent video）。

## 輸入

### 通用輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `mode` | 音訊模式。選擇 `"single_speaker"` 時使用一個音訊輸入；選擇 `"two_speakers"` 時會新增下方列出的第二個說話者輸入。 | DYNAMIC_COMBO | 是 | `"single_speaker"`<br>`"two_speakers"` |
| `model` | 要修補的基礎影片擴散模型。 | MODEL | 是 | - |
| `model_patch` | 包含音訊投影層（audio projection layers）的模型修補。 | MODELPATCH | 是 | - |
| `positive` | 用於引導影片生成的正向條件。 | CONDITIONING | 是 | - |
| `negative` | 用於引導影片生成的負向條件。 | CONDITIONING | 是 | - |
| `vae` | 用於將影像與先前幀編碼至潛在空間的 VAE。 | VAE | 是 | - |
| `width` | 生成影片的寬度（像素），以 16 為步進。（預設值：832） | INT | 是 | 16 - MAX_RESOLUTION (step 16) |
| `height` | 生成影片的高度（像素），以 16 為步進。（預設值：480） | INT | 是 | 16 - MAX_RESOLUTION (step 16) |
| `length` | 要生成的幀數。（預設值：81） | INT | 是 | 1 - MAX_RESOLUTION (step 4) |
| `audio_encoder_output_1` | 第一個說話者的音訊編碼器輸出，包含用於條件化的音訊特徵。 | AUDIOENCODEROUTPUT | 是 | - |
| `start_image` | 可選的起始影像，用於初始化影片的開頭。系統會將其調整為 `width` 和 `height` 的大小。 | IMAGE | 否 | - |
| `clip_vision_output` | 可選的 CLIP 視覺輸出，會同時加入正向與負向條件中。 | CLIPVISIONOUTPUT | 否 | - |
| `motion_frame_count` | 用作動態上下文（motion context）的先前幀數。（預設值：9） | INT | 是 | 1 - 33 (step 1) |
| `audio_scale` | 套用至音訊條件的縮放係數。（預設值：1.0） | FLOAT | 是 | -10.0 - 10.0 (step 0.01) |
| `previous_frames` | 可選的先前影片幀，用於延伸既有序列。節點會使用最後 `motion_frame_count` 個幀作為動態上下文。 | IMAGE | 否 | - |

### 單一說話者輸入

選擇 `single_speaker` 不會新增任何額外輸入。

### 雙說話者輸入

當 `mode` 為 `"two_speakers"` 時，可使用下列輸入。

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `audio_encoder_output_2` | 第二個說話者的音訊編碼器輸出。提供此參數時，也必須提供 `mask_1` 與 `mask_2`。 | AUDIOENCODEROUTPUT | 否 | - |
| `mask_1` | 第一個說話者的遮罩；使用雙音訊輸入時為必填。 | MASK | 否 | - |
| `mask_2` | 第二個說話者的遮罩；使用雙音訊輸入時為必填。 | MASK | 否 | - |

**參數約束：**

- 若提供了 `audio_encoder_output_2`，則也必須同時提供 `mask_1` 與 `mask_2`。
- 若同時提供了 `mask_1` 與 `mask_2`，則也必須提供 `audio_encoder_output_2`。
- 若提供了 `previous_frames`，其幀數必須至少等於 `motion_frame_count` 指定的數量。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `model` | 已套用音訊條件與取樣包裝器的修補後模型。 | MODEL |
| `positive` | 正向條件，可能已使用起始影像或 CLIP 視覺上下文進行修改。 | CONDITIONING |
| `negative` | 負向條件，可能已使用起始影像或 CLIP 視覺上下文進行修改。 | CONDITIONING |
| `latent` | 一個初始化為零的潛在張量，代表待生成的影片。 | LATENT |
| `trim_image` | 從先前幀延伸時，需要從開頭裁掉的幀數；若是開始新序列則為 0。 | INT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanInfiniteTalkToVideo/zh-TW.md)

---
**Source fingerprint (SHA-256):** `b7359490c1de86d9c82122bc227295b3b7f8a3493f629365ae0f22f9f34d9a66`
