此節點將多個文字列表合併為單一組合列表。其設計用於接收文字列表形式的輸入，並將它們串接在一起。節點會記錄合併後列表中的文字總數。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `文字` | 要合併的文字列表。可將多個列表連接到輸入端，它們將被串接成一個列表。 | STRING | 是 | 不適用 |

**注意：** 此節點配置為群組處理（`is_group_process = True`），表示它會在主處理函數執行前，自動透過串接方式處理多個列表輸入。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `文字` | 包含所有輸入文字的單一合併列表。 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MergeTextLists/zh-TW.md)

---
**Source fingerprint (SHA-256):** `043a39a373d03f1ff79dd0746070171bab4d5d915c985e4e64fd35f802b09f69`
