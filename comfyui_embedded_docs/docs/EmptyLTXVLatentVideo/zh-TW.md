# EmptyLTXVLatentVideo

EmptyLTXVLatentVideo 節點會建立一個用於影片生成的空白潛在張量。它會產生一個以指定寬度、高度、長度與批次大小填充零的潛在表示，可作為 LTXV 影片工作流程的起點。潛在表示以壓縮形式儲存影片：空間維度會除以 32，幀數則減少 8 倍。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `width` | 潛在影片的寬度（像素）（預設值：768，步長：32） | INT | 是 | 64 to MAX_RESOLUTION |
| `height` | 潛在影片的高度（像素）（預設值：512，步長：32） | INT | 是 | 64 to MAX_RESOLUTION |
| `length` | 潛在影片的幀數（預設值：97，步長：8） | INT | 是 | 1 to MAX_RESOLUTION |
| `batch_size` | 批次中要生成的潛在影片數量（預設值：1） | INT | 否 | 1 to 4096 |

## 輸出

| 輸出名 | 描述 | 資料類型 |
| --- | --- | --- |
| `samples` | 生成的空白潛在張量，以零填充。該潛在張量還帶有一個 `downscale_ratio_spacial` 值 32，描述套用於寬度和高度的空間縮小比例。 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyLTXVLatentVideo/zh-TW.md)

---
**Source fingerprint (SHA-256):** `0b1e57baf9730d852b03b6bccbb8a033e2be9b9cd2420a0aa3638c31f6d3cd26`
