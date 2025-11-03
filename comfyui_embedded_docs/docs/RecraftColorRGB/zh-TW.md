> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftColorRGB/zh-TW.md)

透過選擇特定的 RGB 值來建立 Recraft 顏色。此節點允許您透過指定個別的紅、綠、藍值來定義顏色，這些值隨後會被轉換為 Recraft 顏色格式，可用於其他 Recraft 操作。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `r` | INT | 是 | 0-255 | 顏色的紅色值（預設值：0） |
| `g` | INT | 是 | 0-255 | 顏色的綠色值（預設值：0） |
| `b` | INT | 是 | 0-255 | 顏色的藍色值（預設值：0） |
| `recraft_color` | COLOR | 否 | - | 用於擴展的現有 Recraft 顏色（可選） |

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `recraft_color` | COLOR | 建立的 Recraft 顏色物件，包含指定的 RGB 值 |