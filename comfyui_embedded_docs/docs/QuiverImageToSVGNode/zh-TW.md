# Quiver 圖像轉 SVG

此節點使用 Quiver AI 的向量化模型，將點陣圖影像轉換為可縮放向量圖形 (SVG)。它會將影像發送到外部 API，由該 API 處理並返回向量化的結果。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `image` | 要進行向量化的輸入影像。 | IMAGE | 是 | 不適用 |
| `auto_crop` | 自動裁切至主要主體。這是一個進階參數（預設值：`False`）。 | BOOLEAN | 否 | `True`<br>`False` |
| `model` | 用於 SVG 向量化的模型。選擇模型會顯示該模型特有的其他參數：`target_size`（正方形縮放目標像素，預設值：1024，範圍：128-4096）、`temperature`、`top_p` 和 `presence_penalty`。 | DYNAMICCOMBO | 是 | 提供多種選項 |
| `seed` | 決定節點是否應重新執行的種子；無論種子值為何，實際結果都是非確定性的。此參數具有「生成後控制」功能（預設值：0）。 | INT | 否 | 0 至 2147483647 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `SVG` | 向量化後的 SVG 輸出。 | SVG |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QuiverImageToSVGNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `4539277fd6c23aef149c44eeafca4d373cad658d85872de0883245eb4f2479e8`
