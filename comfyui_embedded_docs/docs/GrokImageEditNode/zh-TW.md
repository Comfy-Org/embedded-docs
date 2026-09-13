# Grok 圖像編輯

Grok Image Edit 節點會根據文字提示修改現有影像。它會將輸入影像與您的描述傳送至 Grok API，並傳回一張或多張依照提示新生成的影像。此節點已標記為棄用。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | 用於影像編輯的特定 AI 模型。 | COMBO | 是 | `"grok-imagine-image-quality"`<br>`"grok-imagine-image-pro"`<br>`"grok-imagine-image"` |
| `image` | 要編輯的輸入影像。 | IMAGE | 是 |  |
| `prompt` | 用於生成影像的文字提示。多行文字；必須至少包含一個非空白字元。 | STRING | 是 |  |
| `resolution` | 輸出影像的解析度。 | COMBO | 是 | `"1K"`<br>`"2K"` |
| `number_of_images` | 要生成的編輯後影像數量（預設：1）。 | INT | 是 | 1 至 10 |
| `seed` | 用於決定節點是否應重新執行的 `seed`；無論 `seed` 為何，實際結果皆為非確定性（預設：0）。 | INT | 是 | 0 至 2147483647 |
| `長寬比` | 輸出影像的長寬比。僅當有多張影像連接到 `image` 輸入時才允許設定（預設："auto"）。 | COMBO | 否 | `"auto"`<br>`"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"9:16"`<br>`"16:9"`<br>`"9:19.5"`<br>`"19.5:9"`<br>`"9:20"`<br>`"20:9"`<br>`"1:2"`<br>`"2:1"` |

**重要限制：**
- `image` 輸入最多支援 3 張影像，但使用 `grok-imagine-image-pro` 模型時例外，該模型僅支援 1 張輸入影像。
- 僅當多張影像連接到 `image` 輸入時，`aspect_ratio` 參數才能設為自訂值（非 "auto"）。若僅有單張輸入影像卻設定自訂長寬比，將會導致錯誤。
- `prompt` 必須至少包含一個非空白字元。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `output` | 此節點生成的編輯後影像。若生成多張影像，這些影像會合併為單一批次。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokImageEditNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `e2ace07d10901c4e57086da8e3294a5d04e379103e9740131f5355cd4b07625d`
