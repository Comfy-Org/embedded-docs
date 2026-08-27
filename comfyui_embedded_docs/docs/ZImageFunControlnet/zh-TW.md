# ZImageFunControlnet

ZImageFunControlnet 會套用一個專門的控制網路來影響影像生成或編輯過程。它使用基礎模型、模型補丁和 VAE，讓您可以調整控制效果的強度。此節點可搭配基礎影像、修補影像和遮罩使用，以進行更精確的編輯。

## 輸入

| 參數 | 描述 | 資料型別 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `模型` | 用於生成過程的基礎模型。 | MODEL | 是 | - |
| `模型補丁` | 套用控制網路引導的專門補丁模型。 | MODEL_PATCH | 是 | - |
| `vae` | 用於影像編碼和解碼的變分自編碼器。 | VAE | 是 | - |
| `強度` | 控制網路影響的強度。正值套用效果，負值可反轉效果（預設值：1.0）。 | FLOAT | 是 | -10.0 至 10.0 |
| `影像` | 可選的基礎影像，用於引導生成過程。 | IMAGE | 否 | - |
| `修補影像` | 可選影像，專門用於修補遮罩所定義的區域。 | IMAGE | 否 | - |
| `遮罩` | 可選遮罩，定義影像中應被編輯或修補的區域。 | MASK | 否 | - |

**注意：** 通常會搭配 `mask` 使用 `inpaint_image` 參數來指定修補的內容。節點的行為可能因提供了哪些選用輸入而改變（例如，使用 `image` 進行引導，或使用 `image`、`mask` 和 `inpaint_image` 進行修補）。

## 輸出

| 輸出名稱 | 描述 | 資料型別 |
| --- | --- | --- |
| `model` | 已套用控制網路補丁的模型，可用於取樣流程。 | MODEL |
| `positive` | 正向條件，可能已被控制網路輸入修改。 | CONDITIONING |
| `negative` | 負向條件，可能已被控制網路輸入修改。 | CONDITIONING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ZImageFunControlnet/zh-TW.md)

---
**Source fingerprint (SHA-256):** `e1946190a06c52dd951078d9cb753962081957cb6c38accdea26eb4129a51793`
