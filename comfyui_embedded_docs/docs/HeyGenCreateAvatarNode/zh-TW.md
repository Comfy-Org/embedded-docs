# HeyGenCreateAvatarNode

從人物照片或描述角色的文字提示建立可重複使用的 HeyGen 頭像。產生的頭像 ID 可與 HeyGen 頭像影片節點搭配使用，建立以該頭像為特色的影片。

## 輸入
| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `source` | 從文字提示產生新角色，或從連接的人物照片建立頭像。 | COMBO | 是 | `"prompt"`<br>`"photo"` |

當 `source` 設定為 `"prompt"` 時，以下額外參數將可用：

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 要產生的頭像描述（最多 1000 個字元）。 | STRING | 是 | 1 到 1000 個字元 |
| `reference_images` | 最多 3 張引導產生外觀的參考圖片。 | IMAGE | 否 | 0 到 3 張圖片 |

當 `source` 設定為 `"photo"` 時，以下額外參數將可用：

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `identity_photo` | 要轉換為頭像的人物照片。若大於 2K 會自動縮小。 | IMAGE | 是 | 單張圖片 |

**注意：** `source` 參數可在兩種模式之間切換。在 `"prompt"` 模式下，您提供文字描述並可選擇提供最多 3 張參考圖片。在 `"photo"` 模式下，您提供單張人物照片。這兩種模式互斥。

## 輸出
| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `avatar_id` | 頭像外觀 ID。將其傳遞給 HeyGen 頭像影片的 `custom_avatar_id`；儲存以便日後重複使用該頭像。 | STRING |
| `preview` | 所產生頭像的預覽圖片。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenCreateAvatarNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `c60e9cdb0d91fb5ec6ea83b503b9aa10c978ce065a16c751a52e90c12e70a5e2`
