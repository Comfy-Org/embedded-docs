# 轉換影像色彩空間

ImageColorSpace 節點可在 sRGB (Rec.709)、linear Rec.709、HDR (Rec.2020 HLG) 與 HDR PQ (Rec.2020 PQ) 色彩空間之間轉換影像。當轉換為 SDR 輸出，或從 HDR PQ 轉換為 HDR 時，會對整個批次中超出範圍的亮度進行色調映射，並壓縮超出色域的顏色；linear 輸出與 linear-to-HDR 轉換則會保留擴展值，不進行色調映射。轉換以 float32 計算，且任何 alpha 通道都會原樣傳遞。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `image` | 要轉換的輸入影像。 | IMAGE | 是 | 任何有效影像。 |
| `source` | 輸入像素的色彩空間。預設值："sRGB"。 | COMBO | 是 | `"sRGB"`<br>`"HDR"`<br>`"HDR PQ"`<br>`"linear"` |
| `destination` | 輸出像素的色彩空間。請將儲存節點設為相同的色彩空間。預設值："sRGB"。 | COMBO | 是 | `"sRGB"`<br>`"HDR"`<br>`"HDR PQ"`<br>`"linear"` |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `image` | 轉換後、位於指定目標色彩空間的影像。 | IMAGE |

## 備註

- Linear 1.0 使用與 sRGB 相同的 203-nit 參考白；HLG 使用 1000-nit 參考顯示器。
- linear 輸出與 linear-to-HDR 轉換會保留擴展值，不進行色調映射。
- SDR 輸出與 PQ-to-HLG 轉換會對整個批次中超出範圍的亮度進行色調映射（共用同一個白點，因此曝光不會逐幀改變），並壓縮超出色域的顏色。
- 轉換以 float32 計算，並傳回中間裝置與 dtype。
- Straight alpha 不會進行色彩轉換；只有 RGB 通道會被轉換。
- 若 `source` 與 `destination` 相同，則不會套用任何色彩轉換——影像只會被移至中間裝置與 dtype。

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageColorSpace/zh-TW.md)

---
**Source fingerprint (SHA-256):** `04ae447a9f9805341e31755ad0fa56746ac0371fa2cb9bda95df3879c9dbead7`
