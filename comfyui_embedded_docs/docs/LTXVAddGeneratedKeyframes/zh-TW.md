# LTXV 新增生成關鍵影格

LTXV Add Generated Keyframes 節點會將 detailing keyframes 附加到 video latent。每個 keyframe 是單一 latent frame 的 tokens，定位於單一 pixel frame 上；它會與 video 一起被 denoised，且不屬於 decoded output 的一部分。放置方式為每隔 `interval_frames` pixels 放置一個 slot，並跳過 I2V frames、現有 guides，以及已在 conditioning 上的 generated keyframes；可使用 LTXV Separate Generated Keyframes 將它們取回。需要一個針對 generated keyframes 訓練的 checkpoint（帶有 `keyframes_abs_pos_embedding` 的 checkpoint）。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `positive` | 要附加這些 keyframes 的正向 conditioning。 | CONDITIONING | 是 | N/A |
| `negative` | 要附加這些 keyframes 的負向 conditioning。 | CONDITIONING | 是 | N/A |
| `vae` | 僅用於讀取 latent scale factors。 | VAE | 是 | N/A |
| `latent` | 要用來一同產生 keyframes 的單純 5D video latent。請在 Concat AV Latent 之前加入它們。 | LATENT | 是 | N/A |
| `interval_frames` | 自動放置用的 pixel-frame 步幅。預設 24 在 24 fps 下約為每秒一個 keyframe。已佔用的 pixels 會被跳過。當設定 `frame_indices` 時會被忽略。（預設值：24） | INT | 否 | 1-1024 |
| `keyframes` | 選用內容，用來初始化新的 keyframes。連接來自較早 Separate 的 keyframes（相同空間尺寸），或連接一個單純 video latent，以在每個新 slot 複製最接近的 frame（例如在 temporal upscale 之後）。這些仍會被 denoised，不會被固定為 guides。除非設定 `frame_indices`，否則 keyframes latent 上記錄的 indices 會被忽略。僅在 sampling 從低於 sigma 1 開始時才有作用。 | LATENT | 否 | N/A |
| `frame_indices` | 選用的 pixel-frame indices。留空時會依 `interval_frames` 在目前 canvas 上放置。設定後，此列表即為放置位置（連接的 keyframes 會依序配對）。允許最後一個 frame；不允許 frame 0（它已經是獨立的 token）。（預設值：空字串） | STRING | 否 | 以逗號分隔的整數；1 到最後一個 pixel frame（不包含 frame 0） |

**注意：** `latent` 必須是單純的 5D video latent，並在 Concat AV Latent 之前加入 generated keyframes。設定 `frame_indices` 時，列出的每個 pixel frame 都必須唯一，且不能已經包含 image keyframe、guide 或 generated keyframe。如果 `frame_indices` 為空，已佔用的 pixels 會自動跳過；如果沒有可用的 detailing slot，節點會引發錯誤。當附加到現有的 generated keyframes 時，latent 仍必須具有相同的每 frame tokens 數量，且現有區塊必須在最後一個 latent frame 結束。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-----------|-----------|
| `positive` | 已附加 generated-keyframe attention 的正向 conditioning。 | CONDITIONING |
| `negative` | 已附加 generated-keyframe attention 的負向 conditioning。 | CONDITIONING |
| `latent` | 已在 T 上附加 generated keyframes 的 video latent。 | LATENT |

## 備註

- `interval_frames` 參數會設定自動放置 keyframes 的間距。較高的值會產生較少 keyframes 和較寬的間距；較低的值會產生更多 keyframes。
- `keyframes` 輸入可讓您用現有 keyframes 或 video latent 初始化新的 keyframes。如果提供較長的單純 video latent，會在每個新 slot 複製最接近的 video frame。這些 keyframes 仍會被 denoised，不會被固定為 guides。
- `frame_indices` 參數可讓您指定 keyframes 應放置的精確 pixel-frame indices。提供後，`interval_frames` 會被忽略。列表必須包含有效 pixel 範圍內的唯一整數，且不允許 frame 0。
- `positive` 和 `negative` 輸出包含已附加 generated-keyframe attention 的 conditioning。
- `latent` 輸出包含已在 T 上附加 generated keyframes 的 video latent。
- 需要一個針對 generated keyframes 訓練的 checkpoint（帶有 `keyframes_abs_pos_embedding` 的 checkpoint）。
- 使用 LTXV Separate Generated Keyframes 將 generated keyframes 取回。

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAddGeneratedKeyframes/zh-TW.md)

---
**Source fingerprint (SHA-256):** `43053d15eceb61f37223c46dd46417c71f0503ef3a412ee50a3b2f764f310a64`
