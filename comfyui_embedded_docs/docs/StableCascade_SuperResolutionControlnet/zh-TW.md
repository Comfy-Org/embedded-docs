# StableCascade 超解析度 ControlNet

此節點屬於實驗性的 Stable Cascade 群組。它透過使用 VAE 編碼輸入影像以建立 controlnet 輸入，並為 Stable Cascade 管線的 stage C 與 stage B 產生空白（填零）的潛在佔位符，來準備 Stable Cascade 超解析度處理所需的輸入。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `影像` | 要進行超解析度處理的輸入影像。僅使用影像的前 3 個色彩通道（RGB）進行編碼。 | IMAGE | 是 | - |
| `vae` | 用於編碼輸入影像的 VAE 模型 | VAE | 是 | - |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `controlnet_input` | 適合做為 controlnet 輸入的 VAE 編碼影像表徵 | IMAGE |
| `stage_c` | Stable Cascade 處理 stage C 的佔位（填零）潛在表徵，具有 16 個通道，尺寸基於輸入影像大小除以 16 | LATENT |
| `stage_b` | Stable Cascade 處理 stage B 的佔位（填零）潛在表徵，具有 4 個通道，尺寸基於輸入影像大小除以 2 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_SuperResolutionControlnet/zh-TW.md)

---
**Source fingerprint (SHA-256):** `d9eff373ac7736f2e2f9788d1b43c04bb3212422aa1703d1d58ac512ce476925`
