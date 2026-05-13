> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingSingleImageVideoEffectNode/zh-TW.md)

# Kling 單圖影片特效節點

Kling 單圖影片特效節點可根據單張參考圖片，創建具有不同特殊效果的影片。它應用各種視覺效果和場景，將靜態圖片轉換為動態影片內容。此節點支援不同的特效場景、模型選項和影片時長，以達到所需的視覺效果。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | 是 | - | 參考圖片。URL 或 Base64 編碼字串（不含 data:image 前綴）。檔案大小不得超過 10MB，解析度不低於 300x300px，長寬比介於 1:2.5 至 2.5:1 之間 |
| `effect_scene` | COMBO | 是 | `"dizzydizzy"`<br>`"bloombloom"`<br>`"neon"`<br>`"cartoon"`<br>`"sketch"`<br>`"oil"`<br>`"watercolor"`<br>`"3d"` | 應用於影片生成的特殊效果場景類型。部分效果可能會有不同的定價。 |
| `model_name` | COMBO | 是 | `"kling-v1-5"`<br>`"kling-v1-6"` | 用於生成影片效果的特定模型版本。 |
| `duration` | COMBO | 是 | `"5"`<br>`"10"` | 生成影片的長度，以秒為單位。 |

**注意：** `effect_scene` 參數會影響此節點的定價。`dizzydizzy` 和 `bloombloom` 效果每次生成費用為 0.49 美元，而所有其他效果每次生成費用為 0.28 美元。

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `output` | VIDEO | 已套用效果的生成影片 |
| `video_id` | STRING | 生成影片的唯一識別碼 |
| `duration` | STRING | 生成影片的時長 |

---
**Source fingerprint (SHA-256):** `519db2f7185f200140c746bdebf89383523e0342bbfb61538adac063295d365d`
