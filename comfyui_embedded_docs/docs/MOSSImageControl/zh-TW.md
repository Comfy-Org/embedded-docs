# MOSS-Image Color/Depth Control

將 MOSS-Image 色彩/深度控制適配器的色彩區域圖與深度圖加入條件（conditioning）。連接正向與負向條件、一個 VAE，以及其中一張或兩張圖：這些圖會編碼為潛在向量、合併成色彩/深度控制訊號，並附加到您所選取樣區段的條件上。請搭配透過 LoRA 載入器載入的 MOSS-Image 控制適配器使用。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `positive` | 要附加控制訊號的正向條件。 | CONDITIONING | 是 | N/A |
| `negative` | 要附加控制訊號的負向條件。 | CONDITIONING | 是 | N/A |
| `vae` | 用於將圖編碼為潛在向量的 VAE。 | VAE | 是 | N/A |
| `color_map` | 每個區域使用單一平塗色彩，尺寸為輸出尺寸。色彩僅作為區域 ID。 | IMAGE | 否 | N/A |
| `depth_map` | 輸出尺寸的深度圖，近處為白色。 | IMAGE | 否 | N/A |
| `strength` | 縮放這些圖對影像 token 的貢獻程度。0.0 等同於不使用任何圖，1.0 為訓練時的強度（預設：1.0）。 | FLOAT | 是 | 0.0 至 10.0 （步進值：0.01） |
| `start_percent` | 控制開始的取樣百分比（預設：0.0）。 | FLOAT | 是 | 0.0 至 1.0 （步進值：0.001） |
| `end_percent` | 控制結束的取樣百分比。提早結束會保留佈局與深度，而其餘取樣步數會讓形狀較為鬆散（預設：1.0）。 | FLOAT | 是 | 0.0 至 1.0 （步進值：0.001） |

**注意：** 請至少連接 `color_map` 與 `depth_map` 其中之一；若兩者皆未連接，節點會將條件原樣傳回。缺少的圖會以零值取代，因此僅有色彩圖或僅有深度圖的設定皆可運作。當兩張圖尺寸不同時，較小的一張會放大至另一張的尺寸。此節點在 ComfyUI 中標示為實驗性功能。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `positive` | 已附加控制訊號的正向條件。 | CONDITIONING |
| `negative` | 已附加控制訊號的負向條件。 | CONDITIONING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MOSSImageControl/zh-TW.md)

---
**Source fingerprint (SHA-256):** `c4a40c76f26237408e47cb9f683c13bccc3507bd775bec1b89919947a308c115`
