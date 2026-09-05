# Tripo：影像轉多視角

使用 Tripo API 從單一輸入圖片生成主體的前視圖、左視圖、後視圖和右視圖。這是一項付費任務，費用約為 0.10 美元。節點會上傳圖片、等待 Tripo 的生成任務完成，然後回傳四個視圖以及多視圖任務 ID。

## 輸入

| 參數 | 描述 | 資料類型 | 必需 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `image` | 主體的來源圖片，Tripo 會根據它生成前視圖、左視圖、後視圖和右視圖。此請求恰好使用一張圖片。 | IMAGE | 是 | Single image |

注意：節點會呼叫 Tripo 的雲端 API，並等待生成任務完成。典型任務大約需要 25 秒。驗證會透過節點的隱藏輸入自動處理，因此無需在工作流程中提供 Tripo API 金鑰。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `MULTIVIEW_TASK_ID` | Tripo 針對多視圖圖片生成請求所回傳的工作任務識別碼。這是一個字串識別碼，可用來參照已完成的任務。 | MULTIVIEW_TASK_ID |
| `front` | 生成的主體前視圖。 | IMAGE |
| `left` | 生成的主體左視圖。 | IMAGE |
| `back` | 生成的主體後視圖。 | IMAGE |
| `right` | 生成的主體右視圖。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoImageToMultiviewNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `3beca1feeb88aa080330e6867ffd7076bd45b2c52471d1bfacc71f66452211a5`
