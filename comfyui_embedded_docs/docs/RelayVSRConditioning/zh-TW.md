# RelayVSRConditioning

RelayVSR Conditioning 會為 RelayVSR 影片放大準備條件資料與空 latent。RelayVSR 僅會在影片中每第 15 幀以及最後一幀上執行其單步 Wan 2.2 模型，因此它交給你的 latent 只包含這些關鍵影格。接著由 VSR Decode 補齊它們之間的影格。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | RelayVSR 擴散模型，使用 Load Model 載入：`relayvsr_x2_lightx2v_int8_convrot.safetensors` 或 `relayvsr_x4_int8_convrot.safetensors`。 | MODEL | 是 | 不適用 |
| `images` | 原始解析度的低品質影片。模型的放大倍率決定結果的大小。 | IMAGE | 是 | 不適用 |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `positive` | 攜帶所選關鍵影格作為低品質引導的條件資料。 | CONDITIONING |
| `latent` | 每個關鍵影格對應一幀的空 latent，可供取樣器使用。 | LATENT |

## 使用方式

將 `positive` 連接到取樣器的 positive 輸入，然後以 CFG 1、一步對 `latent` 進行取樣：此工作流程中沒有提示詞，也沒有文字編碼器。將取樣器的輸出、相同的 `images` 與 RelayVSR Flash VAE 送入 VSR Decode，並保持兩者配對一致：x2 模型搭配 x2 解碼器，x4 模型搭配 x4 解碼器。

由於只會對關鍵影格進行取樣，因此 150 幀的影片會變成 11 幀的 latent。取樣器只處理影片的一小部分，其餘部分則由 VSR Decode 還原。

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RelayVSRConditioning/zh-TW.md)

---
**Source fingerprint (SHA-256):** `fd1a86262240430e4f2a811c2c9d8d62f0b6cdfccb26d5285e36d0d6de3b186f`
