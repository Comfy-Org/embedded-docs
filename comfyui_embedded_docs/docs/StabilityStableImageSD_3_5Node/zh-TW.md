此節點使用 Stability AI 的 Stable Diffusion 3.5 模型同步生成圖像。它根據文字提示創建圖像，並能在提供輸入圖像時修改現有圖像。該節點支援多種寬高比和風格預設，以自訂輸出結果。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `prompt` | 您希望在輸出圖像中看到的內容。一個強而有力、描述性強的提示，清楚定義元素、顏色和主題，將帶來更好的結果。（預設值：空字串） | STRING | 是 | - |
| `model` | 用於生成的 Stable Diffusion 3.5 模型。 | COMBO | 是 | `sd3.5-large`<br>`sd3.5-large-turbo`<br>`sd3.5-medium` |
| `長寬比` | 生成圖像的寬高比。（預設值：1:1） | COMBO | 是 | `16:9`<br>`1:1`<br>`21:9`<br>`2:3`<br>`3:2`<br>`4:5`<br>`5:4`<br>`9:16`<br>`9:21` |
| `style_preset` | 可選的生成圖像所需風格。選擇「None」表示不使用任何風格預設。 | COMBO | 否 | `3d-model`<br>`analog-film`<br>`anime`<br>`cinematic`<br>`comic-book`<br>`digital-art`<br>`enhance`<br>`fantasy-art`<br>`isometric`<br>`line-art`<br>`low-poly`<br>`modeling-compound`<br>`neon-punk`<br>`origami`<br>`photographic`<br>`pixel-art`<br>`tile-texture`<br>`None` |
| `cfg_scale` | 擴散過程遵循提示文字的嚴格程度（數值越高，圖像越接近您的提示）。（預設值：4.0） | FLOAT | 是 | 1.0 至 10.0 |
| `種子` | 用於創建噪點的隨機種子。（預設值：0） | INT | 是 | 0 至 4294967294 |
| `影像` | 用於圖像到圖像生成的可選輸入圖像。提供此參數時，節點會切換到圖像到圖像模式，並忽略 `長寬比` 參數。 | IMAGE | 否 | - |
| `負向提示詞` | 您不希望出現在輸出圖像中的關鍵詞。這是一項進階功能。（預設值：空字串） | STRING | 否 | - |
| `image_denoise` | 輸入圖像的去噪強度；0.0 會產生與輸入完全相同的圖像，1.0 則如同未提供任何圖像。（預設值：0.5）此參數僅在提供 `影像` 時使用。 | FLOAT | 否 | 0.0 至 1.0 |

**注意：** 當提供 `image` 時，節點會切換到圖像到圖像生成模式，且 `aspect_ratio` 參數會自動根據輸入圖像決定。當未提供 `image` 時，`image_denoise` 參數會被忽略。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `影像` | 生成或修改後的圖像。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StabilityStableImageSD_3_5Node/zh-TW.md)

---
**Source fingerprint (SHA-256):** `80dbb27f19bb3286ee988f020f7f65623a73d7cac77ca0cdfc7a428254102aa3`
