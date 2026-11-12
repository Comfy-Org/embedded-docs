# ByteDance Seedance 2.5 草稿轉最終影片

此節點會將 Seedance 2.5 Draft 的最終影片渲染為 1080p 或 4k，4k 開放所有帳戶使用。草稿是快速的 480p 預覽：在 Seedance 2.5 影片節點（文字轉影片、首尾幀轉影片或參考轉影片）中，將 `model` 設為 `Seedance 2.5 Draft`，執行該節點，並將其 `draft_task_id` 輸出連接到此處。最終影片會保留草稿的場景與動作，並重複使用產生該草稿時所用的提示詞、參考素材、時長、長寬比與音訊設定。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `draft_task_id` | 以 Seedance 2.5 Draft 模型執行 Seedance 2.5 節點所產生的 `draft_task_id` 輸出，或貼上的草稿任務 ID。當您重新執行產生該草稿的節點時，請將其 `seed` 控制項設為固定，否則下一次執行會產生新的草稿，而不是重複使用您已檢閱的草稿。 | STRING | 是 | - |
| `浮水印` | 是否要在影片中加入浮水印。預設為 False。此為進階設定。 | BOOLEAN | 否 | True 或 False |
| `resolution` | 最終影片的解析度。`"4k"` 開放所有帳戶使用；值必須是小寫的 `"4k"`。預設：`"1080p"`。 | COMBO | 否 | `"1080p"`<br>`"4k"` |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `video` | 渲染完成後從供應商下載的最終影片。 | VIDEO |

**注意：** 草稿在建立後 7 天內可以渲染。草稿任務 ID 本身即可識別草稿，因此不需要再次傳入提示詞、參考素材、時長、長寬比與音訊設定。

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2DraftToFinalVideoNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `bf96a485d5febde26e22433d190cfe42bd21dc6316d66141ad23d4b95a845dc5`
