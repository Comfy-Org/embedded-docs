# Reve 圖像編輯

Reve Image Edit 節點允許您根據文字描述修改現有圖片。它使用 Reve API 來解讀您的指示，並將要求的變更套用到您提供的圖片上。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `圖像` | 要編輯的圖片。 | IMAGE | 是 | - |
| `編輯指令` | 如何編輯圖片的文字描述。最多 2560 個字元。 | STRING | 是 | - |
| `模型` | 用於編輯的模型版本。 | MODEL | 是 | `"reve-edit@20250915"`<br>`"reve-edit-fast@20251030"` |
| `model.aspect_ratio` | 編輯後圖片的長寬比。設定為 "auto" 時，長寬比會自動決定。 | COMBO | 否 | `"auto"`<br>`"16:9"`<br>`"9:16"`<br>`"3:2"`<br>`"2:3"`<br>`"4:3"`<br>`"3:4"`<br>`"1:1"` |
| `model.test_time_scaling` | 模型的測試時間縮放因子。較高的值可能會改善品質，但會增加處理時間。 | FLOAT | 否 | - |
| `放大` | 控制是否對生成的圖片進行放大。 | COMBO | 否 | `"disabled"`<br>`"enabled"` |
| `upscale.upscale_factor` | 啟用放大時，圖片的放大倍數。 | FLOAT | 否 | - |
| `去背` | 控制是否移除生成圖片的背景。 | BOOLEAN | 否 | - |
| `種子` | 種子碼控制節點是否應重新執行；無論種子碼為何，結果皆非確定性。（預設值：0） | INT | 否 | 0 到 2147483647 |

**注意：** `upscale.upscale_factor` 參數僅在 `upscale` 參數設定為 `"enabled"` 時才有作用。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `圖像` | 根據指示生成的編輯後圖片。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReveImageEditNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `0a9504ae5e8b7216d309fe3ba95c014da32eadbf11cfc5701247ba5973dd98be`
