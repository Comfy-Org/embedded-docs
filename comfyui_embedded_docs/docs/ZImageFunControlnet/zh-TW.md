> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ZImageFunControlnet/zh-TW.md)

ZImageFunControlnet 節點應用專門的控制網路來影響影像生成或編輯過程。它使用基礎模型、模型修補檔和 VAE，讓您可以調整控制效果的強度。此節點可搭配基礎影像、修補影像和遮罩使用，以進行更精準的編輯。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | 是 | - | 用於生成過程的基礎模型。 |
| `model_patch` | MODEL_PATCH | 是 | - | 應用控制網路引導的專門修補模型。 |
| `vae` | VAE | 是 | - | 用於編碼和解碼影像的變分自編碼器。 |
| `strength` | FLOAT | 是 | -10.0 至 10.0 | 控制網路影響的強度。正值應用效果，負值則可能反轉效果（預設值：1.0）。 |
| `image` | IMAGE | 否 | - | 用於引導生成過程的選用基礎影像。 |
| `inpaint_image` | IMAGE | 否 | - | 專門用於修補由遮罩定義區域的選用影像。 |
| `mask` | MASK | 否 | - | 定義影像中哪些區域應被編輯或修補的選用遮罩。 |

**注意：** `inpaint_image` 參數通常與 `mask` 搭配使用，以指定修補內容。節點的行為可能會根據提供的選用輸入而改變（例如，使用 `image` 進行引導，或使用 `image`、`mask` 和 `inpaint_image` 進行修補）。

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `model` | MODEL | 已應用控制網路修補的模型，準備好用於採樣流程。 |
| `positive` | CONDITIONING | 正向條件，可能已根據控制網路輸入進行修改。 |
| `negative` | CONDITIONING | 負向條件，可能已根據控制網路輸入進行修改。 |
