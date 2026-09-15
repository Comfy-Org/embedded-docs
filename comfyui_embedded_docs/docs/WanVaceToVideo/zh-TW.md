# WAN 人臉轉影片

WanVaceToVideo 節點會為 VACE 控制的影片生成模型準備影片條件資料。它會將正向與負向條件與可選的控制影片、控制遮罩及參考影像結合，透過 VAE 進行編碼，並輸出更新後的條件、空的 latent tensor 及修剪值。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `正向` | 用於引導生成的正向條件輸入 | CONDITIONING | 是 | - |
| `負向` | 用於引導生成的負向條件輸入 | CONDITIONING | 是 | - |
| `vae` | 用於編碼影像與影片影格的 VAE 模型 | VAE | 是 | - |
| `寬度` | 輸出影片寬度（像素，預設：832，步長：16） | INT | 是 | 16 to MAX_RESOLUTION |
| `高度` | 輸出影片高度（像素，預設：480，步長：16） | INT | 是 | 16 to MAX_RESOLUTION |
| `長度` | 影片中的影格數（預設：81，步長：4） | INT | 是 | 1 to MAX_RESOLUTION |
| `批次大小` | 同時生成的影片數量（預設：1） | INT | 是 | 1 至 4096 |
| `強度` | VACE 控制的條件強度（預設：1.0，步長：0.01）。這不是 LoRA 強度。LoRA 權重是透過個別的 LoRA 節點套用。 | FLOAT | 是 | 0.0 至 1000.0 |
| `控制影片` | 用於控制條件的可選輸入影片。若未提供，會自動建立中性灰色影片。 | IMAGE | 否 | - |
| `控制遮罩` | 決定控制影片哪些部分為啟用狀態的可選遮罩。若未提供，會使用全白遮罩。 | MASK | 否 | - |
| `參考影像` | 用於額外條件的可選參考影像。提供時，會將其編碼並附加到 latent 序列開頭。僅會使用第一張影像。 | IMAGE | 否 | - |

**注意：** 提供 `control_video` 時，它會被截斷為 `length` 個影格，並放大至指定的 `width` 與 `height`；若其影格數少於 `length`，缺少的影格會以中性灰色（值 0.5）填充。未提供時，會自動建立包含 `length` 個影格的中性灰色影片。`control_masks` 會放大至指定的 `width` 與 `height`，截斷為 `length` 個影格，若較短則以值 1.0 填充。此遮罩會將控制影片分為非作用部分與反應部分，兩者各自經過 VAE 編碼，並沿通道維度串接；遮罩也會降採樣至 latent 解析度。提供 `reference_image` 時，其第一張影像會經過 VAE 編碼並附加到 latent 序列開頭，而 `trim_latent` 會回報新增的 latent 影格數。latent 影格數計算方式為 `((length - 1) // 4) + 1`，而 latent 空間維度為 `height / 8` 與 `width / 8`。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `positive` | 已套用影片控制資料（vace_frames、vace_mask、vace_strength）的正向條件 | CONDITIONING |
| `negative` | 已套用影片控制資料（vace_frames、vace_mask、vace_strength）的負向條件 | CONDITIONING |
| `latent` | 可用於影片生成的空白 latent tensor，形狀為 [batch_size, 16, latent_length, height/8, width/8] | LATENT |
| `trim_latent` | 使用參考影像時要修剪的 latent 影格數；若未提供參考影像則為 0 | INT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanVaceToVideo/zh-TW.md)

---
**Source fingerprint (SHA-256):** `2039b7509ce5b731e9e41d9cd2dad022d4c5004751f571a4cf88c1ba0cae405b`
