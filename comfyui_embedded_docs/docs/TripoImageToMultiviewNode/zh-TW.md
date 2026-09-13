# Tripo：影像轉多視角

使用 Tripo API 從單一輸入影像生成主體的正面、左側、背面與右側視圖。影像會上傳，多視圖生成任務會啟動並持續輪詢直到完成，最後一併傳回四個生成的視圖與任務 ID。此為付費任務，費用約為 0.10 USD。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `image` | 主體的來源影像，Tripo 會據此生成正面、左側、背面與右側視圖。即使提供批次，請求也只會使用一張影像。 | IMAGE | 是 | Single image |

注意：此節點會呼叫 Tripo 的雲端 API，並等待生成任務完成。典型任務約需 25 秒。驗證會透過節點的隱藏輸入自動處理，因此工作流程中不需要提供 Tripo API key。此節點要求 Tripo 回應中必須包含全部四個視圖 URL（`front_view_url`、`left_view_url`、`back_view_url`、`right_view_url`）；若缺少任何一個視圖，執行就會失敗並產生錯誤。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `multiview task_id` | Tripo 針對多視圖影像生成請求所傳回的任務識別碼。可用來參照已完成的任務，例如使用 Tripo: Edit Multiview 調整視圖時。 | MULTIVIEW_TASK_ID |
| `front` | 生成的主體正面視圖。 | IMAGE |
| `left` | 生成的主體左側視圖。 | IMAGE |
| `back` | 生成的主體背面視圖。 | IMAGE |
| `right` | 生成的主體右側視圖。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoImageToMultiviewNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `7e96d327940f1f09a3e84031c773c1439380f20afae49c79fd4350fcf0aba5da`
