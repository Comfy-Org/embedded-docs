# LTXV 圖片轉影片

LTXV 影像轉影片節點可從單張起始影像生成專業品質的影片。它使用外部 API 根據您的文字提示建立影片序列，讓您自訂時間長度、解析度與幀率。

## 輸入

| 參數 | 說明 | 資料型別 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `image` | 用於影片的第一幀。 | IMAGE | 是 | - |
| `model` | 用於影片生成的 AI 模型。「Pro」模型針對品質最佳化，而「Fast」模型針對速度最佳化。 | COMBO | 是 | `"LTX-2 (Pro)"`<br>`"LTX-2 (Fast)"` |
| `prompt` | 引導生成影片內容與動作的文字描述。 | STRING | 是 | - |
| `duration` | 影片的長度（秒）（預設值：8）。 | COMBO | 是 | `6`<br>`8`<br>`10`<br>`12`<br>`14`<br>`16`<br>`18`<br>`20` |
| `resolution` | 生成影片的輸出解析度。 | COMBO | 是 | `"1920x1080"`<br>`"2560x1440"`<br>`"3840x2160"` |
| `fps` | 影片的每秒幀數（預設值：25）。 | COMBO | 是 | `25`<br>`50` |
| `generate_audio` | 設為 true 時，生成的影片將包含符合場景的 AI 生成音訊（預設值：False）。 | BOOLEAN | 否 | - |

**重要限制：**

* `image` 輸入必須僅包含一張圖片。
* `prompt` 的長度必須介於 1 到 10,000 個字元之間。
* 如果您選擇的 `duration` 超過 10 秒，則必須使用 **"LTX-2 (Fast)"** 模型、**"1920x1080"** 解析度及 **25** FPS。較長的影片需要此組合。

## 輸出

| 輸出名稱 | 說明 | 資料型別 |
| --- | --- | --- |
| `video` | 生成的影片檔案。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LtxvApiImageToVideo/zh-TW.md)

---
**Source fingerprint (SHA-256):** `fa3928262e59105718b6ed97ddc8d2801e540b6b0c142541d92525dd75540cc7`
