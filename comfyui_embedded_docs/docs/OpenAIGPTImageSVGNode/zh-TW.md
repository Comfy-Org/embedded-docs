# OpenAI GPT Image 2.6 SVG

## 概覽

OpenAI GPT Image 2.6 SVG 會使用 OpenAI 的 GPT Image 模型，根據提示詞產生可編輯的 SVG。結果為向量標記，因此形狀與文字在向量編輯器中仍可編輯。提供兩種模型：`gpt-image-2.6-flare` 與 `gpt-image-2.6-sunburst`。

## 輸入

### 通用輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 用於 SVG 的 GPT Image 模型。 | DYNAMIC_COMBO | 是 | `"gpt-image-2.6-flare"`<br>`"gpt-image-2.6-sunburst"` |

### gpt-image-2.6-flare 與 gpt-image-2.6-sunburst 輸入

兩個模型共用相同參數。

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model.prompt` | 要繪製的 SVG 描述。（預設：`""`） | STRING | 是 | 不適用 |
| `model.size` | 用於繪製 SVG 的參考影像尺寸。（預設：`"1024x1024"`） | COMBO | 是 | `"1024x1024"`<br>`"1024x1536"`<br>`"1536x1024"` |
| `model.background` | 參考影像的背景。（預設：`"auto"`） | COMBO | 是 | `"auto"`<br>`"opaque"`<br>`"transparent"` |
| `model.quality` | 用於繪製 SVG 的參考影像品質。（預設：`"low"`） | COMBO | 是 | `"low"`<br>`"medium"`<br>`"high"`<br>`"xhigh"`<br>`"max"` |
| `model.complexity` | 模型在渲染前對參考影像進行規劃的程度。（預設：`"high"`） | COMBO | 是 | `"low"`<br>`"medium"`<br>`"high"` |
| `model.seed` | 控制節點是否重新執行；無論 `seed` 為何，結果皆不具確定性。（預設：`42`） | INT | 是 | 0 至 2147483647 |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `svg` | 以 SVG 標記形式產生的向量影像。 | SVG |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIGPTImageSVGNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `8ac2f473b265d3b6857e6280a1c017301b124fc6d671ec83a59c677218062c90`
