# KlingSingleImageVideoEffectNode

Kling Single Image Video Effect Node 會根據單一參考圖片建立具有不同特殊效果的影片。它會套用各種視覺效果和場景，將靜態圖片轉換為動態影片內容。此節點支援不同的特效場景、模型選項和影片時長，以達到所需的視覺效果。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `image` | 參考圖片。URL 或 Base64 編碼字串（不含 data:image 前綴）。檔案大小不能超過 10MB，解析度不得小於 300x300px，長寬比需介於 1:2.5 至 2.5:1 之間 | IMAGE | 是 | - |
| `effect_scene` | 要套用於影片生成的特效場景類型。部分特效可能會有不同的定價。 | COMBO | 是 | `"dizzydizzy"`<br>`"bloombloom"`<br>`"neon"`<br>`"cartoon"`<br>`"sketch"`<br>`"oil"`<br>`"watercolor"`<br>`"3d"` |
| `model_name` | 用於生成影片特效的特定模型版本。 | COMBO | 是 | `"kling-v1-5"`<br>`"kling-v1-6"` |
| `duration` | 生成影片的長度，以秒為單位。 | COMBO | 是 | `"5"`<br>`"10"` |

**注意：** `effect_scene` 參數會影響此節點的定價。特效 `dizzydizzy` 和 `bloombloom` 每次生成費用為 $0.49 USD，而所有其他特效每次生成費用為 $0.28 USD。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `output` | 已套用特效的生成影片 | VIDEO |
| `video_id` | 生成影片的唯一識別碼 | STRING |
| `duration` | 生成影片的長度 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingSingleImageVideoEffectNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `fb4a8b044daa99154a58d6926ff746bd2397b71ea32f1fafc851589f163ab51a`
