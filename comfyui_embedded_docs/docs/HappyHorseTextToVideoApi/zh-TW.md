# HappyHorse 文字轉影片

此節點使用 HappyHorse 模型根據文字提示產生影片。此節點會將您的提示與設定傳送至 HappyHorse API，等待影片產生完成後，再下載結果。

## 輸入

### 通用輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | 用於產生的 HappyHorse 模型，以及其子參數。選擇模型後，會決定可使用哪些子參數（請參閱下方各模型章節）。 | DICT | 是 | "happyhorse-1.1-t2v"<br>"happyhorse-1.0-t2v" |
| `seed` | 用於產生的隨機種子。使用相同種子搭配相同輸入會產生相同結果。（預設值：0）。 | INT | 是 | 0 到 2147483647 |
| `watermark` | 是否在結果中加入 AI 產生的浮水印。（預設值：False）。 | BOOLEAN | 否 | True / False |

### happyhorse-1.1-t2v 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model.prompt` | 描述元素與視覺特徵的提示。支援英文與中文。（預設值：""）。 | STRING | 是 | - |
| `model.resolution` | 輸出影片的解析度。 | STRING | 是 | "720P"<br>"1080P" |
| `model.ratio` | 輸出影片的長寬比。 | STRING | 是 | "16:9"<br>"9:16"<br>"1:1"<br>"4:3"<br>"3:4"<br>"21:9"<br>"9:21"<br>"5:4"<br>"4:5" |
| `model.duration` | 影片長度（秒）。（預設值：5，最小值：3，最大值：15，間距：1）。 | INT | 是 | 3 到 15 |

### happyhorse-1.0-t2v 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model.prompt` | 描述元素與視覺特徵的提示。支援英文與中文。（預設值：""）。 | STRING | 是 | - |
| `model.resolution` | 輸出影片的解析度。 | STRING | 是 | "720P"<br>"1080P" |
| `model.ratio` | 輸出影片的長寬比。 | STRING | 是 | "16:9"<br>"9:16"<br>"1:1"<br>"4:3"<br>"3:4" |
| `model.duration` | 影片長度（秒）。（預設值：5，最小值：3，最大值：15，間距：1）。 | INT | 是 | 3 到 15 |

注意：提示不得為空；若未提供提示，則會產生錯誤。兩個模型皆支援 3 到 15 秒的影片長度。`happyhorse-1.1-t2v` 模型提供額外的長寬比（`21:9`、`9:21`、`5:4`、`4:5`），而 `happyhorse-1.0-t2v` 不支援這些長寬比。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `VIDEO` | 產生的影片檔案。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HappyHorseTextToVideoApi/zh-TW.md)

---
**Source fingerprint (SHA-256):** `b60cfc3ce4935d7eb36bb28f9bd268446c4df5b437e06278b7e6d91d349d0238`
