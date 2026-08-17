# ARVideoI2V

## 概述

此節點為 AR（自迴歸）視訊模型準備影像轉視訊的生成設定。它接收一張起始影像，使用 VAE 將其編碼到潛在空間，並將編碼後的影像儲存在模型的配置中。這樣一來，視訊取樣流程就能以該影像作為第一幀，從而在無需獨立影像轉視訊模型架構的情況下初始化生成過程。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 用於生成任務的 AR 視訊模型。 | MODEL | 是 | - |
| `vae` | 用於將起始影像編碼到潛在空間的 VAE 模型。 | VAE | 是 | - |
| `start_image` | 作為生成視訊第一幀的初始影像。 | IMAGE | 是 | - |
| `width` | 生成視訊幀的寬度（預設值：832）。 | INT | 是 | 16 to 8192 (step: 16) |
| `height` | 生成視訊幀的高度（預設值：480）。 | INT | 是 | 16 to 8192 (step: 16) |
| `length` | 生成視訊的總幀數（預設值：81）。 | INT | 是 | 1 to 1024 (step: 4) |
| `batch_size` | 單一批次中要生成的視訊序列數量（預設值：1）。 | INT | 是 | 1 to 64 |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `MODEL` | 已克隆的模型，其配置中儲存了編碼後的起始影像，可用於視訊生成。 | MODEL |
| `LATENT` | 一個空的潛在張量，形狀為 [batch_size, 16, lat_t, height/8, width/8]，其中 lat_t = ((length - 1) // 4) + 1 是根據所需視訊長度推導出的潛在幀數。 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ARVideoI2V/zh-TW.md)

---
**Source fingerprint (SHA-256):** `984834951b9d5a22aef51c85a5019fd8ba58cdb2d6fff235371ed29f316896d8`
