# LtxvApiImageToVideo

LTXV Image To Video 節點可從單一起始圖像生成專業品質的影片。它使用外部 API，根據你的文字提示詞建立影片序列，讓你能自訂時長、解析度和影格率。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `image` | 用於影片的第一個影格。 | IMAGE | 是 | - |
| `model` | 用於影片生成的 AI 模型。"Pro" 模型針對品質最佳化，而 "Fast" 模型則針對速度最佳化。 | COMBO | 是 | `"LTX-2 (Pro)"`<br>`"LTX-2 (Fast)"` |
| `prompt` | 引導生成影片內容與動作的文字描述（預設：空白）。 | STRING | 是 | - |
| `duration` | 影片長度，以秒為單位（預設：8）。 | COMBO | 是 | `6`<br>`8`<br>`10`<br>`12`<br>`14`<br>`16`<br>`18`<br>`20` |
| `resolution` | 生成影片的輸出解析度。 | COMBO | 是 | `"1920x1080"`<br>`"2560x1440"`<br>`"3840x2160"` |
| `fps` | 影片的每秒影格數（預設：25）。 | COMBO | 是 | `25`<br>`50` |
| `generate_audio` | 當為 true 時，生成的影片將包含與場景相符的 AI 生成音訊（預設：False）。 | BOOLEAN | 否 | - |

**重要限制：**

* `image` 輸入必須恰好包含一張圖像。
* `prompt` 的長度必須介於 1 到 10,000 個字元之間。
* 如果你選擇的 `duration` 超過 10 秒，則必須使用 **"LTX-2 (Fast)"** 模型、**"1920x1080"** 解析度，以及 **25** FPS。較長的影片必須使用此組合。

**注意：** 此節點已標記為棄用。節點上顯示的預估成本取決於所選的 `model`、`duration` 和 `resolution`。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `video` | 生成的影片檔案。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LtxvApiImageToVideo/zh-TW.md)

---
**Source fingerprint (SHA-256):** `fa3928262e59105718b6ed97ddc8d2801e540b6b0c142541d92525dd75540cc7`
