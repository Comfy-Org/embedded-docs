# StableCascade 超解析度 ControlNet

StableCascade_SuperResolutionControlnet 節點為 Stable Cascade 超解析度處理準備輸入。它接收輸入影像，並使用 VAE 對其進行編碼以建立 controlnet 輸入，同時為 Stable Cascade 管線的 stage C 與 stage B 生成佔位潛在表示。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `影像` | 要進行超解析度處理的輸入影像。僅使用影像的前 3 個顏色通道（RGB）進行編碼。 | IMAGE | 是 | - |
| `vae` | 用於編碼輸入影像的 VAE 模型 | VAE | 是 | - |

## 輸出

| 輸出名 | 描述 | 資料類型 |
| --- | --- | --- |
| `controlnet_input` | 適合 controlnet 輸入的 VAE 編碼影像表示 | IMAGE |
| `stage_c` | 用於 Stable Cascade 處理 stage C 的佔位（零填充）潛在表示，具有 16 個通道，維度基於輸入影像尺寸除以 16 | LATENT |
| `stage_b` | 用於 Stable Cascade 處理 stage B 的佔位（零填充）潛在表示，具有 4 個通道，維度基於輸入影像尺寸除以 2 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_SuperResolutionControlnet/zh-TW.md)

---
**Source fingerprint (SHA-256):** `d9eff373ac7736f2e2f9788d1b43c04bb3212422aa1703d1d58ac512ce476925`
