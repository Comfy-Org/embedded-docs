# Moonvalley Marey 影像轉影片節點

Moonvalley Marey 影像轉影片節點使用 Moonvalley API 將參考影像轉換為影片。它接收輸入影像和文字提示，以指定的解析度、品質設定和創意控制來生成影片。此節點處理從影像上傳到影片生成和下載的完整流程。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `image` | 用於生成影片的參考影像 | IMAGE | 是 | - |
| `prompt` | 影片生成的文字描述（多行輸入） | STRING | 是 | - |
| `negative_prompt` | 排除不必要元素的負面提示文字（預設：廣泛的負面提示列表） | STRING | 否 | - |
| `resolution` | 輸出影片的解析度（預設："16:9 (1920 x 1080)"） | COMBO | 否 | "16:9 (1920 x 1080)"<br>"9:16 (1080 x 1920)"<br>"1:1 (1152 x 1152)"<br>"4:3 (1536 x 1152)"<br>"3:4 (1152 x 1536)" |
| `prompt_adherence` | 生成控制的引導比例（預設：4.5，步長：1.0） | FLOAT | 否 | 1.0 - 20.0 |
| `seed` | 隨機種子值（預設：9，啟用生成後控制） | INT | 否 | 0 - 4294967295 |
| `steps` | 去噪步驟數（預設：33，步長：1） | INT | 否 | 1 - 100 |

**限制條件：**

- 輸入影像的尺寸必須在 300x300 像素到最大允許高度/寬度之間
- 提示和負面提示文字長度受限於 Moonvalley Marey 的最大提示長度

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `output` | 生成的影片輸出 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoonvalleyImg2VideoNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `674e69a7f106f6f961f10c179008b7bb1147bf0e569c72d207a105f3fab2aaf5`
