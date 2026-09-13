# Marigold V2 後處理

此節點將解碼後的 Marigold V2 預測結果轉換為可檢視的圖像。它接收原始預測張量，並依據預測類型進行格式化：正規化深度（近處物件呈現明亮）、單位長度表面法線，或 sRGB 反照率。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `image` | 要轉換為可顯示圖像的解碼後 Marigold V2 預測結果。 | IMAGE | 是 | - |
| `prediction` | 輸入所含的預測類型，此類型決定資料的轉換方式。`"depth"` 會將深度值正規化，使近處表面明亮、遠處表面昏暗，然後把結果複製到三個色彩通道。`"normals"` 會將數值重新縮放至 -1..1 範圍，將其正規化為單位表面法線，再映射回 0..1。`"albedo"` 則對數值套用線性至 sRGB 的轉換。 | COMBO | 是 | `"depth"`<br>`"normals"`<br>`"albedo"` |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `IMAGE` | 所選表示法下處理完成的圖像：正規化深度（重複於三個通道的灰階）、單位表面法線，或 sRGB 反照率。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MarigoldV2PostProcess/zh-TW.md)

---
**Source fingerprint (SHA-256):** `848b29e2dfcd34c44cf9707b9b26cb13c18e82bb16618a15afbe477a1d620e1e`
