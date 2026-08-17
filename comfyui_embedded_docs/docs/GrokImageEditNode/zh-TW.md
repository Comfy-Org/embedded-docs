# Grok 圖像編輯

Grok 影像編輯節點會根據文字提示修改現有影像。它使用 Grok API 產生一張或多張基於輸入影像變體的新影像，並由您的描述引導。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | 用於影像編輯的特定 AI 模型。 | COMBO | 是 | `"grok-imagine-image-quality"`<br>`"grok-imagine-image-pro"`<br>`"grok-imagine-image"` |
| `image` | 要編輯的輸入影像。最多支援 3 張輸入影像，但「pro」模型僅支援 1 張。 | IMAGE | 是 |  |
| `prompt` | 用於產生影像的文字提示。去除空白後長度必須至少為 1 個字元。 | STRING | 是 |  |
| `resolution` | 輸出影像的解析度。 | COMBO | 是 | `"1K"`<br>`"2K"` |
| `number_of_images` | 要產生的已編輯影像數量（預設值：1）。 | INT | 是 | 1 至 10 |
| `seed` | 用於判斷節點是否應重新執行的種子；無論種子為何，實際結果都是非確定性的（預設值：0）。 | INT | 是 | 0 至 2147483647 |
| `aspect_ratio` | 輸出影像的長寬比。僅當多張影像連接到影像輸入時才允許設定。若設為「auto」，將自動決定長寬比（預設值：「auto」）。 | COMBO | 否 | `"auto"`<br>`"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"9:16"`<br>`"16:9"`<br>`"9:19.5"`<br>`"19.5:9"`<br>`"9:20"`<br>`"20:9"`<br>`"1:2"`<br>`"2:1"` |

**重要約束：**
- `image` 輸入最多支援 3 張影像，但使用 `grok-imagine-image-pro` 模型時僅支援 1 張輸入影像。
- 僅當多張影像連接到 `image` 輸入時，`aspect_ratio` 參數才能設為自訂值（非「auto」）。使用單一輸入影像設定自訂長寬比將導致錯誤。

**注意：** 此節點已棄用。

## 輸出

| 輸出名 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `output` | 節點產生的已編輯影像。如果 `number_of_images` 大於 1，輸出會串接成一個批次。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokImageEditNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `e2ace07d10901c4e57086da8e3294a5d04e379103e9740131f5355cd4b07625d`
