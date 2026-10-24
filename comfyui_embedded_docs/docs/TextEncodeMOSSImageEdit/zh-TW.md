# Text Encode MOSS-Image Edit

將編輯指令與參考圖片一起編碼成用於 MOSS-Image 編輯 LoRA 的 conditioning。將輸出連接為正向 conditioning，並使用相同的參考圖片再執行一個實例以產生負向 conditioning。參考圖片會依其傳入時的尺寸使用，因此請先縮放再連接。未連接 VAE 時，圖片只會進入文字編碼器。此節點在 ComfyUI 中標記為實驗性。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `clip` | 用於將指令分詞並編碼的 CLIP 模型。 | CLIP | 是 | - |
| `prompt` | 描述編輯操作的指令。支援多行文字與動態提示詞。 | STRING | 是 | 任意文字 |
| `vae` | 將圖片編碼為編輯 LoRA 的參考 latent。選用：未連接時，圖片只會進入文字編碼器。 | VAE | 否 | - |
| `edit_format` | 編輯 LoRA 訓練時所採用的配置。它會選擇參考 latent 方法，以及文字編碼器是否也會看到參考圖片。 | COMBO | 是 | `"ai-toolkit"`<br>`"ai-toolkit (kv_cache off)"`<br>`"Moss-Image-Edit"` |
| `images` | 可擴增插槽：連接一張或多張參考圖片（`image_1`、`image_2`、...）。每張圖片會以其傳入時的尺寸使用。連接了 VAE 時，會捨棄 alpha 通道並將每張圖片編碼成參考 latent；未連接 VAE 時，圖片只會進入文字編碼器。 | IMAGE | 是 | 1 張或以上圖片 |
| `image_strength` | 縮放模型對文字編碼器所見圖片的關注程度（ai-toolkit 格式，或未連接 VAE）：0 表示忽略，1 表示不變，大於 1 表示加強。進階參數。預設：1.0。 | FLOAT | 是 | 0.0 到 100.0（步進 0.05） |

**注意：** 使用 `"ai-toolkit"` 和 `"ai-toolkit (kv_cache off)"` 時，或在未連接 VAE 且 `image_strength` 大於 0 時，文字編碼器也會看到每一張參考圖片，這些圖片會被縮小到最大 384x384 像素，並在提示詞中前置一個 `Picture N:` 標記，因此指令可以透過編號引用它們。使用 `"Moss-Image-Edit"` 且連接了 VAE 時，參考圖片僅以參考 latent 的形式進入模型，文字編碼器只會看到指令本身。此外，`"ai-toolkit (kv_cache off)"` 會讓參考圖片持續關注正在生成的圖片，因此它們會在每個取樣步驟中重新計算。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `conditioning` | 編碼後的指令，附帶參考 latent 以及相匹配的參考 latent 方法。 | CONDITIONING |

> 本文件由 AI 產生。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeMOSSImageEdit/zh-TW.md)

---
**Source fingerprint (SHA-256):** `673f098df6a8e466a5c8060009f446eac8f7556311a870de626c5f4bfc3ab196`
