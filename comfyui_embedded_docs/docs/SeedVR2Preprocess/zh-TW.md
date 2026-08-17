# 預處理 SeedVR2 輸入

此節點會對調整大小後的影像進行填充（padding），以準備供 SeedVR2 模型使用。在處理過程中會移除 Alpha 色版，之後由配套的「Post-Process SeedVR2 Output」節點使用原始調整大小後的影像將其還原。

## 輸入
| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `resized_images` | 要處理的已調整大小影像。 | IMAGE | Yes | - |

注意：輸入可以是單張影像或一系列幀（例如，來自影片的幀）。其較短的邊緣必須至少為 2 像素。在處理過程中，Alpha 色版（如果存在）會被移除，像素值會被限制在 [0, 1] 範圍內，寬度和高度會被填充為 16 的倍數。幀序列會進行填充，使其長度遵循 1、5、9、13、…… 幀的模式。

## 輸出
| Output Name | Description | Data Type |
|-------------|-------------|-----------|
| `images` | 用於 VAE 編碼的填充後影像。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedVR2Preprocess/zh-TW.md)

---
**Source fingerprint (SHA-256):** `f4fa433d299feba40696f27ff365c59988e5102112f09536724b5db5b09416bb`
