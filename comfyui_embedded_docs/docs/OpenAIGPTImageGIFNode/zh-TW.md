# OpenAI GPT Image 2.6 GIF

## 概覽

OpenAI GPT Image 2.6 GIF 會使用 OpenAI 的 GPT Image 模型，依提示詞生成動態 GIF，並以影格批次加上影格率的形式回傳，因此可直接接入影片或動態影像的儲存節點。目前提供兩種模型：`gpt-image-2.6-flare` 與 `gpt-image-2.6-sunburst`。

## 輸入

### 通用輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 用於製作動畫的 GPT Image 模型。 | DYNAMIC_COMBO | 是 | `"gpt-image-2.6-flare"`<br>`"gpt-image-2.6-sunburst"` |

### gpt-image-2.6-flare 與 gpt-image-2.6-sunburst 輸入

兩種模型共用相同的參數。

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model.prompt` | 要製作成動畫的內容。（預設：`""`） | STRING | 是 | N/A |
| `model.size` | 每個影格的尺寸。尺寸越大，僅能搭配較少的影格數。（預設：`"512x512"`） | COMBO | 是 | `"384x384"`<br>`"512x512"`<br>`"640x640"`<br>`"720x720"`<br>`"768x768"`<br>`"960x960"`<br>`"512x288"`<br>`"288x512"`<br>`"1024x576"`<br>`"576x1024"`<br>`"1280x720"`<br>`"720x1280"` |
| `model.frame_count` | 影格數。影格依級距計費：2 至 8、9、10 至 12、13 至 16。（預設：`9`） | INT | 是 | 2 至 16 |
| `model.frame_duration_ms` | 每個影格顯示的持續時間，單位為毫秒。（預設：`200`） | INT | 是 | 20 至 2000（步進值：10） |
| `model.background` | 影格背景。使用 vp9 的 Save WEBM、Save Animated WEBP 與 Save Animated PNG 可保留透明度。（預設：`"opaque"`） | COMBO | 是 | `"opaque"`<br>`"transparent"` |
| `model.quality` | 影像品質。等級越高，費用越高且耗時越長。（預設：`"low"`） | COMBO | 是 | `"low"`<br>`"medium"`<br>`"high"`<br>`"xhigh"`<br>`"max"` |
| `model.complexity` | 模型在算繪前對動畫的規劃程度。（預設：`"high"`） | COMBO | 是 | `"low"`<br>`"medium"`<br>`"high"` |
| `model.seed` | 控制節點是否重新執行；無論種子為何，結果皆不具決定性。（預設：`42`） | INT | 是 | 0 至 2147483647 |

**參數限制與注意事項：**

- 影格率由 `model.frame_duration_ms` 計算：200 毫秒相當於 5 fps。
- 較大的 `model.size` 搭配較高的 `model.frame_count` 無法使用，並會在價格標籤上顯示「Size too large for this frame count」。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `frames` | 以影格批次形式呈現的動畫，可直接供影片或動態影像的儲存節點使用。 | IMAGE |
| `fps` | 每秒影格數，取自回傳 GIF 的影格持續時間。 | FLOAT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIGPTImageGIFNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `e47ebaef90f8b2618ef3c2659778f75ac9763013dcc515ba5650764ce49da951`
