# LTX Video AlphaGen

擷取灰階 Alpha 遮罩（前景為白色），並與輸入影片逐影格相符。將此遮罩饋送至 Get Video Components 與 Image To Mask，即可轉換成遮罩。不會保留音訊。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `video` | 要製作遮罩的影片，長度最多 10 秒，支援任一方向的 3840x2160。 | VIDEO | 是 | - |
| `seed` | 控制此節點是否重新執行；無論 `seed` 為何，結果皆不具確定性。預設：42。 | INT | 否 | 0 至 4294967295 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `matte` | 以影片形式呈現的 Alpha 遮罩，每個輸入影格對應一個影格，且不含音訊。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LtxApiVideoAlphaGen/zh-TW.md)

---
**Source fingerprint (SHA-256):** `54a8304c2d092a736ad7fb86c8497aceda6340886beb81b6068a3de5a387a746`
