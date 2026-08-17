# Runway 首尾幀轉影片

Runway 首尾幀轉影片節點透過上傳首幀與尾幀關鍵影格，並搭配文字提示來產生影片。它使用 Runway 的 Gen-3 模型，在提供的開始與結束影格之間建立平滑轉場。這對於結束影格與開始影格差異甚大的複雜轉場特別有用。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 用於生成內容的文字提示（預設為空字串） | STRING | 是 | N/A |
| `start_frame` | 用於影片的起始影格 | IMAGE | 是 | N/A |
| `end_frame` | 用於影片的結束影格。僅支援 gen3a_turbo 模型。 | IMAGE | 是 | N/A |
| `duration` | 影片時長（秒）（預設為 "5"） | COMBO | 是 | `"5"`<br>`"10"` |
| `ratio` | 生成影片的長寬比（預設為 "768:1280"） | COMBO | 是 | `"768:1280"`<br>`"1280:768"` |
| `seed` | 生成時使用的隨機種子。設為 0 則使用隨機種子（預設為 0）。 | INT | 否 | 0 至 4294967295 |

**參數約束：**

- `prompt` 必須包含至少 1 個字元
- `start_frame` 和 `end_frame` 的最大尺寸皆必須為 7999x7999 像素
- `start_frame` 和 `end_frame` 的長寬比皆必須介於 0.5 到 2.0 之間
- `end_frame` 參數僅在使用 gen3a_turbo 模型時受支援

**注意：** 此節點已標記為棄用。使用前請參閱 Runway 在 Gen-3 上使用關鍵影格進行創作的建議做法：https://help.runwayml.com/hc/en-us/articles/34170748696595-Creating-with-Keyframes-on-Gen-3

## 輸出

| 輸出名 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `output` | 在起始與結束影格之間轉場的生成影片 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RunwayFirstLastFrameNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `1d8720aba833348583d2aa37e13a1ad43d9055b0201c9cb6ad9c95dada7e5056`
