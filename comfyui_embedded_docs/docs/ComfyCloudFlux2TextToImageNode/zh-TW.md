# ComfyCloudFlux2TextToImageNode

在 Comfy Cloud GPU 上執行 Flux 2 dev 文字轉圖片模型，並回傳生成的圖片。`turbo` 選項會以短排程套用 Turbo LoRA，以少許保真度換取更快的執行速度；關閉此選項則會執行完整的 dev 流程，且不套用 LoRA。這是一組 Beta 節點，會依執行時間以點數計費。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|------|-------|
| `prompt` | 描述要生成之圖片的文字提示。提交前會移除前後空白字元。 | STRING | 是 | 1 至 4096 個字元 |
| `seed` | 用於控制生成結果以具備可重現性的隨機種子（預設值：42）。 | INT | 是 | 0 至 18446744073709551615 |
| `aspect_ratio` | 輸出圖片的長寬比（預設值："1:1"）。 | COMBO | 是 | "1:1"<br>"3:4"<br>"2:3"<br>"3:2"<br>"4:3"<br>"16:9"<br>"9:16"<br>"21:9" |
| `megapixels` | 總像素預算。在方形比例下，1.0 約為 1024x1024（預設值：1.0）。 | FLOAT | 是 | 0.1 至 16.0（步進 0.1） |
| `turbo` | 以短排程執行 Turbo LoRA，用少許保真度換取更快的執行時間。關閉時則會執行完整的 dev 流程，且不套用 LoRA（預設值：True）。 | BOOLEAN | 是 | True / False |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `IMAGE` | 從文字提示生成的圖片，以可傳遞至其他節點的 ComfyUI 圖片張量形式回傳。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyCloudFlux2TextToImageNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `1b51a8ab89ae7c355dec4256a1a25a09a15e192c72fc8d1862c652dbdf337fcb`
