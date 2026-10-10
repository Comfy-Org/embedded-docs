# Vidu Q4 Image-to-Video Generation

使用 Vidu Q4 模型，從起始影格與可選提示詞生成影片。輸出的畫面會保持輸入影像的長寬比。

選擇 `model` 會顯示該模型專屬的參數。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `image` | 生成影片的起始影格。長寬比必須介於 1:5 與 5:1 之間。 | IMAGE | 是 | N/A |
| `model` | 用於影片生成的模型。選擇模型後會顯示其專屬參數：`prompt`、`resolution`、`duration`、`audio` 和 `seed`。 | DYNAMIC_COMBO | 是 | `"Vidu Q4 Preview"` |
| `prompt` | 用於影片生成的可選文字提示詞，最多 5000 個字元（預設：空）。 | STRING | 是 | 任意文字 |
| `resolution` | 輸出影片的解析度（預設：`"720p"`）。 | COMBO | 是 | `"540p"`<br>`"720p"`<br>`"1080p"`<br>`"2K"`<br>`"4K"` |
| `duration` | 輸出影片的長度，以秒為單位（預設：5）。 | INT | 是 | 3 至 16 |
| `audio` | 啟用時，輸出含聲音的影片，包括對話與音效（預設：True）。 | BOOLEAN | 是 | `True`<br>`False` |
| `seed` | `seed` 控制節點是否應重新執行；無論 `seed` 為何，結果都是非確定性的。此參數具有「生成後控制」功能（預設：42）。 | INT | 是 | 1 至 2147483647 |

**注意：** `image` 的長寬比必須維持在 1:5 與 5:1 之間，且 `prompt` 不得超過 5000 個字元。結果會保持輸入影像的長寬比，因此輸出尺寸只會在此比例範圍內遵循 `resolution` 設定。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `VIDEO` | 生成的影片檔案。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu4ImageToVideoNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `8778696edbdfb821afaa99dcba09cbebff57fd4cd2378273e82ad9fb18600b62`
