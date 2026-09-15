# 儲存文字

Save Text 節點會將文字內容寫入輸出目錄中的檔案。它支援以 .txt、.csv、.md 或 .json 格式儲存，並且當提供有效的 JSON 時，會自動處理 JSON 美化輸出。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `text` | 要儲存到檔案的文字內容。此輸入必須從其他節點連接。 | STRING | 是 | - |
| `filename_prefix` | 輸出檔案名稱的前綴。會附加一個 5 位數計數器，以避免覆寫現有檔案（預設："ComfyUI"）。 | STRING | 否 | - |
| `format` | 儲存文字時使用的檔案格式（預設："txt"）。當選擇 "json" 時，有效的 JSON 文字會以 2 空格縮排美化輸出；否則文字會依原樣儲存。 | COMBO | 否 | `"txt"`<br>`"csv"`<br>`"md"`<br>`"json"` |

### 注意事項

- `text` 是強制輸入，必須連接到另一個節點；無法直接輸入。
- 儲存的檔案命名為 `<filename_prefix>_<5-digit counter>.<extension>`，並寫入 ComfyUI 輸出目錄（位於由前綴衍生的子資料夾中）。
- 選擇 `"json"` 格式時，會嘗試將文字解析為 JSON。若解析成功，內容會以 2 空格縮排美化輸出；若解析失敗，則會將原始文字依原樣寫入。
- 此節點會將儲存的檔案回報至介面，使其與其他產生的輸出檔案一併顯示。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `text` | 儲存到檔案的原始文字內容 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveText/zh-TW.md)

---
**Source fingerprint (SHA-256):** `09bd896cab770358132834892c1b37efd2ffa0cb0aa7b02b7ef91163331dc9b1`
