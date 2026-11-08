# OpenAI GPT Image 2.6

## 概述

OpenAI GPT Image 2.6 使用 OpenAI 的 GPT Image 模型，根據提示詞生成影像，並在連接參考影像時進行編輯。此節點提供四種模型：`gpt-image-2.6-flare`、`gpt-image-2.6-sunburst`、`gpt-image-2.5-flare` 和 `gpt-image-2.5-sunburst`。在第一張參考影像上繪製標註，並將它們作為標記對連接，以向模型顯示確切的編輯位置。

## 輸入

### 通用輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 要使用的 GPT Image 模型。選取模型後會顯示該模型的參數。 | DYNAMIC_COMBO | 是 | `"gpt-image-2.6-flare"`<br>`"gpt-image-2.6-sunburst"`<br>`"gpt-image-2.5-flare"`<br>`"gpt-image-2.5-sunburst"` |

### gpt-image-2.6-flare 與 gpt-image-2.6-sunburst 輸入

當 `model` 設為 `gpt-image-2.6-flare` 或 `gpt-image-2.6-sunburst` 時，會出現這些輸入。兩個模型共用相同的參數。

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model.prompt` | 要生成的內容，或要進行的編輯。（預設：`""`） | STRING | 是 | N/A |
| `model.size` | 影像尺寸。選擇 "Custom" 以使用自訂寬度和高度。（預設：`"auto"`） | COMBO | 是 | `"auto"`<br>`"1024x1024"`<br>`"1024x1536"`<br>`"1536x1024"`<br>`"2048x2048"`<br>`"2048x1152"`<br>`"1152x2048"`<br>`"3840x2160"`<br>`"2160x3840"`<br>`"Custom"` |
| `model.custom_width` | 僅在 `model.size` 為 "Custom" 時使用。必須是 16 的倍數。（預設：`1024`） | INT | 否 | 480 至 3840（步進值：16） |
| `model.custom_height` | 僅在 `model.size` 為 "Custom" 時使用。必須是 16 的倍數。（預設：`1024`） | INT | 否 | 480 至 3840（步進值：16） |
| `model.background` | 傳回包含或不包含背景的影像。（預設：`"auto"`） | COMBO | 是 | `"auto"`<br>`"opaque"`<br>`"transparent"` |
| `model.quality` | 影像品質。較高等級成本更高且耗時更長。（預設：`"low"`） | COMBO | 是 | `"low"`<br>`"medium"`<br>`"high"`<br>`"xhigh"`<br>`"max"` |
| `model.complexity` | 模型在渲染前規劃影像的程度。（預設：`"high"`） | COMBO | 是 | `"low"`<br>`"medium"`<br>`"high"` |
| `model.images` | 用於編輯的選用參考影像。最多 16 張。 | AUTOGROW | 否 | 0 至 16 |
| `model.markup` | 繪製於第一張參考影像上的標註，顯示要編輯的位置。必須與該影像的尺寸相符，且必須與 `model.markup_alpha` 一起連接。 | IMAGE | 否 | N/A |
| `model.markup_alpha` | 白色標記 `model.markup` 中的標註。Painter 節點的 MASK 輸出可直接使用；Load Image 的遮罩需要先經過 Invert Mask。 | MASK | 否 | N/A |
| `model.seed` | 控制節點是否重新執行；無論種子為何，結果都是非確定性的。（預設：`42`） | INT | 是 | 0 至 2147483647 |

### gpt-image-2.5-flare 與 gpt-image-2.5-sunburst 輸入

當 `model` 設為 `gpt-image-2.5-flare` 或 `gpt-image-2.5-sunburst` 時，會出現這些輸入。它們與 2.6 模型相同，但不提供 `model.complexity`。

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model.prompt` | 要生成的內容，或要進行的編輯。（預設：`""`） | STRING | 是 | N/A |
| `model.size` | 影像尺寸。選擇 "Custom" 以使用自訂寬度和高度。（預設：`"auto"`） | COMBO | 是 | `"auto"`<br>`"1024x1024"`<br>`"1024x1536"`<br>`"1536x1024"`<br>`"2048x2048"`<br>`"2048x1152"`<br>`"1152x2048"`<br>`"3840x2160"`<br>`"2160x3840"`<br>`"Custom"` |
| `model.custom_width` | 僅在 `model.size` 為 "Custom" 時使用。必須是 16 的倍數。（預設：`1024`） | INT | 否 | 480 至 3840（步進值：16） |
| `model.custom_height` | 僅在 `model.size` 為 "Custom" 時使用。必須是 16 的倍數。（預設：`1024`） | INT | 否 | 480 至 3840（步進值：16） |
| `model.background` | 傳回包含或不包含背景的影像。（預設：`"auto"`） | COMBO | 是 | `"auto"`<br>`"opaque"`<br>`"transparent"` |
| `model.quality` | 影像品質。較高等級成本更高且耗時更長。（預設：`"low"`） | COMBO | 是 | `"low"`<br>`"medium"`<br>`"high"`<br>`"xhigh"`<br>`"max"` |
| `model.images` | 用於編輯的選用參考影像。最多 16 張。 | AUTOGROW | 否 | 0 至 16 |
| `model.markup` | 繪製於第一張參考影像上的標註，顯示要編輯的位置。必須與該影像的尺寸相符，且必須與 `model.markup_alpha` 一起連接。 | IMAGE | 否 | N/A |
| `model.markup_alpha` | 白色標記 `model.markup` 中的標註。Painter 節點的 MASK 輸出可直接使用；Load Image 的遮罩需要先經過 Invert Mask。 | MASK | 否 | N/A |
| `model.seed` | 控制節點是否重新執行；無論種子為何，結果都是非確定性的。（預設：`42`） | INT | 是 | 0 至 2147483647 |

**參數限制與限制條件：**

- 當 `model.size` 設為 "Custom" 時，`model.custom_width` 和 `model.custom_height` 都必須是 16 的倍數，最長邊不得超過 3840，長寬比不得超過 3:1，且總像素數必須介於 655,360 和 8,294,400 之間。
- `model.markup` 和 `model.markup_alpha` 必須一起連接。標記需要至少一張參考影像，且其寬度和高度必須與第一張參考影像相符。
- 若沒有 `model.images`，節點僅根據提示詞生成影像；若有參考影像，則會編輯並組合它們。
- 參考影像在傳送到 API 之前會先縮小。
- `model.complexity` 僅存在於 `gpt-image-2.6-flare` 和 `gpt-image-2.6-sunburst`；2.5 模型使用固定的規劃深度。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `image` | 生成的一或多張影像。所有傳回的影像會堆疊成一個批次；若尺寸不同，則會調整大小以符合第一張影像。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIGPTImageNodeV3/zh-TW.md)

---
**Source fingerprint (SHA-256):** `33f5d91af56c215cc7f7c704f9b123fe1c35bf287012072b818b76b551c04667`
