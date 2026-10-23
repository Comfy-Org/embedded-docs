# VAE 解碼

## 概述
VAEDecode 節點專門用於使用指定的變分自編碼器（VAE）將潛在表示解碼為圖像。其目的是從壓縮的數據表示中生成圖像，促進從潛在空間編碼中重建圖像。

## 輸入

| 參數 | 描述 | 資料類型 |
| --- | --- | --- |
| `samples` | 'samples' 參數代表要解碼為圖像的潛在表示。它對於解碼過程至關重要，因為它提供了用於重建圖像的壓縮數據。 | `LATENT` |
| `vae` | 'vae' 參數指定要用於將潛在表示解碼為圖像的變分自編碼器模型。它對於決定解碼機制和重建圖像的品質至關重要。 | VAE |

## 輸出

| 參數 | 描述 | 資料類型 |
| --- | --- | --- |
| `image` | 輸出是使用指定的 VAE 模型從提供的潛在表示重建的圖像。 | `IMAGE` |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEDecode/zh-TW.md)
