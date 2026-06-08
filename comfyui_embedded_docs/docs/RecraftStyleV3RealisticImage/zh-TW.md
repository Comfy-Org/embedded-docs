此節點用於建立風格配置，以使用 Recraft 的 API 生成逼真影像。它選取 `realistic_image` 風格，並讓您選擇一個可選的子風格來微調輸出外觀。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `子風格` | 要套用至 realistic_image 風格的特定子風格。若設為 "None"，則不套用任何子風格。 | STRING | 是 | 多個選項可用（由 Recraft API 決定） |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `recraft_style` | 一個 Recraft 風格配置物件，包含 `realistic_image` 風格與所選的子風格設定。此輸出可連接至其他接受風格輸入的 Recraft 節點。 | STYLEV3 |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftStyleV3RealisticImage/zh-TW.md)

---
**Source fingerprint (SHA-256):** `23eafae0a00f1806052a6583db791a5c1fd418ea940ed6463824dffe843ed0d7`
