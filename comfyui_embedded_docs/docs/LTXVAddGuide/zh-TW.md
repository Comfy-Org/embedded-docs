# LTXV 添加引導

LTXVAddGuide 透過將輸入的影像或影片編碼，並將其作為關鍵幀納入 conditioning 資料中，為 latent 序列新增影片 conditioning 引導。它會透過 VAE 編碼器處理輸入，並將產生的 latent 策略性地放置在指定的幀位置，同時以關鍵幀資訊更新正向與負向 conditioning。此節點處理幀對齊限制，並允許控制 conditioning 影響的強度。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `positive` | 要透過關鍵幀引導修改的正向 conditioning 輸入 | CONDITIONING | 是 | - |
| `negative` | 要透過關鍵幀引導修改的負向 conditioning 輸入 | CONDITIONING | 是 | - |
| `vae` | 用於編碼輸入影像/影片幀的 VAE 模型 | VAE | 是 | - |
| `latent` | 接收 conditioning 幀的輸入 latent 序列 | LATENT | 是 | - |
| `image` | 用於對 latent 影片進行 conditioning 的影像或影片。必須為 8*n + 1 幀。若影片不是 8*n + 1 幀，將被裁切至最接近的 8*n + 1 幀。 | IMAGE | 是 | - |
| `frame_idx` | 開始 conditioning 的幀索引。對於單幀影像或 1-8 幀的影片，任何 `frame_idx` 值皆可接受。對於 9 幀以上的影片，`frame_idx` 必須能被 8 整除，否則會向下取整至最接近的 8 的倍數。負值從影片末尾開始計算。（預設值：0） | INT | 否 | -9999 至 9999 |
| `strength` | conditioning 影響的強度，其中 1.0 套用完整 conditioning，0.0 不套用任何 conditioning（預設值：1.0） | FLOAT | 否 | 0.0 至 10.0 |
| `attention_mask` | 可選的像素空間空間遮罩。透過 self-attention 控制每個區域的 conditioning 影響，並與 `strength` 相乘。 | MASK | 否 | - |
| `iclora_parameters` | 來自 Get IC-LoRA Parameters 節點的可選 IC-LoRA 參數。用於依特定 IC-LoRA 的需求調整引導處理（例如 `reference_downscale_factor` 大於 1 的 IC-LoRA）。串接時，每個 LTXVAddGuide 僅使用與其連接的參數。 | IC_LORA_PARAMETERS | 否 | - |

**注意事項：**

- 輸入的影像/影片必須符合 8*n + 1 的幀數模式（例如 1、9、17、25 幀）。若輸入超出此模式，將自動裁切至最接近的有效幀數。
- 當使用 `reference_downscale_factor` 大於 1 的 IC-LoRA 參數時，latent 的空間維度（寬與高）必須能被該因數整除。若未滿足此條件，節點會引發錯誤。
- 引導內容必須能放入 latent 序列中：起始幀索引加上引導幀數不得超過 latent 長度，否則節點會引發錯誤。
- 此節點不支援結合音訊與影片的 latent。輸入的 `latent` 與編碼後的引導資料都必須使用標準的 128 通道影片 latent 格式，否則節點會引發錯誤。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `positive` | 已使用關鍵幀引導資訊更新的正向 conditioning | CONDITIONING |
| `negative` | 已使用關鍵幀引導資訊更新的負向 conditioning | CONDITIONING |
| `latent` | 已納入 conditioning 幀並更新雜訊遮罩的 latent 序列 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAddGuide/zh-TW.md)

---
**Source fingerprint (SHA-256):** `3e0d1422fbd1b5b3e4c69e641af2ecdb5ae8de3f4368b336917a0dce4286771e`
