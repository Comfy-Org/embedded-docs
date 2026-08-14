# QwenImageEditApi

此節點使用 Qwen-Image 3.0 模型，在文字提示的引導下編輯或組合最多 3 張參考圖片。您提供文字提示和參考圖片，節點會將生成的結果以一或多張圖片的形式回傳。

## 輸入
| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | 要使用的模型。此選擇也包含文字提示、最多 3 個參考圖片輸入，以及可選的負面提示。 | COMBO | 是 | "qwen-image-3.0-pro"<br>"qwen-image-3.0" |
| `size` | 輸出解析度。「match input」會重複使用第一張參考圖片的尺寸，「auto」讓模型選擇具有相同長寬比的尺寸，「custom」則設定明確的寬度和高度。 | COMBO | 是 | "match input"<br>"auto"<br>"custom" |
| `n` | 要生成的圖片數量，以批次形式回傳。（預設值：1） | INT | 否 | 1 到 6 |
| `seed` | 用於生成的種子。（預設值：42） | INT | 否 | 0 到 2147483647 |
| `prompt_extend` | 是否透過 AI 輔助來增強提示。（預設值：True） | BOOLEAN | 否 | True<br>False |
| `watermark` | 是否在結果中加入 AI 生成的水印。（預設值：False） | BOOLEAN | 否 | True<br>False |

### 限制條件

- 文字提示為必填，且至少包含一個字元。
- 最多支援 3 張參考圖片；如果提供更多，則會引發錯誤（批次輸入的每張圖片各計一次）。
- 當 `size` 設定為「custom」時，必須提供明確的寬度和高度值，並會進行驗證。
- 當 `size` 設定為「match input」時，至少需要一張參考圖片，因為會使用第一張參考圖片的尺寸。

## 輸出
| 輸出名 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| IMAGE | 生成的圖片或以批次形式回傳的圖片。最多回傳 `n` 張圖片。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QwenImageEditApi/zh-TW.md)

---
**Source fingerprint (SHA-256):** `efa8d2b1a039a7b91789c0332b751a5f90ab8dad755ef0e25124d7d1c44d9abb`
