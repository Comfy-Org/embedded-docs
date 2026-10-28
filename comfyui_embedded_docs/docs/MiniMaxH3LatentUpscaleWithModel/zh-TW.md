# MiniMax H3 Latent Upscale With Model

MiniMax H3 Latent Upscale With Model 會使用 Latent 放大模型，將 MiniMax H3 latent 中的影片部分調整為目標寬度與高度。音訊 latent 會保持原樣一併保留，因此片段能保留聲音，且不需要重新取樣。當片段需要以更大尺寸輸出時，請在 MiniMax H3 取樣之後、H3 VAE 解碼之前使用此節點。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | Latent 放大模型，通常透過 Load Latent Upscale Model 載入。它必須是 MiniMax H3 3D-conv latent 放大器。 | LATENT_UPSCALE_MODEL | 是 | - |
| `samples` | 要調整尺寸的 MiniMax H3 latent。巢狀 latent 會保持其音訊部分不變。 | LATENT | 是 | - |
| `width` | 目標影片寬度，單位為像素。latent 會調整為 `width / 16` 欄，因此數值會向下捨入至 16 的倍數。（預設值：2560） | INT | 是 | 32 至 16384 （步進值：32） |
| `height` | 目標影片高度，單位為像素，也會向下捨入至 16 的倍數。（預設值：1440） | INT | 是 | 32 至 16384 （步進值：32） |

當要求的尺寸已與 latent 相符時，會原樣返回輸入的 latent。輸出 latent 不帶 `noise_mask`，因此部分遮罩的 latent 會失去其遮罩。此網路會以時間切片執行其 3D 卷積，讓長片段使用的記憶體維持在接近單一時間切片的用量。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `LATENT` | 調整尺寸後的 latent，可直接供 H3 VAE 解碼使用。 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MiniMaxH3LatentUpscaleWithModel/zh-TW.md)

---
**Source fingerprint (SHA-256):** `cd659baace5a21620033dd3470b854cccbada01d09545a2f61273b949c3a004b`
