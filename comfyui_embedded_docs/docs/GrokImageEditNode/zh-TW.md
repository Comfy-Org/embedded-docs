# Grok 圖像編輯

Grok 圖片編輯節點可根據文字提示修改現有圖片。它使用 Grok API 生成一個或多個基於輸入圖片並根據您的描述進行變化的新圖片。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 用於圖片編輯的特定 AI 模型。 | COMBO | 是 | `"grok-imagine-image-quality"`<br>`"grok-imagine-image-pro"`<br>`"grok-imagine-image"`<br>`"grok-imagine-image-beta"` |
| `image` | 要編輯的輸入圖片。最多支援 3 張輸入圖片，但「pro」模型僅支援 1 張。 | IMAGE | 是 |  |
| `prompt` | 用於生成編輯後圖片的文字提示。去除空白字元後至少需有 1 個字元。 | STRING | 是 |  |
| `resolution` | 輸出圖片的解析度。 | COMBO | 是 | `"1K"`<br>`"2K"` |
| `number_of_images` | 要生成的編輯圖片數量（預設值：1）。 | INT | 否 | 1 到 10 |
| `seed` | 用於決定節點是否應重新執行的種子；無論種子為何，實際結果都是非確定性的（預設值：0）。 | INT | 否 | 0 到 2147483647 |
| `長寬比` | 輸出圖片的長寬比。僅當多張圖片連接到圖片輸入時才允許設定。若設為「auto」，則長寬比會自動決定（預設值：「auto」）。 | COMBO | 否 | `"auto"`<br>`"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"9:16"`<br>`"16:9"`<br>`"9:19.5"`<br>`"19.5:9"`<br>`"9:20"`<br>`"20:9"`<br>`"1:2"`<br>`"2:1"` |

**重要限制：**
- `image` 輸入最多支援 3 張圖片，但使用 `grok-imagine-image-pro` 模型時除外，該模型僅支援 1 張輸入圖片。
- `aspect_ratio` 參數僅能在多張圖片連接到 `image` 輸入時設定為自訂值（非「auto」）。若使用單張輸入圖片設定自訂長寬比，將會導致錯誤。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `output` | 由節點生成的編輯後圖片。若 `number_of_images` 大於 1，則輸出會合併為一個批次。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokImageEditNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `021d867e9e04451c0c4ef035c19fa86ebc8d4a3f64572aff33f493324d7fe308`
