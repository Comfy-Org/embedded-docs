# TripoEditMultiviewNode

Tripo: Edit Multiview 透過對每個視圖使用不同的文字指令，編輯 Tripo: Image to Multiview 結果的四個視圖。沒有指令的視圖保持不變。編輯後的圖像是為了連接到 Tripo: Multiview to Model，以建立 3D 模型。

## 輸入

| 參數 | 描述 | 資料型態 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `multiview_task_id` | 其視圖將被編輯的 Tripo: Image to Multiview 結果之任務 ID。 | MULTIVIEW_TASK_ID | 是 | Task ID |
| `front_prompt` | 描述要套用至前視圖之編輯的文字指令。當此值為空白時，前視圖保持不變。預設值：空白。 | STRING | 否 | Multiline text |
| `left_prompt` | 描述要套用至左視圖之編輯的文字指令。當此值為空白時，左視圖保持不變。預設值：空白。 | STRING | 否 | Multiline text |
| `back_prompt` | 描述要套用至後視圖之編輯的文字指令。當此值為空白時，後視圖保持不變。預設值：空白。 | STRING | 否 | Multiline text |
| `right_prompt` | 描述要套用至右視圖之編輯的文字指令。當此值為空白時，右視圖保持不變。預設值：空白。 | STRING | 否 | Multiline text |

注意：四個提示（`front_prompt`、`left_prompt`、`back_prompt`、`right_prompt`）中至少有一個必須包含非空文字，否則節點將引發錯誤。`multiview_task_id` 必須來自 Tripo: Image to Multiview 節點。已編輯的多視圖集合無法再次編輯。

## 輸出

| 輸出名稱 | 描述 | 資料型態 |
|-------------|-------------|-----------|
| `前方` | 編輯後的前視圖圖像。 | IMAGE |
| `左側` | 編輯後的左視圖圖像。 | IMAGE |
| `後方` | 編輯後的後視圖圖像。 | IMAGE |
| `右側` | 編輯後的右視圖圖像。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoEditMultiviewNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `7a25f3867776c01ab606d43a988b5491e543b72d3eedac1779fa170453c1ca21`
