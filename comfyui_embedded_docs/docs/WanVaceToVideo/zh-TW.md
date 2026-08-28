# WAN 人臉轉影片

WanVaceToVideo 節點用於為影片生成模型準備影片條件資料。它接收正向與負向條件輸入，以及選用的控制影片、遮罩與參考影像，並將它們編碼為潛在表示，以引導影片生成。此節點處理放大、填補、遮罩及 VAE 編碼，以建立適合影片模型的條件結構。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `正向` | 用於引導生成的正向條件輸入 | CONDITIONING | 是 | - |
| `負向` | 用於引導生成的負向條件輸入 | CONDITIONING | 是 | - |
| `vae` | 用於編碼影像與影片影格的 VAE 模型 | VAE | 是 | - |
| `寬度` | 輸出影片寬度（像素）（預設：832，步長：16） | INT | 是 | 16 to MAX_RESOLUTION |
| `高度` | 輸出影片高度（像素）（預設：480，步長：16） | INT | 是 | 16 to MAX_RESOLUTION |
| `長度` | 影片的影格數（預設：81，步長：4） | INT | 是 | 1 to MAX_RESOLUTION |
| `批次大小` | 同時生成的影片數量（預設：1） | INT | 是 | 1 至 4096 |
| `強度` | VACE 控制條件的強度（預設：1.0，步長：0.01）。這不是 LoRA 強度。LoRA 權重需透過個別 LoRA 節點套用。 | FLOAT | 是 | 0.0 至 1000.0 |
| `控制影片` | 用於控制條件的選用輸入影片。若未提供，會自動建立中性灰影片。 | IMAGE | 否 | - |
| `控制遮罩` | 選用遮罩，用於決定控制影片的哪些部分為啟用。若未提供，會使用全白遮罩。 | MASK | 否 | - |
| `參考影像` | 供額外條件使用的選用參考影像。提供時，它會被編碼並前置至潛在序列。 | IMAGE | 否 | - |

**注意：** 若提供了 `control_video`，它會被截斷為 `length` 個影格，並放大至指定的 `width` 與 `height`；若其影格數少於 `length`，缺少的影格會以中性灰（值 0.5）填補。若未提供 `control_video`，則會自動建立長度為 `length` 個影格的中性灰影片。`control_masks` 會被放大至指定的 `width` 與 `height`，截斷為 `length` 個影格，若較短則以值 1.0 填補。此遮罩會將控制影片分為未啟用與反應部分，各部分分別經 VAE 編碼後沿通道維度串接；遮罩也會被降採樣至潛在解析度。當提供 `reference_image` 時，它會經 VAE 編碼並前置至潛在序列。潛在影格數的計算方式為 `((length - 1) // 4) + 1`，潛在空間尺寸為 `height / 8` 與 `width / 8`。

## 輸出

| 輸出名 | 描述 | 資料類型 |
| --- | --- | --- |
| `正向` | 已套用影片控制資料（vace_frames、vace_mask、vace_strength）的正向條件 | CONDITIONING |
| `負向` | 已套用影片控制資料（vace_frames、vace_mask、vace_strength）的負向條件 | CONDITIONING |
| `潛在空間` | 已準備好進行影片生成的空潛在張量，形狀為 [batch_size, 16, latent_length, height/8, width/8] | LATENT |
| `裁剪潛空間` | 使用參考影像時需修剪的潛在影格數；若未提供參考影像則為 0 | INT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanVaceToVideo/zh-TW.md)

---
**Source fingerprint (SHA-256):** `2039b7509ce5b731e9e41d9cd2dad022d4c5004751f571a4cf88c1ba0cae405b`
