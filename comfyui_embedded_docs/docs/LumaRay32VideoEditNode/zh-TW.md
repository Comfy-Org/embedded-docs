# LumaRay32VideoEditNode

此節點使用 Luma Ray 3.2 根據新的提示詞重新渲染現有影片，讓您能夠在保留原始動態的同時重新調整風格、重新打光、新增或移除元素。來源影片最長可達 18 秒，編輯後的影片將保留來源的原始長度。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `影片` | 要編輯的來源影片。最長 18 秒。 | VIDEO | 是 | - |
| `提示詞` | 描述所需的編輯內容。 | STRING | 是 | - |
| `解析度` | 編輯後影片的輸出解析度。 | COMBO | 是 | `"360p"`<br>`"540p"`<br>`"720p"`<br>`"1080p"` |
| `強度` | 保留原始內容與重新想像來源內容的強度。"auto" 讓 Ray 3.2 自行選擇；adhere_* 保留最多原始內容，flex_* 較為平衡，reimagine_* 變動最大。（預設值："auto"） | COMBO | 是 | `"auto"`<br>`"adhere_1"`<br>`"adhere_2"`<br>`"adhere_3"`<br>`"flex_1"`<br>`"flex_2"`<br>`"flex_3"`<br>`"reimagine_1"`<br>`"reimagine_2"`<br>`"reimagine_3"` |
| `種子` | 用於再現結果的隨機種子。 | INT | 是 | - |

**注意：** `prompt` 必須介於 1 到 6000 個字元之間。來源影片的長度不得超過 18 秒。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `generation_id` | 編輯後的影片輸出。 | VIDEO |
| `generation_id` | 生成請求的唯一識別碼。 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaRay32VideoEditNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `936d9d7da3fdee9b0b468781fd470751db01f772f3c5c20582da7fb1ff85e6e6`
