# ZImageFunControlnet

ZImageFunControlnet 會將控制網路補丁套用至基礎模型，使其能引導影像生成或編輯流程。它結合模型、模型補丁與 VAE，並讓你控制控制效果對結果的影響強度。可選的 `image`、修補影像與 `mask` 輸入可實現更精準的編輯。此節點可搭配 Z-Image ControlNet 補丁，以及透過 Load Model Patch 節點載入的 Qwen Image 2.1 Fun ControlNet 補丁使用。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `模型` | 用於生成過程的基礎模型。 | MODEL | 是 | - |
| `模型補丁` | 套用控制網路引導的專門補丁模型。 | MODEL_PATCH | 是 | - |
| `vae` | 用於編碼與解碼影像的變分自編碼器。 | VAE | 是 | - |
| `強度` | 控制網路影響力的強度。正值會套用效果，負值則可將其反轉（預設：1.0）。 | FLOAT | 是 | -10.0 至 10.0 （步進值：0.01） |
| `影像` | 可選的基礎影像，用於引導生成過程。 | IMAGE | 否 | - |
| `修補影像` | 可選的影像，專門用於修補由遮罩定義的區域。 | IMAGE | 否 | - |
| `遮罩` | 可選的遮罩，用於定義影像中應編輯或修補的區域。 | MASK | 否 | - |
| `start_percent` | 去噪過程中，控制網路開始生效的時機點，以總取樣步數的比例表示（預設：0.0）。 | FLOAT | 否 | 0.0 至 1.0 （步進值：0.001） |
| `end_percent` | 去噪過程中，控制網路停止生效的時機點（預設：1.0）。 | FLOAT | 否 | 0.0 至 1.0 （步進值：0.001） |

**注意：** `inpaint_image` 參數通常會與 `mask` 搭配使用，以指定要修補的內容。節點的行為可能會根據提供了哪些可選輸入而改變（例如，使用 `image` 進行引導，或使用 `image`、`mask` 和 `inpaint_image` 進行修補）。`start_percent` 和 `end_percent` 值會將控制網路限制在去噪過程的某個區間內；在該區間之外，模型會在不套用補丁的情況下取樣。如果 `strength` 為 0，或 `image`、`inpaint_image` 和 `mask` 都未連接，節點會傳回未變更的基礎模型。對於 Z-Image Control 補丁，提供的遮罩會先反轉（1.0 - mask）再使用；而 Qwen Image 2.1 Fun ControlNet 補丁則會直接使用提供的遮罩。此節點標記為實驗性。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `model` | 已套用控制網路補丁的模型，可用於取樣流程。 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ZImageFunControlnet/zh-TW.md)

---
**Source fingerprint (SHA-256):** `9673b8b6e091713bcc93fe5fd1cfed12e6941571d1017e10ac94c19e1afd4ca1`
