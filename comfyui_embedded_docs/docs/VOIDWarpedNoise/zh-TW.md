# VOIDWarpedNoise

## 概述

為 VOID 影片精煉流程的第二階段生成時間相關的噪聲。它接收來自第一階段的輸出影片，並沿著光流向量扭曲高斯噪聲，創建與影片內容一致移動的噪聲。此扭曲噪聲用作第二階段的起始潛在表示，以改善最終輸出中的時間一致性。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `optical_flow` | 來自 OpticalFlowLoader（RAFT-large）的光流模型。 | MODEL | 是 | - |
| `video` | 第一階段輸出影片幀 [T, H, W, 3]。 | IMAGE | 是 | - |
| `width` | 輸出潛在表示的寬度（預設值：672）。 | INT | 是 | 16 至 MAX_RESOLUTION（步長 8） |
| `height` | 輸出潛在表示的高度（預設值：384）。 | INT | 是 | 16 至 MAX_RESOLUTION（步長 8） |
| `length` | 像素幀數。向下取整以使 `latent_t` 為偶數（`patch_size_t=2` 要求），例如 49 → 45（預設值：45）。 | INT | 是 | 1 至 MAX_RESOLUTION（步長 1） |
| `batch_size` | 要生成的相同噪聲序列數量（預設值：1）。 | INT | 是 | 1 至 64 |

**關於 `length` 參數的說明：** `length` 值會自動向下取整到最接近的有效值，以產生偶數的 `latent_t` 維度。這是 CogVideoX-Fun-V1.5 模型的 `patch_size_t=2` 約束所要求的。當發生取整時，會記錄一條警告訊息。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `warped_noise` | 一個包含光流扭曲高斯噪聲的 5D 張量（B, C, T, H, W），準備用作 VOID 第二階段的初始潛在表示。 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDWarpedNoise/zh-TW.md)

---
**Source fingerprint (SHA-256):** `a0f986e54bcc6c455220f89f5d840585a9eae081e522ea11e0ce37ab46821bd9`
