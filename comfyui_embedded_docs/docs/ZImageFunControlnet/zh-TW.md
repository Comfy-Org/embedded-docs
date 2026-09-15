# ZImageFunControlnet

ZImageFunControlnet 將控制網路修補套用至基礎模型，使其能夠引導影像生成或編輯流程。它結合模型、模型修補與 VAE，並讓您控制控制效果對結果的影響強度。可選的 `image`、`inpaint_image` 與 `mask` 輸入可實現更精準的編輯。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `模型` | 用於生成流程的基礎模型。 | MODEL | 是 | - |
| `模型補丁` | 套用控制網路引導的專用修補模型。 | MODEL_PATCH | 是 | - |
| `vae` | 用於編碼與解碼影像的變分自編碼器。 | VAE | 是 | - |
| `強度` | 控制網路影響的強度。正值會套用效果，而負值可將其反轉（預設值：1.0）。 | FLOAT | 是 | -10.0 至 10.0 （步進值：0.01） |
| `影像` | 可選的基礎影像，用於引導生成流程。 | IMAGE | 否 | - |
| `修補影像` | 可選的影像，專門用於對遮罩所定義的區域進行修補。 | IMAGE | 否 | - |
| `遮罩` | 可選的遮罩，用於定義影像中應編輯或修補的區域。 | MASK | 否 | - |

**注意：** `inpaint_image` 參數通常與 `mask` 搭配使用，以指定修補內容。節點的行為可能會根據提供哪些可選輸入而改變（例如：使用 `image` 進行引導，或使用 `image`、`mask` 與 `inpaint_image` 進行修補）。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `model` | 已套用控制網路修補的模型，可用於取樣流程。 | MODEL |
| `positive` | 正向條件，可能已由控制網路輸入修改。 | CONDITIONING |
| `negative` | 負向條件，可能已由控制網路輸入修改。 | CONDITIONING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ZImageFunControlnet/zh-TW.md)

---
**Source fingerprint (SHA-256):** `e1946190a06c52dd951078d9cb753962081957cb6c38accdea26eb4129a51793`
