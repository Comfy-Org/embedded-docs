# OpenAI Sora - 影片

OpenAIVideoSora2 節點使用 OpenAI 的 Sora 模型生成影片。它接收文字提示，以及可選的單張參考圖像，將請求傳送至 OpenAI，等待生成完成，然後回傳生成的影片。支援的持續時間與解析度取決於所選模型。

**棄用通知：** OpenAI 將於 2026 年 9 月停止提供 Sora v2 API。此節點屆時將從 ComfyUI 中移除。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 用於影片生成的 OpenAI Sora 模型（預設："sora-2"） | COMBO | 是 | "sora-2"<br>"sora-2-pro" |
| `prompt` | 引導文字；若有輸入圖像，則可留空（預設：空字串） | STRING | 是 | - |
| `size` | 生成影片的解析度（預設："1280x720"） | COMBO | 是 | "720x1280"<br>"1280x720"<br>"1024x1792"<br>"1792x1024" |
| `duration` | 生成影片的持續時間，以秒為單位（預設：8） | COMBO | 是 | 4<br>8<br>12 |
| `image` | 用於影片生成的可選輸入參考圖像；僅支援單張圖像 | IMAGE | 否 | - |
| `seed` | 用於決定節點是否應重新執行的種子；無論種子為何，實際結果皆不具決定性（預設：0） | INT | 否 | 0 至 2147483647 |

**限制與條件：**

- "sora-2" 模型僅支援 "720x1280" 與 "1280x720" 尺寸；若搭配 "sora-2" 選擇 "1024x1792" 或 "1792x1024" 會引發錯誤。較大的尺寸僅能搭配 "sora-2-pro" 使用。
- 當連接圖像時，必須恰好包含一張圖像；連接超過一張圖像會引發錯誤。
- 無論 `seed` 值為何，結果皆不具決定性。
- 顯示的價格預估取決於所選的 `model`、`size` 與 `duration`。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `output` | 由 OpenAI Sora 生成的影片 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIVideoSora2/zh-TW.md)

---
**Source fingerprint (SHA-256):** `d19eb6b65d7f712278828e4b1f7105068cc5e7cb72813b7549ab24520e7719fc`
