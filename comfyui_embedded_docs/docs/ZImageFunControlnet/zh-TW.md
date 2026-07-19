# ZImageFunControlnet

ZImageFunControlnet 節點應用一個專門的控制網路來影響影像生成或編輯過程。它使用基礎模型、模型修補程式和 VAE，讓您可以調整控制效果的強度。此節點可與基礎影像、修補影像和遮罩配合使用，以進行更精確的編輯。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `模型` | 用於生成過程的基礎模型。 | MODEL | 是 | - |
| `模型補丁` | 一個專門的修補模型，用於套用控制網路的引導。 | MODEL_PATCH | 是 | - |
| `vae` | 用於編碼和解碼影像的變分自編碼器。 | VAE | 是 | - |
| `強度` | 控制網路影響的強度。正值套用效果，負值則可能反轉效果（預設值：1.0）。 | FLOAT | 是 | -10.0 至 10.0 |
| `影像` | 一個可選的基礎影像，用於引導生成過程。 | IMAGE | 否 | - |
| `修補影像` | 一個可選的影像，專門用於修補由遮罩定義的區域。 | IMAGE | 否 | - |
| `遮罩` | 一個可選的遮罩，用於定義影像中應被編輯或修補的區域。 | MASK | 否 | - |

**注意：** `inpaint_image` 參數通常與 `mask` 搭配使用，以指定用於修補的內容。節點的行為可能會根據提供哪些可選輸入而改變（例如，使用 `image` 進行引導，或使用 `image`、`mask` 和 `inpaint_image` 進行修補）。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `模型` | 已套用控制網路修補的模型，準備好用於取樣流程。 | MODEL |
| `positive` | 正向條件化，可能已由控制網路輸入修改。 | CONDITIONING |
| `negative` | 負向條件化，可能已由控制網路輸入修改。 | CONDITIONING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ZImageFunControlnet/zh-TW.md)

---
**Source fingerprint (SHA-256):** `465f9eb0dd60af23e6cdc2031579e404b4fed021738e592ee6acbb6ee57e83a0`
