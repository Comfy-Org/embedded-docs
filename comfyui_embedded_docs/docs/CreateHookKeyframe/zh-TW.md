> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateHookKeyframe/zh-TW.md)

Create Hook Keyframe 節點允許您在生成過程中定義特定的行為切換點。它會建立關鍵幀，在生成進度的特定百分比處修改掛鉤的強度，這些關鍵幀可以串聯起來以建立複雜的排程模式。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 參數說明 |
|-----------|-----------|----------|-------|-------------|
| `strength_mult` | FLOAT | 是 | -20.0 至 20.0 | 此關鍵幀處的掛鉤強度乘數 (預設值: 1.0) |
| `start_percent` | FLOAT | 是 | 0.0 至 1.0 | 此關鍵幀在生成過程中生效的百分比點 (預設值: 0.0) |
| `prev_hook_kf` | HOOK_KEYFRAMES | 否 | - | 可選的先前掛鉤關鍵幀群組，用於將此關鍵幀加入其中 |

## 輸出結果

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `HOOK_KF` | HOOK_KEYFRAMES | 包含新建立關鍵幀的一組掛鉤關鍵幀 |