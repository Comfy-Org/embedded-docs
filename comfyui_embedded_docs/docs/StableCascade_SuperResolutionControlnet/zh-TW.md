# StableCascade 超解析度 ControlNet

## 概述

StableCascade_SuperResolutionControlnet 節點用於準備 Stable Cascade 超解析度處理的輸入。它接收輸入影像，並使用 VAE 對其進行編碼以建立 controlnet 輸入，同時也為 Stable Cascade 管線的階段 C 和階段 B 生成佔位潛在表示。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `影像` | 要進行超解析度處理的輸入影像 | IMAGE | 是 | - |
| `vae` | 用於編碼輸入影像的 VAE 模型 | VAE | 是 | - |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `stage_c` | 適合 controlnet 輸入的編碼影像表示 | IMAGE |
| `stage_b` | 用於 Stable Cascade 處理階段 C 的佔位潛在表示 | LATENT |
| `stage_b` | 用於 Stable Cascade 處理階段 B 的佔位潛在表示 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_SuperResolutionControlnet/zh-TW.md)

---
**Source fingerprint (SHA-256):** `78b6e5a02c48ac37a205ef9d8532a3aca19134de4ec7be98b2ee55969dab7b53`
