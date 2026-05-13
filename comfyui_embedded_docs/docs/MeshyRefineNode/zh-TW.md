> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyRefineNode/zh-TW.md)

# Meshy：精煉草稿模型節點

Meshy：精煉草稿模型節點會取得先前生成的 3D 草稿模型，並改善其品質，可選擇性地添加紋理。它會向 Meshy API 提交精煉任務，並在處理完成後回傳最終的 3D 模型檔案。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | 是 | `"latest"` | 指定用於精煉的 AI 模型。目前僅提供 "latest" 模型。 |
| `meshy_task_id` | MESHY_TASK_ID | 是 | - | 您要精煉的草稿模型的唯一任務 ID。 |
| `enable_pbr` | BOOLEAN | 否 | - | 除了基本顏色之外，是否生成 PBR 貼圖（金屬、粗糙度、法線）。注意：使用雕刻風格時應設為 false，因為雕刻風格會生成自己的一套 PBR 貼圖。（預設值：`False`） |
| `texture_prompt` | STRING | 否 | - | 提供文字提示以引導紋理生成過程。最多 600 個字元。不能與 `texture_image` 同時使用。（預設值：空字串） |
| `texture_image` | IMAGE | 否 | - | `texture_image` 和 `texture_prompt` 兩者中只能同時使用其中一個。 |

**注意：** `texture_prompt` 和 `texture_image` 輸入是互斥的。您無法在同一個操作中同時提供文字提示和圖片來進行紋理生成。

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `model_file` | STRING | 生成的 GLB 模型檔案名稱。（僅為向後相容性保留） |
| `meshy_task_id` | MESHY_TASK_ID | 已提交精煉作業的唯一任務 ID。 |
| `GLB` | FILE3DGLB | 最終精煉後的 3D 模型，格式為 GLB。 |
| `FBX` | FILE3DFBX | 最終精煉後的 3D 模型，格式為 FBX。 |

---
**Source fingerprint (SHA-256):** `cdf620ead0a4504cbb5d5554e0fe40e4cadd08884726f147cd486e63ab37f278`
