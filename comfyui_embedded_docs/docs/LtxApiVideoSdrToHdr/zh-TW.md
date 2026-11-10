# LTX Video SDR to HDR

將 SDR 影片轉換為 BT.2020、使用 HLG 轉移函數的 10 位元 HDR 影片，並維持相同解析度。不會保留音訊。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `video` | 要轉換的 SDR 影片，無論橫向或直向，最大為 3840x2160。1080p 時最多 273 幀，1440p 時最多 193 幀，4K 時最多 65 幀。 | VIDEO | 是 | - |
| `seed` | 控制此節點是否重新執行；無論 `seed` 為何，結果皆不具確定性。預設：42。 | INT | 否 | 0 至 4294967295 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `video` | 轉換後的 10 位元 HDR 影片，不含音訊。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LtxApiVideoSdrToHdr/zh-TW.md)

---
**Source fingerprint (SHA-256):** `e5c0ef901f504a9477f042b4aef24935f4b85da52ccfaddfc764e9efec490915`
