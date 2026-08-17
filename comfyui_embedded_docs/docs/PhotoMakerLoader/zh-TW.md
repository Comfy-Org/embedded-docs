# PhotoMaker 載入器

PhotoMakerLoader 節點會從可用的模型檔案中載入 PhotoMaker 模型。它會讀取指定的模型檔案，並準備 PhotoMaker ID 編碼器，用於以身份為基礎的影像生成任務。此節點被標記為實驗性功能，僅供測試用途。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `photomaker_model_name` | 要載入的 PhotoMaker 模型檔案名稱。可用選項取決於 `photomaker` 資料夾中的模型檔案。 | COMBO | Yes | Multiple options available |

注意：所選的模型檔案必須存在於 `photomaker` 資料夾中。如果找不到指定的檔案，節點將引發錯誤。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `photomaker_model` | 已載入的 PhotoMaker 模型，包含 ID 編碼器，可用於身份編碼操作。 | PHOTOMAKER |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PhotoMakerLoader/zh-TW.md)

---
**Source fingerprint (SHA-256):** `1b26630fadbdc144cd42ca7393f743b079ee7463deb9c8b31b628b5dc7432317`
