# StableCascade 超解析度 ControlNet

The StableCascade_SuperResolutionControlnet 節點負責準備 Stable Cascade 超解析度處理所需的輸入。它接收輸入影像，並使用 VAE 將其編碼以產生 controlnet 輸入，同時為 Stable Cascade 流程的 stage C 與 stage B 產生佔位潛在表示。

## 輸入

| 參數 | 說明 | 資料型態 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `image` | 要進行超解析度處理的輸入影像 | IMAGE | 是 | - |
| `vae` | 用於對輸入影像進行編碼的 VAE 模型 | VAE | 是 | - |

注意：使用 VAE 進行編碼時，僅使用輸入影像的前三個色彩通道。

## 輸出

| 輸出名稱 | 說明 | 資料型態 |
| --- | --- | --- |
| `controlnet_input` | 適合用作 controlnet 輸入的編碼影像表示 | IMAGE |
| `stage_c` | Stable Cascade 處理中 stage C 的佔位潛在表示，其尺寸依據輸入影像大小除以 16 計算 | LATENT |
| `stage_b` | Stable Cascade 處理中 stage B 的佔位潛在表示，其尺寸依據輸入影像大小除以 2 計算 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_SuperResolutionControlnet/zh-TW.md)

---
**Source fingerprint (SHA-256):** `d9eff373ac7736f2e2f9788d1b43c04bb3212422aa1703d1d58ac512ce476925`
