# ByteDance Seedance 2.5 Draft to Final Video

此節點會渲染 Seedance 2.5 Draft 的 1080p 最終影片。草稿是快速的 480p 預覽：在 Seedance 2.5 影片節點（文字轉影片、首尾幀轉影片或參考轉影片）中，將 `model` 設為 `Seedance 2.5 Draft`，執行它，然後將其 `draft_task_id` 輸出連接到此處。最終影片會保留草稿的場景與動作，並重複使用產生該草稿時所用的提示詞、參考、時長、長寬比與音訊設定。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `draft_task_id` | 以 Seedance 2.5 Draft 模型執行 Seedance 2.5 節點所產生的 `draft_task_id` 輸出，或貼上的草稿任務 ID。當你重新執行產生該草稿的節點時，請將其 `seed` 控制項設為 fixed，否則下一次執行會產生新的草稿，而不是重複使用你已檢閱的草稿。 | STRING | 是 | - |
| `watermark` | 是否要在影片中加入浮水印。預設值為 False。這是進階設定。 | BOOLEAN | 否 | True / False |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `video` | 渲染完成的 1080p 最終影片，會在渲染任務完成後從供應商下載。 | VIDEO |

**注意：** 草稿可在建立後 7 天內進行渲染。草稿任務 ID 本身即可識別草稿，因此不需要再次傳入提示詞、參考、時長、長寬比與音訊設定。

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2DraftToFinalVideoNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `c9a607826915f09ec199748964010a00a239b5efab3647a3b97fdceee6b04cde`
