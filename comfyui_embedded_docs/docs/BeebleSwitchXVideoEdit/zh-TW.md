# Beeble SwitchX 影片編輯

使用 Beeble SwitchX 編輯影片。此節點可以切換場景中的任何元素（背景、燈光、服裝），同時保留原始主體的像素和動作。提供參考圖片和/或文字提示來描述新的外觀。

## ## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `影片` | 要編輯的輸入影片。最多 240 幀，每幀最多約 2.77 百萬像素。 | VIDEO | 是 | N/A |
| `提示詞` | 場景所需新外觀的文字描述。 | STRING | 是 | N/A |
| `alpha 模式` | Alpha 遮罩模式。"fill" 模式沒有獨立的遮罩，會填滿整個畫面。"select" 模式使用單一關鍵幀圖片來定義要編輯的區域。"custom" 模式使用完整的 Alpha 影片來逐幀定義要編輯的區域。 | COMBO | 是 | `"fill"`<br>`"select"`<br>`"custom"` |
| `最大解析度` | 輸出影片的最大解析度（預設："1080p"）。 | COMBO | 是 | `"720p"`<br>`"1080p"` |
| `種子` | 用於可重現性的種子值。使用相同的種子和輸入將產生相同的結果。 | INT | 是 | 0 至 2147483647 |
| `參考圖像` | 可選的參考圖片，用於描述場景所需的新外觀。 | IMAGE | 否 | N/A |

### Alpha 模式詳細說明

`alpha_mode` 參數控制影片中哪些部分會被編輯：

- **fill**：編輯整個影片畫面。不會產生獨立的 Alpha 遮罩。
- **select**：您提供單一關鍵幀圖片來定義要編輯的區域。節點將使用此圖片來決定要更改影片的哪些部分。
- **custom**：您提供完整的 Alpha 影片來逐幀定義要編輯的區域。這讓您可以精確控制每幀中哪些部分被編輯。

使用 `select` 模式時，您必須提供 `alpha_keyframe` 圖片。使用 `custom` 模式時，您必須提供 `alpha_mask` 影片。

## ## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `影片` | 已套用場景變更的編輯後影片。 | VIDEO |
| `alpha` | Beeble 使用的 Alpha 遮罩。在 "fill" 模式下此輸出為空，因為該模式沒有獨立的遮罩。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BeebleSwitchXVideoEdit/zh-TW.md)

---
**Source fingerprint (SHA-256):** `e2d67b037863f024f42c97943ec0d2daf32b547b232a7dfedd6de398f4b7ba28`
