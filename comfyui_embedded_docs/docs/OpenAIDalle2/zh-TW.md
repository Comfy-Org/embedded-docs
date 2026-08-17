# OpenAI DALL·E 2

OpenAI DALL·E 2 透過 OpenAI 的 DALL·E 2 端點同步生成圖像。提供文字提示以建立新圖像，或同時提供圖像和遮罩以編輯現有圖像。

## 運作方式

此節點連線到 OpenAI 的 DALL·E 2 API，根據文字描述建立圖像。當您提供文字提示時，節點會將其傳送到 OpenAI 的伺服器，由伺服器生成對應的圖像並回傳至 ComfyUI。此節點可運作於兩種模式：僅使用文字提示的標準圖像生成模式，以及在同時提供圖像與遮罩時的圖像編輯模式。在編輯模式中，節點會使用遮罩來決定原始圖像中應被修改的部分，同時保持其他區域不變。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | DALL·E 的文字提示（預設值：空） | STRING | Yes | - |
| `seed` | 尚未在後端實作（預設值：0） | INT | No | 0 to 2147483647 |
| `size` | 圖像尺寸（預設值："1024x1024"） | COMBO | No | "256x256"<br>"512x512"<br>"1024x1024" |
| `n` | 要生成的圖像數量（預設值：1） | INT | No | 1 to 8 |
| `image` | 用於圖像編輯的選用參考圖像。 | IMAGE | No | - |
| `mask` | 用於修復的選用遮罩（白色區域將被取代） | MASK | No | - |

注意：`image` 和 `mask` 必須同時提供。當同時提供兩者時，節點會切換至圖像編輯模式。如果只提供其中一個，則會引發錯誤。`mask` 的大小必須與 `image` 相同。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `IMAGE` | 從 DALL·E 2 生成或編輯的圖像 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIDalle2/zh-TW.md)

---
**Source fingerprint (SHA-256):** `c6bba5dd44ebed1d795e6ec93bdd2e19685e8ae9f24be9145ad9d74d3a9b7a0c`
