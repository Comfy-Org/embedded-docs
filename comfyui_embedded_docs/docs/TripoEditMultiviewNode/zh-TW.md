# Tripo：編輯多視角

使用針對每個視圖的獨立文字指令，編輯 Tripo: Image to Multiview 結果的視圖。沒有指令的視圖會保持不變。編輯後的影像應連接到 Tripo: Multiview to Model 以建立 3D 模型；已編輯的多視圖集無法再次編輯。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `multiview_task_id` | 要編輯其視圖的 Tripo: Image to Multiview 結果的工作 ID。必須來自 Tripo: Image to Multiview 節點。 | MULTIVIEW_TASK_ID | 是 | Task ID |
| `front_prompt` | 描述要套用於前視圖之編輯的文字指令。當為空時，前視圖保持不變。預設：空字串。 | STRING | 否 | Multiline text |
| `left_prompt` | 描述要套用於左視圖之編輯的文字指令。當為空時，左視圖保持不變。預設：空字串。 | STRING | 否 | Multiline text |
| `back_prompt` | 描述要套用於後視圖之編輯的文字指令。當為空時，後視圖保持不變。預設：空字串。 | STRING | 否 | Multiline text |
| `right_prompt` | 描述要套用於右視圖之編輯的文字指令。當為空時，右視圖保持不變。預設：空字串。 | STRING | 否 | Multiline text |

注意：四個提示（`front_prompt`、`left_prompt`、`back_prompt`、`right_prompt`）中至少有一個必須包含非空文字；只有空白字元的文字會視為空，且如果所有提示皆為空，節點會引發錯誤。

注意：每個具有編輯指令的視圖成本約為 0.05 美元。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `front` | 編輯後的前視圖影像。 | IMAGE |
| `left` | 編輯後的左視圖影像。 | IMAGE |
| `back` | 編輯後的後視圖影像。 | IMAGE |
| `right` | 編輯後的右視圖影像。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoEditMultiviewNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `db8b0a3ffe4332fcbcaac4da0d7b07217d01d2f05526750540f6036293e013ab`
