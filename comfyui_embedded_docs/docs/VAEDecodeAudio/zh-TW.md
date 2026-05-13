> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEDecodeAudio/zh-TW.md)

## 概述

VAEDecodeAudio 節點使用變分自編碼器（Variational Autoencoder）將潛在空間表示轉換回音訊波形。它接收編碼後的音訊樣本，透過 VAE 進行處理以重建原始音訊，並應用歸一化來確保一致的輸出電平。最終輸出的音訊採用 44100 Hz 的標準取樣率。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `samples` | LATENT | 是 | - | 潛在空間中的編碼音訊樣本，將被解碼回音訊波形 |
| `vae` | VAE | 是 | - | 用於將潛在樣本解碼為音訊的變分自編碼器模型 |

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `AUDIO` | AUDIO | 解碼後的音訊波形，具有歸一化音量及 44100 Hz 取樣率 |

---
**Source fingerprint (SHA-256):** `15848d3763324cbae986949146d57352c68369713cd99a27d216797560836824`
