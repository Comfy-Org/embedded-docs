> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SetClipHooks/zh-TW.md)

SetClipHooks 節點允許您對 CLIP 模型應用自定義掛鉤，從而實現對其行為的高級修改。它可以將掛鉤應用於條件輸出，並可選擇啟用 CLIP 排程功能。此節點會建立輸入 CLIP 模型的克隆副本，並應用指定的掛鉤配置。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 參數說明 |
|-----------|-----------|----------|-------|-------------|
| `clip` | CLIP | 是 | - | 要應用掛鉤的 CLIP 模型 |
| `apply_to_conds` | BOOLEAN | 是 | - | 是否對條件輸出應用掛鉤（預設值：True） |
| `schedule_clip` | BOOLEAN | 是 | - | 是否啟用 CLIP 排程功能（預設值：False） |
| `hooks` | HOOKS | 否 | - | 可選的掛鉤群組，將應用於 CLIP 模型 |

## 輸出結果

| 輸出名稱 | 資料類型 | 輸出說明 |
|-------------|-----------|-------------|
| `clip` | CLIP | 已應用指定掛鉤的克隆 CLIP 模型 |