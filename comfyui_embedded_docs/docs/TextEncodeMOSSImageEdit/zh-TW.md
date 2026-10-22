# Text Encode MOSS-Image Edit

將編輯指令與參考圖片一起編碼成 MOSS-Image 編輯 LoRA 的 conditioning。將輸出連接為正向 conditioning，並使用相同的參考圖片再執行一個實例以產生負向 conditioning。參考圖片會以其傳入時的尺寸使用，因此請在連接前先進行縮放。此節點在 ComfyUI 中標記為實驗性。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `clip` | 用於將指令分詞並編碼的 CLIP 模型。 | CLIP | 是 | - |
| `prompt` | 描述編輯操作的指令。支援多行文字與動態提示詞。 | STRING | 是 | 任意文字 |
| `vae` | 用於將參考圖片編碼成參考 latent 的 VAE。 | VAE | 是 | - |
| `edit_format` | 編輯 LoRA 訓練時所採用的配置。它會選擇參考 latent 方法，以及文字編碼器是否也會看到參考圖片。 | COMBO | 是 | `"ai-toolkit"`<br>`"ai-toolkit (kv_cache off)"`<br>`"Moss-Image-Edit"` |
| `images` | 可擴增插槽：連接一張或多張參考圖片（`image_1`、`image_2`、...）。每張圖片會以其傳入時的尺寸使用，捨棄其 alpha 通道，並經 VAE 編碼成參考 latent。 | IMAGE | 是 | 1 張或以上圖片 |

**注意：** 使用 `"ai-toolkit"` 與 `"ai-toolkit (kv_cache off)"` 時，文字編碼器也會看到每一張參考圖片；這些圖片會縮小至最多 384x384 像素，並在提示詞中於其前面加上 `Picture N:` 標記，因此指令可以透過編號來指涉它們。使用 `"Moss-Image-Edit"` 時，參考圖片只會以參考 latent 的形式抵達模型，而文字編碼器只會看到指令。`"ai-toolkit (kv_cache off)"` 還會讓參考圖片持續對正在生成的圖片進行注意力計算，因此它們會在每個取樣步驟重新計算。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `conditioning` | 已附加參考 latent 與相符參考 latent 方法的編碼指令。 | CONDITIONING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeMOSSImageEdit/zh-TW.md)

---
**Source fingerprint (SHA-256):** `30e4edbb129f647cdce4ec95f78c002ecdc9a4f8fc5a45f1477fdc555b541dae`
