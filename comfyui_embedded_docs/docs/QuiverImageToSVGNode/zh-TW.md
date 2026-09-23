# Quiver 圖像轉 SVG

此節點使用 Quiver AI 的向量化模型，將點陣圖像轉換為可縮放向量圖形（SVG）。它會將圖像傳送至外部 API，由該 API 處理並傳回向量化結果。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `image` | 要向量化的輸入圖像。 | IMAGE | 是 | N/A |
| `auto_crop` | 自動裁切至主要主體（預設：False）。 | BOOLEAN | 是 | True<br>False |
| `model` | 用於 SVG 向量化的模型。選取模型後會顯示該模型專屬的額外參數：`target_size`（方形縮放目標，單位為像素；0 會保留來源影像尺寸，否則為 128 至 4096）、`temperature`、`top_p` 和 `presence_penalty`。 | DYNAMIC_COMBO | 是 | `"arrow-2"`<br>`"arrow-2-telos"`<br>`"arrow-1.1"`<br>`"arrow-1.1-max"`<br>`"arrow-preview"` |
| `seed` | 用於決定節點是否應重新執行的種子；實際結果無論種子值為何皆不具確定性。此參數具有「生成後控制」功能（預設：0）。 | INT | 是 | 0 至 2147483647 |
| `推理強度` | 模型在繪製前投入多少推理。較高等級可提升細節，但會耗用更多 token。僅 Arrow 2 模型會使用（預設："high"）。 | COMBO | 否 | `"low"`<br>`"medium"`<br>`"high"`<br>`"xhigh"` |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `SVG` | 向量化後的 SVG 輸出。 | SVG |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QuiverImageToSVGNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `d32225207ede8f15fd54780778c6b23b1ce1880be8cb416c341e73afbd9b8aa0`
