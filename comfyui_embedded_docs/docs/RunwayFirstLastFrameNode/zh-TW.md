# Runway 首尾幀轉影片節點

Runway 首尾幀轉影片節點透過上傳首尾關鍵幀以及文字提示來生成影片。它使用 Runway 的 Gen-3 模型在提供的起始和結束幀之間建立流暢的過渡效果。這對於結束幀與起始幀差異較大的複雜過渡特別有用。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `提示詞` | 生成用的文字提示（預設：空字串） | STRING | 是 | 不適用 |
| `起始幀` | 用於影片的起始幀 | IMAGE | 是 | 不適用 |
| `結束幀` | 用於影片的結束幀。僅支援 gen3a_turbo 模型。 | IMAGE | 是 | 不適用 |
| `持續時間` | 影片長度（秒）（預設："5"） | COMBO | 是 | `"5"`<br>`"10"` |
| `比例` | 生成影片的長寬比（預設："16:9"） | COMBO | 是 | `"16:9"`<br>`"9:16"`<br>`"1:1"` |
| `種子值` | 生成用的隨機種子。設為 0 使用隨機種子（預設：0）。 | INT | 否 | 0 至 4294967295 |

**參數限制：**

- `prompt` 必須包含至少 1 個字元
- `start_frame` 和 `end_frame` 的最大尺寸必須為 7999x7999 像素
- `start_frame` 和 `end_frame` 的長寬比必須在 0.5 到 2.0 之間
- `end_frame` 參數僅在使用 gen3a_turbo 模型時支援

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `output` | 在起始和結束幀之間過渡的生成影片 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RunwayFirstLastFrameNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `57b72c1143b7053272107403279e1f84919cbfe71c57ca4f4e21b4324f7a5346`
