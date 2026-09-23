# Quiver 文字轉 SVG

Quiver Text to SVG 節點使用 Quiver AI 的模型，從文字描述生成可縮放向量圖形 (SVG) 影像。您可以選擇性提供參考影像和風格指示來引導生成過程。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 期望 SVG 輸出的文字描述。這是生成內容的主要指示。 | STRING | 是 | N/A |
| `instructions` | 額外的風格或格式指引。這是選用的進階參數。 | STRING | 否 | N/A |
| `reference_images` | 最多 4 張參考影像來引導生成。這是選用輸入。 | IMAGE | 否 | 0 至 4 images |
| `model` | 用於 SVG 生成的模型。選擇模型會顯示該模型專屬的額外參數：`temperature`、`top_p` 和 `presence_penalty`。 | DYNAMIC_COMBO | 是 | `"arrow-2"`<br>`"arrow-2-telos"`<br>`"arrow-1.1"`<br>`"arrow-1.1-max"`<br>`"arrow-preview"` |
| `seed` | 用來決定節點是否重新執行的種子；無論種子為何，實際結果都是不確定的。預設值：0。 | INT | 是 | 0 至 2147483647 |
| `推理強度` | 模型在繪製前花費多少推理。較高等級可提升細節，但會消耗更多 token。僅 Arrow 2 模型使用（預設值："high"）。 | COMBO | 否 | `"low"`<br>`"medium"`<br>`"high"`<br>`"xhigh"` |

**注意：** `reference_images` 輸入最多接受 4 張影像。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `SVG` | 生成的可縮放向量圖形 (SVG) 影像。 | SVG |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QuiverTextToSVGNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `8b6f21c26748f48eddf2eddaed785a2331a29364744edf30e86e420b0c117e49`
