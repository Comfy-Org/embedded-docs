# Clarity AI Crystal Video Upscale

使用 Clarity AI 的 Crystal Video Upscaler 放大影片；這是一款高保真放大器，能忠實保留來源內容。上傳片段後，會依你設定的倍率進行放大，並以影片形式返回。輸出限制為每幀 9 百萬像素（例如 4000x2250），且每個片段限制為 360 百萬像素秒，因此大型或較長的片段返回時，解析度會低於所要求倍率。

選擇 `model` 會顯示該模型專屬的參數。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | 要使用的模型。選擇模型會顯示其專屬參數：`video` 和 `scale_factor`。 | DYNAMIC_COMBO | 是 | `"crystal-video-upscaler"` |
| `video` | 要放大的影片。 | VIDEO | 是 | N/A |
| `scale_factor` | 將影片寬度和高度相乘的倍率。輸出限制為每幀 9 百萬像素及每個片段 360 百萬像素秒，因此大型或較長的影片會以較小的幅度放大；當該倍率會使任一側超過 5120 像素時，倍率會再降低（預設值：2.0）。 | FLOAT | 是 | 1.0 至 200.0 （步進值：0.1） |

**注意：** 片段每一側最多可為 5120 像素，且每幀最多為 9 百萬像素。最大長度取決於畫面尺寸與幀率：以 360 百萬像素秒除以每幀像素數，再除以向上取整至 30 fps 倍數的幀率，因此 1080p、30 fps 的片段最長可達約 173 秒。高於 30 fps 的片段以 2 倍計算，高於 60 fps 以 3 倍計算，依此類推。

## 輸出

| 輸出名 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `video` | 放大後的影片。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ClarityCrystalVideoUpscaleNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `ca44ed6591474421edaf7e4e99e6da62e0c2e4e66964b7dac51d45758150aaa8`
