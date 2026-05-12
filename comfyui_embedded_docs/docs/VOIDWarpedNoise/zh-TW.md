> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDWarpedNoise/zh-TW.md)

## 概述

為 VOID 影片精煉流程的第二階段生成時間相關的噪聲。它接收來自第一階段的輸出影片，並沿著光流向量扭曲高斯噪聲，創建與影片內容一致移動的噪聲。此扭曲噪聲用作第二階段的起始潛在表示，以改善最終輸出中的時間一致性。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `optical_flow` | MODEL | 是 | - | 來自 OpticalFlowLoader（RAFT-large）的光流模型。 |
| `video` | IMAGE | 是 | - | 第一階段輸出影片幀 [T, H, W, 3]。 |
| `width` | INT | 是 | 16 至 MAX_RESOLUTION（步長 8） | 輸出潛在表示的寬度（預設值：672）。 |
| `height` | INT | 是 | 16 至 MAX_RESOLUTION（步長 8） | 輸出潛在表示的高度（預設值：384）。 |
| `length` | INT | 是 | 1 至 MAX_RESOLUTION（步長 1） | 像素幀數。向下取整以使 `latent_t` 為偶數（`patch_size_t=2` 要求），例如 49 → 45（預設值：45）。 |
| `batch_size` | INT | 是 | 1 至 64 | 要生成的相同噪聲序列數量（預設值：1）。 |

**關於 `length` 參數的說明：** `length` 值會自動向下取整到最接近的有效值，以產生偶數的 `latent_t` 維度。這是 CogVideoX-Fun-V1.5 模型的 `patch_size_t=2` 約束所要求的。當發生取整時，會記錄一條警告訊息。

## 輸出

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `warped_noise` | LATENT | 一個 5D 張量 (B, C, T, H, W)，包含經光流扭曲的高斯噪聲，可直接用作 VOID 第二階段的初始潛在表示。 |