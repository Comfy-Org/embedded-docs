> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SetClipHooks/zh-TW.md)

## 概述

SetClipHooks 節點允許您將自訂鉤子（hooks）套用至 CLIP 模型，從而實現對其行為的高階修改。它可以將鉤子套用至條件化輸出，並可選擇啟用 CLIP 排程功能。此節點會建立輸入 CLIP 模型的克隆副本，並套用指定的鉤子配置。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `clip` | CLIP | 是 | - | 要套用鉤子的 CLIP 模型 |
| `apply_to_conds` | BOOLEAN | 是 | - | 是否將鉤子套用至條件化輸出（預設：True） |
| `schedule_clip` | BOOLEAN | 是 | - | 是否啟用 CLIP 排程功能（預設：False） |
| `hooks` | HOOKS | 否 | - | 可選的鉤子群組，用於套用至 CLIP 模型 |

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `clip` | CLIP | 已套用指定鉤子的 CLIP 模型克隆副本 |

---
**Source fingerprint (SHA-256):** `904a878638c015bdce1983ae0c11a2b580b271090fca39edb304f6ed90c8c66d`
