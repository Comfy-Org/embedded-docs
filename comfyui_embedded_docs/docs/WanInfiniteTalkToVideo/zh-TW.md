# WanInfiniteTalkToVideo

WanInfiniteTalkToVideo 可從音訊輸入生成影片序列。它使用影片擴散模型，以從一或兩位說話者提取的音訊特徵為條件，產生說話者人像影片的潛在表示。此節點可以生成新序列，或使用先前幀作為動作上下文來擴展現有序列。

## 輸入

### 通用輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `模式` | 音訊輸入模式。`single_speaker` 使用一個音訊輸入。`two_speakers` 啟用「雙說話者輸入」一節中列出的額外音訊輸入和遮罩。 | DYNAMIC_COMBO | 是 | `"single_speaker"`<br>`"two_speakers"` |
| `模型` | 基礎影片擴散模型。 | MODEL | 是 | - |
| `模型修補` | 包含音訊投影層的模型修補。 | MODEL_PATCH | 是 | - |
| `正向提示` | 用於引導生成的正向條件。 | CONDITIONING | 是 | - |
| `負向提示` | 用於引導生成的負向條件。 | CONDITIONING | 是 | - |
| `vae` | 用於在潛在空間中對影像進行編碼及解碼的 VAE。 | VAE | 是 | - |
| `寬度` | 輸出影片的寬度（像素）。必須能被 16 整除。（預設值：832） | INT | 是 | 16 - MAX_RESOLUTION (step 16) |
| `高度` | 輸出影片的高度（像素）。必須能被 16 整除。（預設值：480） | INT | 是 | 16 - MAX_RESOLUTION (step 16) |
| `長度` | 要生成的幀數。（預設值：81） | INT | 是 | 1 - MAX_RESOLUTION (step 4) |
| `clip 視覺輸出` | 可選的 CLIP 視覺輸出，用於額外條件化。 | CLIP_VISION_OUTPUT | 否 | - |
| `起始圖像` | 可選的起始影像，用於初始化影片序列。 | IMAGE | 否 | - |
| `音訊編碼器輸出 1` | 主要音訊編碼器輸出，包含第一位說話者的特徵。 | AUDIO_ENCODER_OUTPUT | 是 | - |
| `動作影格數` | 用作動作上下文的先前幀數。（預設值：9） | INT | 是 | 1 - 33 |
| `音訊縮放` | 套用至音訊條件化的縮放因子。（預設值：1.0） | FLOAT | 是 | -10.0 - 10.0 |
| `前置影格` | 可選的先前影片幀，用於從中擴展。最後 `motion_frame_count` 幀會用作動作上下文。 | IMAGE | 否 | - |

### 雙說話者輸入

此處的輸入會在 `mode` 設為 `"two_speakers"` 時顯示。

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `audio_encoder_output_2` | 第二音訊編碼器輸出，包含第二位說話者的特徵。 | AUDIO_ENCODER_OUTPUT | 否 | - |
| `mask_1` | 第一位說話者的遮罩，若使用兩個音訊輸入則為必填。 | MASK | 否 | - |
| `mask_2` | 第二位說話者的遮罩，若使用兩個音訊輸入則為必填。 | MASK | 否 | - |

**參數限制：**

- 當 `mode` 設為 `"two_speakers"` 時，`audio_encoder_output_2`、`mask_1` 和 `mask_2` 是第二位說話者設定所必需的。
- 若提供了 `audio_encoder_output_2`，則也必須提供 `mask_1` 和 `mask_2`。
- 若提供了 `mask_1` 和 `mask_2`，則也必須提供 `audio_encoder_output_2`。
- 若提供了 `previous_frames`，其幀數必須至少等於 `motion_frame_count` 所指定的數目。

## 輸出

| 輸出名 | 描述 | 資料類型 |
| --- | --- | --- |
| `模型` | 套用了音訊條件化的已修補模型。 | MODEL |
| `正向提示` | 正向條件，可能已透過額外上下文（例如起始影像或 CLIP 視覺輸出）修改。 | CONDITIONING |
| `負向提示` | 負向條件，可能已透過額外上下文修改。 | CONDITIONING |
| `latent` | 在潛在空間中生成的影片序列。 | LATENT |
| `裁切圖像` | 擴展序列時應從動作上下文開頭修剪的幀數。當提供了 `previous_frames` 時等於 `motion_frame_count`，否則為 0。 | INT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanInfiniteTalkToVideo/zh-TW.md)

---
**Source fingerprint (SHA-256):** `b7359490c1de86d9c82122bc227295b3b7f8a3493f629365ae0f22f9f34d9a66`
