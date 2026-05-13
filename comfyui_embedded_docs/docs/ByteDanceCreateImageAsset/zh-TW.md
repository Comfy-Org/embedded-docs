> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceCreateImageAsset/zh-TW.md)

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | 是 | | 要註冊為個人資產的圖像。 |
| `group_id` | STRING | 否 | | 重複使用現有的 Seedance 資產群組 ID，以跳過對同一人物的重複人體驗證。留空則在瀏覽器中執行真實人物驗證並建立新群組（預設：空值）。 |

**圖像限制：**
*   圖像寬度必須在 300 到 6000 像素之間。
*   圖像高度必須在 300 到 6000 像素之間。
*   圖像長寬比必須在 0.4:1 到 2.5:1 之間。

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `group_id` | STRING | 新建立的圖像資產的唯一識別碼。 |
| `group_id` | STRING | 資產群組的識別碼。這將是提供的 `group_id` 或新建立的群組 ID。 |

---
**Source fingerprint (SHA-256):** `b8b7b4cbbc16a8bb0102982757496ad4e8140bd87155902668c0be0d8b4d3d98`
