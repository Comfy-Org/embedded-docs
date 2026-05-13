> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Rodin3D_Sketch/zh-TW.md)

此節點使用 Rodin API 生成 3D 資產。它接收輸入圖像，並透過外部服務將其轉換為 3D 模型。該節點處理從任務建立到下載最終 3D 模型檔案的完整流程。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `Images` | IMAGE | 是 | - | 要轉換為 3D 模型的輸入圖像。可提供多張圖像。 |
| `Seed` | INT | 否 | 0-65535 | 用於生成的隨機種子值（預設值：0）。設為 0 則使用隨機種子。 |

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `3D Model Path` | STRING | 生成的 3D 模型檔案路徑（僅為向後相容性保留） |
| `GLB` | FILE3DGLB | 以 GLB 格式生成的 3D 模型 |

---
**Source fingerprint (SHA-256):** `d3bc71e6a44c11cbeff25351d561e99a7f09ed8ce3544d2968a873b6796512da`
