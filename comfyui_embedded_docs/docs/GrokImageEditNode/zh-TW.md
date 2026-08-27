# Grok 圖像編輯

Grok Image Edit 節點會根據文字提示修改現有圖像。它使用 Grok API 產生一張或多張輸入圖像的變體，並根據您的描述進行引導。此節點已標記為棄用。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | 用於圖像編輯的特定 AI 模型。 | COMBO | 是 | `"grok-imagine-image-quality"`<br>`"grok-imagine-image-pro"`<br>`"grok-imagine-image"` |
| `image` | 要編輯的輸入圖像。 | IMAGE | 是 |  |
| `prompt` | 用於產生圖像的文字提示。多行文字；必須包含至少一個非空白字元。 | STRING | 是 |  |
| `resolution` | 輸出圖像的解析度。 | COMBO | 是 | `"1K"`<br>`"2K"` |
| `number_of_images` | 要產生的已編輯圖像數量（預設值：1）。 | INT | 是 | 1 至 10 |
| `seed` | 用於決定節點是否應重新執行的種子；無論種子值為何，實際結果皆不具確定性（預設值：0）。 | INT | 是 | 0 至 2147483647 |
| `長寬比` | 輸出圖像的長寬比。僅在圖像輸入連接到多個圖像時才允許設定（預設值："auto"）。 | COMBO | 否 | `"auto"`<br>`"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"9:16"`<br>`"16:9"`<br>`"9:19.5"`<br>`"19.5:9"`<br>`"9:20"`<br>`"20:9"`<br>`"1:2"`<br>`"2:1"` |

**重要限制：**
- `image` 輸入最多支援 3 張圖像，但使用 `grok-imagine-image-pro` 模型時除外，該模型僅支援 1 張輸入圖像。
- `aspect_ratio` 參數只能在多個圖像連接到 `image` 輸入時設定為自訂值（非 "auto"）。使用單一輸入圖像設定自訂長寬比會導致錯誤。
- `prompt` 必須包含至少一個非空白字元。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `output` | 由節點產生的已編輯圖像。如果產生多張圖像，這些圖像會串接成單一批次。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokImageEditNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `e2ace07d10901c4e57086da8e3294a5d04e379103e9740131f5355cd4b07625d`
