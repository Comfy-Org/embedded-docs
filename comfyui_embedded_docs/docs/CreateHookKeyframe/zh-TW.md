# 建立 Hook 關鍵影格

建立鉤子關鍵影格節點可讓您在生成過程中定義鉤子行為變化的特定點。它會建立關鍵影格，在生成進度的特定百分比處修改鉤子的強度，並且這些關鍵影格可以鏈接在一起，以建立複雜的排程模式。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `strength_mult` | 此關鍵影格處鉤子強度的乘數（預設值：1.0） | FLOAT | 是 | -20.0 至 20.0 |
| `start_percent` | 此關鍵影格在生成過程中生效的百分比點（預設值：0.0） | FLOAT | 是 | 0.0 至 1.0 |
| `prev_hook_kf` | 可選的先前鉤子關鍵影格群組，用於將此關鍵影格加入其中 | HOOK_KEYFRAMES | 否 | - |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `HOOK_KF` | 包含新建立關鍵影格在內的一組鉤子關鍵影格 | HOOK_KEYFRAMES |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateHookKeyframe/zh-TW.md)

---
**Source fingerprint (SHA-256):** `51893311a0623cafcf8c2d8af00e4005ca2fea2df9474e87d7d4b332b38435c3`
