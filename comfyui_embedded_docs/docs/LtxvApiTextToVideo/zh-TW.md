> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LtxvApiTextToVideo/zh-TW.md)

LTXV Text To Video 節點能根據文字描述生成專業品質的影片。它透過連接外部 API 來建立影片，並可自訂影片的持續時間、解析度和幀率。您還可以選擇為影片添加 AI 生成的音訊。

## 輸入參數

| 參數 | 資料類型 | 必填 | 範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | 是 | `"LTX-2 (Fast)"`<br>`"LTX-2 (Quality)"`<br>`"LTX-2 (Turbo)"` | 用於影片生成的 AI 模型。可用的模型對應自原始碼中的 `MODELS_MAP`。 |
| `prompt` | STRING | 是 | - | AI 將用於生成影片的文字描述。此欄位支援多行文字。 |
| `duration` | COMBO | 是 | `6`<br>`8`<br>`10`<br>`12`<br>`14`<br>`16`<br>`18`<br>`20` | 生成影片的長度，單位為秒（預設值：8）。 |
| `resolution` | COMBO | 是 | `"1920x1080"`<br>`"2560x1440"`<br>`"3840x2160"` | 輸出影片的像素尺寸（寬度 x 高度）。 |
| `fps` | COMBO | 是 | `25`<br>`50` | 影片的每秒幀數（預設值：25）。 |
| `generate_audio` | BOOLEAN | 否 | - | 啟用後，生成的影片將包含與場景匹配的 AI 生成音訊（預設值：False）。 |

**重要限制：**

* `prompt` 的長度必須介於 1 到 10,000 個字元之間。
* 如果您選擇的 `duration` 超過 10 秒，則必須同時使用 `"LTX-2 (Fast)"` 模型、`"1920x1080"` 的解析度以及 `25` 的 `fps`。此組合是生成較長影片的必要條件。

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `output` | VIDEO | 生成的影片檔案。 |
