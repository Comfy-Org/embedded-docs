# Vidu 多畫格影片生成

## 概述
此節點透過在多個關鍵影格之間建立轉場效果來生成影片。它從初始影像開始，透過一系列使用者定義的結束影像和提示詞進行動畫處理，最終輸出單一影片檔案。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 用於影片生成的 Vidu 模型。 | COMBO | 是 | `"viduq2-pro"`<br>`"viduq2-turbo"` |
| `start_image` | 起始幀影像。長寬比必須介於 1:4 到 4:1 之間。 | IMAGE | 是 | - |
| `seed` | 隨機數生成的種子值，用於確保結果可重現（預設值：1）。 | INT | 否 | 0 到 2147483647 |
| `resolution` | 輸出影片的解析度。 | COMBO | 是 | `"720p"`<br>`"1080p"` |
| `frames` | 關鍵影格轉場數量（2-9）。選取值後會動態顯示每個影格所需的輸入項目。 | DYNAMICCOMBO | 是 | `"2"`<br>`"3"`<br>`"4"`<br>`"5"`<br>`"6"`<br>`"7"`<br>`"8"`<br>`"9"` |

**影格輸入（動態顯示）：**
當您為 `frames` 選取值（例如 "3"）時，節點會顯示每個轉場對應的一組必要輸入。對於從 1 到所選數字的每個影格 `i`，您必須提供：

* `end_image{i}` (IMAGE)：此轉場的目標影像。長寬比必須介於 1:4 到 4:1 之間。
* `prompt{i}` (STRING)：引導轉場至此影格的文字描述（最多 2000 個字元）。
* `duration{i}` (INT)：此特定轉場區段的持續時間（秒）。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `output` | 包含所有動畫轉場的生成影片檔案。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ViduMultiFrameVideoNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `02ddbb1e041b6d9e6654ab6c3cc25f4c2e5bc1545d84a30624608edc85e51f96`
