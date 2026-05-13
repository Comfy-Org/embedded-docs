> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QuiverTextToSVGNode/zh-TW.md)

### 概述

Quiver Text to SVG 節點使用 Quiver AI 的模型，根據文字描述生成可縮放向量圖形（SVG）圖像。您可以選擇性地提供參考圖像和樣式指示來引導生成過程。

### 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | 是 | 不適用 | 所需 SVG 輸出的文字描述。這是生成內容的主要指示。 |
| `instructions` | STRING | 否 | 不適用 | 額外的樣式或格式指引。這是可選的進階參數。 |
| `reference_images` | IMAGE | 否 | 0 到 4 張圖像 | 最多 4 張參考圖像，用於引導生成過程。這是可選輸入。 |
| `model` | COMBO | 是 | `"Quiver SVG v1"`<br>`"Quiver SVG v1 Max"`<br>`"Quiver SVG v1 Preview"` | 用於 SVG 生成的模型。可用選項由 Quiver API 決定。 |
| `seed` | INT | 是 | 0 到 2147483647 | 用於決定節點是否應重新執行的種子；實際結果無論種子為何都是非確定性的。預設值：0。 |

**注意：** `reference_images` 輸入最多接受 4 張圖像。如果提供超過此數量，節點將會引發錯誤。

### 輸出

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `SVG` | SVG | 生成的可縮放向量圖形（SVG）圖像。 |

---
**Source fingerprint (SHA-256):** `634758797a59e5a409424deee808e1d8b5b5852a86eac4bccd7f2634a19fb743`
