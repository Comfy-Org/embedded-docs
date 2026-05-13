> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftColorRGB/zh-TW.md)

透過指定個別的紅、綠、藍數值來建立 Recraft 顏色。此節點接收 RGB 整數值（0-255），並將其轉換為可在其他 Recraft 操作中使用的 Recraft 顏色格式。您也可以選擇性地提供現有的 Recraft 顏色鏈，以將新顏色擴充至其中。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `r` | INT | 是 | 0-255 | 顏色的紅色數值（預設值：0） |
| `g` | INT | 是 | 0-255 | 顏色的綠色數值（預設值：0） |
| `b` | INT | 是 | 0-255 | 顏色的藍色數值（預設值：0） |
| `recraft_color` | COLOR | 否 | - | 可選的現有 Recraft 顏色鏈，用於將新的 RGB 顏色擴充至其中 |

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `recraft_color` | COLOR | 包含指定 RGB 數值的已建立 Recraft 顏色物件，或若提供了現有顏色鏈，則為擴充後的顏色鏈 |

---
**Source fingerprint (SHA-256):** `8c3503632d085fa4c1771f92f17008b7b051e9604d9e7d1e7d352cbbbd22dddc`
