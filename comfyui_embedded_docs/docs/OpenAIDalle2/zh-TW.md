# OpenAIDalle2

透過 OpenAI 的 DALL·E 2 端點同步生成圖像。此節點會將文字提示傳送到 OpenAI 的 DALL·E 2 API，並將產生的圖像回傳至 ComfyUI。當 `image` 和 `mask` 同時提供時，它也可以編輯現有圖像。

## 運作方式

此節點連線至 OpenAI 的 DALL·E 2 API，以根據文字描述建立圖像。當您提供文字提示時，節點會將其傳送到 OpenAI 的伺服器，伺服器會生成對應圖像並將其回傳至 ComfyUI。此節點可運作於兩種模式：僅使用文字提示的標準圖像生成，或同時提供圖像與遮罩時的圖像編輯模式。在編輯模式中，它會使用遮罩來決定原始圖像中哪些部分應被修改，同時保持其他區域不變。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `prompt` | DALL·E 的文字提示（預設：空） | STRING | 是 | - |
| `seed` | 後端尚未實作（預設：0） | INT | 否 | 0 到 2147483647 |
| `size` | 圖像尺寸（預設："1024x1024"） | COMBO | 否 | "256x256"<br>"512x512"<br>"1024x1024" |
| `n` | 要生成多少張圖像（預設：1） | INT | 否 | 1 到 8 |
| `image` | 用於圖像編輯的選用參考圖像。 | IMAGE | 否 | - |
| `mask` | 用於影像修補的選用遮罩（白色區域將被替換） | MASK | 否 | - |

**注意：** 只有當 `image` 和 `mask` 同時提供時，圖像編輯模式才會啟用。若只提供其中一個，會引發錯誤。`mask` 必須與 `image` 大小相同；否則會引發錯誤。在編輯模式下，遮罩的白色區域表示將被替換的區域。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `IMAGE` | 由 DALL·E 2 生成或編輯的圖像 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIDalle2/zh-TW.md)

---
**Source fingerprint (SHA-256):** `c6bba5dd44ebed1d795e6ec93bdd2e19685e8ae9f24be9145ad9d74d3a9b7a0c`
