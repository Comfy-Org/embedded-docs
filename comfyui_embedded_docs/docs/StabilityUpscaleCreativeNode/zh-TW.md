> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StabilityUpscaleCreativeNode/zh-TW.md)

## 概述

以最小改動將影像放大至 4K 解析度。此節點使用 Stability AI 的創意放大技術，在保留原始內容的同時提升影像解析度，並加入細微的創意細節。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | 是 | - | 要放大的輸入影像 |
| `prompt` | STRING | 是 | - | 您希望在輸出影像中看到的內容。一個強而有力、描述性強的提示詞，清楚定義元素、顏色和主題，將帶來更好的結果。（預設值：空字串） |
| `creativity` | FLOAT | 是 | 0.1-0.5 | 控制產生未受初始影像強烈制約的額外細節的可能性。（預設值：0.3） |
| `style_preset` | STRING | 是 | `"3d-model"`<br>`"analog-film"`<br>`"anime"`<br>`"cinematic"`<br>`"comic-book"`<br>`"digital-art"`<br>`"enhance"`<br>`"fantasy-art"`<br>`"isometric"`<br>`"line-art"`<br>`"low-poly"`<br>`"modeling-compound"`<br>`"neon-punk"`<br>`"origami"`<br>`"photographic"`<br>`"pixel-art"`<br>`"tile-texture"` | 可選的生成影像風格。（預設值："None"） |
| `seed` | INT | 是 | 0-4294967294 | 用於產生噪聲的隨機種子。（預設值：0） |
| `negative_prompt` | STRING | 否 | - | 您不希望出現在輸出影像中的關鍵詞。這是一項進階功能。（預設值：空字串） |

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `image` | IMAGE | 放大至 4K 解析度的影像 |

---
**Source fingerprint (SHA-256):** `46f7bdd3cb4254b6305407f43e4a9a69a54fd3a0ac285d784c899dbf52edd552`
