# Flux Pro Ultra 影像節點

根據提示詞和解析度，透過 API 使用 Flux Pro 1.1 Ultra 生成影像。此節點連接到外部服務，根據您的文字描述和指定的尺寸來建立影像。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `提示詞` | 影像生成的提示詞（預設：空字串） | STRING | 是 | - |
| `提示詞向上採樣` | 是否對提示詞進行上取樣。若啟用，將自動修改提示詞以產生更具創意的生成結果，但結果不具確定性（相同的種子不會產生完全相同的結果）。（預設：False） | BOOLEAN | 否 | - |
| `種子` | 用於建立雜訊的隨機種子。（預設：0） | INT | 否 | 0 到 18446744073709551615 |
| `長寬比` | 影像的長寬比；必須介於 1:4 和 4:1 之間。（預設："16:9"） | STRING | 否 | - |
| `原始` | 設為 True 時，生成較少處理、更自然的影像。（預設：False） | BOOLEAN | 否 | - |
| `影像提示` | 可選的參考影像，用於引導生成 | IMAGE | 否 | - |
| `影像提示強度` | 提示詞與影像提示詞之間的混合程度。（預設：0.1） | FLOAT | 否 | 0.0 到 1.0 |

**注意：** `aspect_ratio` 參數必須介於 1:4 和 4:1 之間。當提供 `image_prompt` 時，`image_prompt_strength` 會生效，並控制參考影像對最終輸出的影響程度。如果未提供 `image_prompt`，則會驗證 `prompt` 參數不為空。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `output_image` | 由 Flux Pro 1.1 Ultra 生成的影像 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxProUltraImageNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `8632aeb76e9007d65d7f3fd51465fe78f56ba92264ef65ce505db2fc95cfd25b`
