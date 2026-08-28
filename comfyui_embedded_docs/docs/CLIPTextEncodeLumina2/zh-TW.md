# CLIP 文本編碼（Lumina2）

此節點使用 CLIP 模型將系統提示詞和使用者提示詞編碼為嵌入，該嵌入可用於引導擴散模型生成特定圖像。它將預先定義的 Lumina 2 系統提示詞與您的自訂文字提示詞結合，並透過 CLIP 模型處理它們，以建立用於圖像生成的條件資料。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `system_prompt` | Lumina2 提供兩種類型的系統提示詞：Superior：您是一個旨在根據文字提示或使用者提示，以卓越的圖文對齊程度生成卓越圖像的輔助工具。Alignment：您是一個旨在根據文字提示，以最高程度的圖文對齊生成高品質圖像的輔助工具。 | COMBO | 是 | `"superior"`<br>`"alignment"` |
| `user_prompt` | 要編碼的文字。支援多行輸入和動態提示詞。 | STRING | 是 | N/A |
| `clip` | 用於編碼文字的 CLIP 模型。 | CLIP | 是 | N/A |

**注意：** `clip` 輸入為必填項，不能為 None。如果 clip 輸入無效，節點將拋出錯誤，表示檢查點可能不包含有效的 CLIP 或文字編碼器模型。

## 輸出

| 輸出名 | 描述 | 資料類型 |
| --- | --- | --- |
| `CONDITIONING` | 包含用於引導擴散模型的嵌入文字的條件資料。 | CONDITIONING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeLumina2/zh-TW.md)

---
**Source fingerprint (SHA-256):** `0c7540e6232c93b0f76c4903f5646e00a639ccb0b7720f70b5ac727513358a02`
