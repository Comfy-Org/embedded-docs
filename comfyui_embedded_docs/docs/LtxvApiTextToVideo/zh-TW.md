# LtxvApiTextToVideo

LTXV Text To Video 節點可根據文字描述生成專業品質的影片。它會連線至外部 API，以建立具有自訂時長、解析度和影格率的影片。您也可以選擇將 AI 生成的音訊加入影片中。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 用於影片生成的 AI 模型。「LTX-2 (Pro)」提供更高的品質，而「LTX-2 (Fast)」則針對速度進行最佳化。 | COMBO | 是 | `"LTX-2 (Pro)"`<br>`"LTX-2 (Fast)"` |
| `prompt` | AI 將用來生成影片的文字描述。此欄位支援多行文字，且必須包含 1 到 10,000 個字元。預設值：""（空）。 | STRING | 是 | - |
| `duration` | 生成的影片長度，以秒為單位（預設值：8）。 | COMBO | 是 | `6`<br>`8`<br>`10`<br>`12`<br>`14`<br>`16`<br>`18`<br>`20` |
| `resolution` | 輸出影片的像素尺寸（寬 x 高）。 | COMBO | 是 | `"1920x1080"`<br>`"2560x1440"`<br>`"3840x2160"` |
| `fps` | 影片的每秒影格數（預設值：25）。 | COMBO | 是 | `25`<br>`50` |
| `generate_audio` | 當設為 true 時，生成的影片會包含與場景相符的 AI 生成音訊（預設值：False）。這是進階的選用設定。 | BOOLEAN | 否 | - |

**重要限制：**

* `prompt` 的長度必須介於 1 到 10,000 個字元之間。
* 若您選擇大於 10 秒的 `duration`，則還必須使用 `"LTX-2 (Fast)"` 模型、`resolution` 設為 `"1920x1080"`，以及 `fps` 設為 `25`。較長的影片需要使用此組合。
* 價格取決於所選的 `model`、`duration` 和 `resolution`。

**注意：** 此節點已棄用。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `output` | 生成的影片檔案。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LtxvApiTextToVideo/zh-TW.md)

---
**Source fingerprint (SHA-256):** `8cf7409e46bb92abdff8a12e0d4ab49d67bb70e66c0c9074c9af99d1cf250df8`
