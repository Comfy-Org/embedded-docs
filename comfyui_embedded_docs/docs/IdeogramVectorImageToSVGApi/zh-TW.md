# Ideogram Vector Image to SVG

此節點使用 Ideogram Vector 將影像轉換為可編輯的 SVG。結果是向量標記而非點陣影像，因此描繪出的形狀可在向量編輯器中保持可編輯。含 alpha 的影像中，透明區域會保持透明。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | 要使用的模型。預設值：`"ideogram-vector-1"`。 | DYNAMIC_COMBO | 是 | `"ideogram-vector-1"` |
| `image` | 要轉換的影像。批次輸入會逐張影像轉換，並一併回傳產生的 SVG。 | IMAGE | 是 | - |
| `mode` | `"simple"` 會描繪較少、較大的形狀；`"default"` 會保留更精細的細節。預設值：`"default"`。 | COMBO | 是 | `"simple"`<br>`"default"` |

**限制：**

* 最長邊超過 2048 像素的影像會在上傳前縮小。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `SVG` | 轉換後的影像，以可編輯的向量標記表示。 | SVG |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramVectorImageToSVGApi/zh-TW.md)

---
**Source fingerprint (SHA-256):** `6553291e9d887b31485b9cbf8f6ced4186470eb47e8621ebb0f4e5df6542123e`
