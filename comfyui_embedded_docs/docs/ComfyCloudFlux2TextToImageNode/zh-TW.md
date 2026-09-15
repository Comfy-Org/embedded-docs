# Comfy Cloud Flux 2 文字轉影像 [測試版]

在 Comfy Cloud GPU 上執行 Flux 2 dev 文字轉圖像模型，並回傳生成的圖像。`turbo` 選項會以簡短排程套用 Turbo LoRA，大幅加快執行速度，但會稍微犧牲保真度；關閉此選項則會執行完整的 dev 流程，且不使用 LoRA。這是一組 beta 節點集，會依執行時間以 credits 計費。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `提示詞` | 描述要生成之圖像的文字提示。提交前會移除開頭與結尾的空白字元。 | STRING | 是 | 1 到 4096 個字元 |
| `種子` | 用於控制生成結果以確保可重現性的隨機種子（預設：42）。 | INT | 是 | 0 到 18446744073709551615 |
| `長寬比` | 輸出圖像的長寬比（預設："1:1"）。 | COMBO | 是 | "1:1"<br>"3:4"<br>"2:3"<br>"3:2"<br>"4:3"<br>"16:9"<br>"9:16"<br>"21:9" |
| `百萬像素` | 總像素預算。在正方形比例下，1.0 約為 1024x1024（預設：1.0）。 | FLOAT | 是 | 0.1 到 16.0（步長 0.1） |
| `Turbo` | 以簡短排程執行 Turbo LoRA，稍微犧牲保真度以換取更快的執行速度。關閉時會執行完整 dev 流程，且不使用 LoRA（預設：True）。 | BOOLEAN | 是 | True / False |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `IMAGE` | 由文字提示生成的圖像，會以 ComfyUI 圖像張量形式回傳，可傳遞給其他節點。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyCloudFlux2TextToImageNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `1b51a8ab89ae7c355dec4256a1a25a09a15e192c72fc8d1862c652dbdf337fcb`
