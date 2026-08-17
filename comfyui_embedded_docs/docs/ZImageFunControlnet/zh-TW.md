# ZImageFunControlnet

ZImageFunControlnet 節點應用一個專門的控制網路來影響圖像生成或編輯過程。它使用基礎模型、模型修補和 VAE，讓您可以調整控制效果的強度。此節點可與基礎圖像、修復圖像和遮罩搭配使用，以進行更精確的編輯。

## 輸入
| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 用於生成過程的基礎模型。 | MODEL | 是 | - |
| `model_patch` | 一種專門的修補模型，用於應用控制網路的引導。 | MODEL_PATCH | 是 | - |
| `vae` | 用於編碼和解碼圖像的變分自編碼器（VAE）。 | VAE | 是 | - |
| `strength` | 控制網路影響的強度。正值應用效果，而負值則可能反轉效果（預設值：1.0）。 | FLOAT | 是 | -10.0 to 10.0 |
| `image` | 可選的基礎圖像，用於引導生成過程。 | IMAGE | 否 | - |
| `inpaint_image` | 可選的圖像，專門用於修復由遮罩定義的區域。 | IMAGE | 否 | - |
| `mask` | 可選的遮罩，定義圖像中應被編輯或修復的區域。 | MASK | 否 | - |

**注意：** `inpaint_image` 參數通常與 `mask` 搭配使用，以指定用於修復的內容。節點的行為可能因提供的可選輸入而有所不同（例如，使用 `image` 進行引導，或使用 `image`、`mask` 和 `inpaint_image` 進行修復）。

## 輸出
| 輸出名 | 描述 | 資料類型 |
| --- | --- | --- |
| `model` | 已應用控制網路修補的模型，可用於取樣管線。 | MODEL |
| `positive` | 正向條件，可能受控制網路輸入影響。 | CONDITIONING |
| `negative` | 負向條件，可能受控制網路輸入影響。 | CONDITIONING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ZImageFunControlnet/zh-TW.md)

---
**Source fingerprint (SHA-256):** `e1946190a06c52dd951078d9cb753962081957cb6c38accdea26eb4129a51793`
