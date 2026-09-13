# RecraftStyleV3VectorIllustrationNode

此節點為 Recraft API 選擇一種風格，具體來說是向量插畫風格類別。您可以選擇性在該類別中挑選更精確的子風格。此節點會輸出一個風格設定物件，可傳遞給其他 Recraft 節點。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `substyle` | 向量插畫類別中更精確的風格。可用選項為 Recraft API 針對 `vector_illustration` 風格所定義的子風格。若未選擇子風格，則使用基礎 `vector_illustration` 風格。 | COMBO | 是 | 多個可用選項（動態載入的 `vector_illustration` 風格子風格清單） |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `recraft_style` | 一個 Recraft 風格設定物件，包含所選的向量插畫風格及可選的子風格。可連接到其他 Recraft 節點。 | STYLEV3 |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftStyleV3VectorIllustrationNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `e88e7ea35b18acb55ec59814981cb36451d922d3287d23dcdb504289ea9f541b`
