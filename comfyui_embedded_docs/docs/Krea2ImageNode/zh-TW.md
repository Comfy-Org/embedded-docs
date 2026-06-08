## 概述

Krea 2 影像節點使用 Krea 2 AI 模型生成影像。它支援兩種模型變體：Medium 適合表現力豐富的插圖，Large 則適合表現力豐富的照片級寫實風格。您可以選擇性地加入情緒板（moodboard）以及最多 10 個影像風格參考，以影響生成的影像。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `提示詞` | 影像的文字提示。 | STRING | 是 | 不適用 |
| `模型` | Krea 2 Medium 最適合表現力豐富的插圖；Krea 2 Large 最適合表現力豐富的照片級寫實風格。 | DICT | 是 | 見下方 |
| `隨機種子` | 用於再現結果的隨機種子（預設值：0）。 | INT | 是 | 0 到 2147483647 |

`model` 參數是一個字典，包含以下子參數：

| 子參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `模型` | 選擇 Krea 2 模型變體。 | STRING | 是 | `"krea 2 medium"`<br>`"krea 2 large"` |
| `aspect_ratio` | 生成影像的長寬比。 | STRING | 是 | 不適用 |
| `resolution` | 生成影像的解析度。 | STRING | 是 | 不適用 |
| `creativity` | 控制生成過程的創意程度。 | FLOAT | 是 | 不適用 |
| `moodboard_id` | 用於影響影像的 Krea 情緒板 UUID。必須是有效的 UUID。 | STRING | 否 | 不適用 |
| `moodboard_strength` | 情緒板的影響強度（預設值：0.35）。 | FLOAT | 否 | 不適用 |
| `style_reference` | 影像風格參考列表。每個參考必須包含 `url`（STRING）和 `strength`（FLOAT）。 | LIST | 否 | 0 到 10 個項目 |

**限制條件：**
- `moodboard_id` 必須是有效的 UUID（例如 `"123e4567-e89b-12d3-a456-426614174000"`）。請從 Krea 網站複製。
- `style_reference` 最多接受 10 個影像風格參考。
- `prompt` 長度必須至少為 1 個字元。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `image` | 生成的影像，以張量形式呈現。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Krea2ImageNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `6aeb2d935ef5df5699a19271c9ceb766892ef4b0e4f67bfa540bf12ffadf362d`
