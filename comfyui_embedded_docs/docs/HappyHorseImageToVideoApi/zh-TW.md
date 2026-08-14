# HappyHorse 圖像轉影片

此節點使用 HappyHorse 模型從單一起始圖片生成一段短影片。您提供首幀影像和描述所需動作與場景的文字提示，該節點會建立從該影像繼續延伸的影片。

## 輸入

### 通用輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | 用於影片生成的 HappyHorse 模型。 | COMBO | 是 | `"happyhorse-1.1-i2v"`<br>`"happyhorse-1.0-i2v"` |
| `first_frame` | 首幀影像。輸出寬高比由此影像決定。 | IMAGE | 是 | 最小 300×300 像素；長寬比 1:2.5 至 2.5:1 |
| `seed` | 用於生成的種子。（預設值：0） | INT | 否 | 0 至 2147483647 |
| `watermark` | 是否在結果中加入 AI 生成的浮水印。（進階選項；預設值：False） | BOOLEAN | 否 | True / False |

### happyhorse-1.1-i2v 和 happyhorse-1.0-i2v 輸入

兩個模型版本共用相同的參數集合。

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model.prompt` | 描述元素和視覺特徵的提示。支援英文和中文。（預設值：""） | STRING | 否 | N/A |
| `model.resolution` | 輸出影片解析度。（預設值："720P"） | COMBO | 是 | `"720P"`<br>`"1080P"` |
| `model.duration` | 生成影片的長度（秒）。（預設值：5） | INT | 是 | 3 至 15 |

注意：`first_frame` 影像必須至少為 300x300 像素，且其寬高比必須介於 1:2.5 與 2.5:1 之間。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `video` | 生成的影片檔案。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HappyHorseImageToVideoApi/zh-TW.md)

---
**Source fingerprint (SHA-256):** `4bf6eece0d1b4104ce2d84e29b2c918a0a6ba782da1dd801b66cbfa1666d150b`
