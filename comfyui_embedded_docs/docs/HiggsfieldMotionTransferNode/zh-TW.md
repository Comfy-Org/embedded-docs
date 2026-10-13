# Higgsfield Genjutsu Motion Transfer

**Higgsfield Genjutsu Motion Transfer** 節點會使用取自參考圖像的新角色、地點或風格來重新演繹影片，同時保留來源片段的動作、攝影機運鏡、時間節奏與音訊。連接要重新風格的片段，以及一張或多張描述新外觀的參考圖像，然後在 `prompt` 中描述結果。請求會傳送至 Higgsfield API，並回傳生成的影片。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | 要使用的模型。選取模型後會顯示其專屬參數：`video`、`reference_images`、`prompt`、`resolution` 和 `seed`。 | DYNAMIC_COMBO | 是 | `"genjutsu-v1.0"` |
| `video` | 來源影片，其動作、攝影機運鏡、時間節奏與音訊都會保留。至少 4 秒；只會使用前 30 秒。 | VIDEO | 是 | 4 至 30 秒 |
| `reference_images` | 可增長的插槽：連接 1 到 8 張要使用的角色、地點或風格圖像（`image_1`、`image_2`、...）。批次輸入會依每張圖像各計一次。 | IMAGE | 是 | 1 至 8 張影像 |
| `prompt` | 選填。描述結果，例如哪個參考圖像取代哪個人，或新的場景設定。（預設值：空） | STRING | 是 | 任意文字 |
| `resolution` | 輸出影片的解析度。（預設值：`"720p"`） | COMBO | 是 | `"480p"`<br>`"720p"`<br>`"1080p"` |
| `seed` | `seed` 控制節點是否應重新執行；無論 `seed` 為何，結果都不是確定性的。此參數具有「生成後控制」功能（預設值：42）。 | INT | 是 | 0 至 2147483647 |

來源影片會在傳送請求前進行驗證：短於 4 秒的片段會被拒絕，長於 30 秒的片段會被修剪為前 30 秒。其音訊會保留到結果中。參考圖像會先上傳，且所有已連接插槽的圖像總數不得超過 8，即使此節點提供八個插槽。Higgsfield 的內容審核可能會拒絕輸入或結果，此時會引發錯誤，而不是回傳影片。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `VIDEO` | 重新風格後的影片檔案。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HiggsfieldMotionTransferNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `f0c30fb93dd2af8d564335290fdb6ff61c38e36ab62cef9641fd1aa81cc10cd2`
