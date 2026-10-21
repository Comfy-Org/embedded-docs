# Bria FIBO 2.0 Image Generate

使用 Bria FIBO 2.0 從文字提示、結構化 JSON 提示或單一參考影像生成新影像。此節點會將請求傳送至 Bria API，等待生成完成，並回傳影像以及結構化提示；此結構化提示可在後續執行中重現或微調該影像。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 以自然語言描述要生成的影像（預設：空）。 | STRING | 是 | 多行文字 |
| `structured_prompt` | 來自先前 Bria FIBO 結果的 JSON 結構化提示。使用相同的 `seed` 可重現該影像；變更 JSON 或新增提示可對其進行微調（預設：空）。 | STRING | 是 | 多行文字 |
| `aspect_ratio` | 輸出長寬比（預設：`"1:1"`）。從 `"16:10"` 起的比例為具有額外要求的 FIBO 2.0 尺寸，詳列如下。 | COMBO | 是 | `"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"4:5"`<br>`"5:4"`<br>`"9:16"`<br>`"16:9"`<br>`"16:10"`<br>`"10:16"`<br>`"2:1"`<br>`"1:2"`<br>`"21:9"`<br>`"9:21"`<br>`"3:1"`<br>`"1:3"`<br>`"4:1"`<br>`"1:4"`<br>`"5:1"`<br>`"1:5"` |
| `resolution` | 以百萬像素為單位的輸出解析度（預設：`"1MP"`）。 | COMBO | 是 | `"1MP"`<br>`"4MP"` |
| `seed` | 用於初始化生成的隨機種子（預設：42）。 | INT | 是 | 1 至 2147483647 |
| `moderation` | 審核設定。選擇 `"true"` 會顯示下列審核輸入。 | DYNAMIC_COMBO | 是 | `"false"`<br>`"true"` |
| `image` | 可選的參考影像，用於作為繪製依據。結果會是所選長寬比的新影像，而不是對此影像進行編輯。 | IMAGE | 否 | - |

### 審核輸入

當 `moderation` 設為 `"true"` 時，這些額外輸入會變為可用：

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt_content_moderation` | 是否要審核提示文字；若審核拒絕，請求會失敗（預設：false）。 | BOOLEAN | 否 | `true`<br>`false` |
| `visual_input_moderation` | 是否要審核參考影像；若審核拒絕，請求會失敗（預設：false）。 | BOOLEAN | 否 | `true`<br>`false` |
| `visual_output_moderation` | 是否要審核生成的影像；若審核拒絕，請求會失敗（預設：false）。 | BOOLEAN | 否 | `true`<br>`false` |

**重要限制：**

- 請至少提供 `prompt`、`structured_prompt` 或參考 `image` 其中一項。若三者皆為空，節點會引發錯誤。
- 參考影像不能與 `structured_prompt` 合併使用：請擇一使用。
- FIBO 2.0 比例（`"16:10"`、`"10:16"`、`"2:1"`、`"1:2"`、`"21:9"`、`"9:21"`、`"3:1"`、`"1:3"`、`"4:1"`、`"1:4"`、`"5:1"`、`"1:5"`）需要 `resolution` 為 `"1MP"`，且必須恰好提供 `prompt` 或 `structured_prompt` 其中一項。
- 此節點為付費 API 節點；ComfyUI 每次執行收取約 0.0572 USD。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `IMAGE` | Bria API 回傳的生成影像。 | IMAGE |
| `structured_prompt` | 所生成影像的結構化描述，可用於透過此節點重現或微調該影像。 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaImageGenerate/zh-TW.md)

---
**Source fingerprint (SHA-256):** `4d53fe457e2e349ac41b5c8a0d3d5599eafa53cb653c470335853f1d4517688f`
