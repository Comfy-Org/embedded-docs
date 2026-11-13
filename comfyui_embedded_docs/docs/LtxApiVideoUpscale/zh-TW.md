# LTX Video Upscale

將影片放大至 1080p、4K 或 8K，同時保持其長寬比、影格率與音訊。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `video` | 要放大的影片，短邊至少 480 像素，且無論橫向或直向，最大為 7680x4320。1080p 最多 2401 個影格，4K 最多 601 個影格，8K 最多 241 個影格。 | VIDEO | 是 | - |
| `resolution` | 輸出尺寸，會放大至可容納於 1920x1080、3840x2160 或 7680x4320 的最大尺寸；直式影片會轉向。預設：`"4k"`。 | COMBO | 是 | `"1080p"`<br>`"4k"`<br>`"8k"` |
| `seed` | 控制此節點是否重新執行；無論 `seed` 為何，結果都不具確定性。預設：42。 | INT | 否 | 0 至 4294967295 |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `video` | 放大後的影片，並保留其音訊。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LtxApiVideoUpscale/zh-TW.md)

---
**Source fingerprint (SHA-256):** `e9b3b760365568ab2f6572c5f4f28758d67c4f5795fc39716ed4f648aafef80e`
