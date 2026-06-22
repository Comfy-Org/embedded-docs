# WanInfiniteTalkToVideo

WanInfiniteTalkToVideo 節點可根據音訊輸入生成影片序列。它使用影片擴散模型，並以從一個或兩個說話者提取的音訊特徵作為條件，生成說話頭部影片的潛在表示。此節點可以生成新的序列，或使用先前幀作為運動上下文來擴展現有序列。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `模式` | 音訊輸入模式。`"single_speaker"` 使用一個音訊輸入。`"two_speakers"` 啟用第二個說話者的輸入及對應遮罩。 | COMBO | 是 | `"single_speaker"`<br>`"two_speakers"` |
| `模型` | 基礎影片擴散模型。 | MODEL | 是 | - |
| `模型修補` | 包含音訊投影層的模型修補。 | MODELPATCH | 是 | - |
| `正向提示` | 引導生成的正向條件。 | CONDITIONING | 是 | - |
| `負向提示` | 引導生成的負向條件。 | CONDITIONING | 是 | - |
| `vae` | 用於將影像編碼至潛在空間及從潛在空間解碼的 VAE。 | VAE | 是 | - |
| `寬度` | 輸出影片的寬度（像素）。必須能被 16 整除。（預設值：832） | INT | 否 | 16 - MAX_RESOLUTION |
| `高度` | 輸出影片的高度（像素）。必須能被 16 整除。（預設值：480） | INT | 否 | 16 - MAX_RESOLUTION |
| `長度` | 要生成的幀數。（預設值：81） | INT | 否 | 1 - MAX_RESOLUTION |
| `clip 視覺輸出` | 可選的 CLIP 視覺輸出，用於額外條件。 | CLIPVISIONOUTPUT | 否 | - |
| `起始圖像` | 可選的起始影像，用於初始化影片序列。 | IMAGE | 否 | - |
| `音訊編碼器輸出 1` | 主要音訊編碼器輸出，包含第一個說話者的特徵。 | AUDIOENCODEROUTPUT | 是 | - |
| `動作影格數` | 擴展序列時用作運動上下文的先前幀數。（預設值：9） | INT | 否 | 1 - 33 |
| `音訊縮放` | 應用於音訊條件的縮放因子。（預設值：1.0） | FLOAT | 否 | -10.0 - 10.0 |
| `前置影格` | 可選的先前影片幀，用於從中擴展。 | IMAGE | 否 | - |
| `audio_encoder_output_2` | 第二個音訊編碼器輸出。當 `模式` 設定為 `"two_speakers"` 時為必要。 | AUDIOENCODEROUTPUT | 否 | - |
| `mask_1` | 第一個說話者的遮罩，若使用兩個音訊輸入則為必要。 | MASK | 否 | - |
| `mask_2` | 第二個說話者的遮罩，若使用兩個音訊輸入則為必要。 | MASK | 否 | - |

**參數限制：**

* 當 `mode` 設定為 `"two_speakers"` 時，參數 `audio_encoder_output_2`、`mask_1` 和 `mask_2` 變為必要。
* 若提供了 `audio_encoder_output_2`，則必須同時提供 `mask_1` 和 `mask_2`。
* 若提供了 `mask_1` 和 `mask_2`，則必須同時提供 `audio_encoder_output_2`。
* 若提供了 `previous_frames`，則其必須包含至少 `motion_frame_count` 指定的幀數。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `正向提示` | 已套用音訊條件的修補模型。 | MODEL |
| `負向提示` | 正向條件，可能已透過額外上下文（例如起始影像、CLIP 視覺）修改。 | CONDITIONING |
| `latent` | 負向條件，可能已透過額外上下文修改。 | CONDITIONING |
| `裁切圖像` | 在潛在空間中生成的影片序列。 | LATENT |
| `trim_image` | 擴展序列時，應從運動上下文開頭修剪的幀數。 | INT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanInfiniteTalkToVideo/zh-TW.md)

---
**Source fingerprint (SHA-256):** `6bb976da5cac0b61edb7d4c9d206c7c7ea9ffc0e982034c23c7f2e891e972888`
