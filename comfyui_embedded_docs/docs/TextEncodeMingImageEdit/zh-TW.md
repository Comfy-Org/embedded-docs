# Text Encode Ming Image Edit

Text Encode Ming Image Edit 會將文字提示編碼為用於 Ming 圖像編輯的 conditioning，並可選擇混入參考圖像。提示與參考圖像會由 CLIP 模型進行 token 化；當連接 VAE 時，參考圖像也會被編碼為附加到 conditioning 的 latent 幀。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `clip` | 用於將提示與參考圖像進行 token 化的 CLIP 模型。 | CLIP | 是 | - |
| `vae` | 可選的 VAE，會將參考圖像編碼為附加到 conditioning 的 latent 幀。若沒有 VAE，圖像僅會透過視覺塔對文字編碼器進行條件化。 | VAE | 否 | - |
| `prompt` | 要編碼的文字提示。支援多行輸入與動態提示。 | STRING | 是 | 多行文字 |
| `images` | 可增長的插槽：可選的參考圖像，會由文字編碼器讀取，並以乾淨幀的形式附加到 latent 序列。連接 1..8 張圖像（`image_1`、`image_2`、...）；後續圖像會調整大小以符合第一張圖像，取樣得到的 latent 也應符合第一張圖像的尺寸。僅使用 RGB 通道。 | IMAGE | 否 | 0 至 8 |

**備註：** 參考圖像會依其插槽名稱的數字順序讀取，空插槽會被忽略。只有在同時提供 `vae` 與至少一張圖像時，才會產生參考 latent。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `CONDITIONING` | 包含已編碼提示的 conditioning，以及當提供 VAE 與參考圖像時的參考 latent。 | CONDITIONING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeMingImageEdit/zh-TW.md)

---
**Source fingerprint (SHA-256):** `675fb3cc0af006e1284fdb2a5ca2c268c540ee92e1ede90b2359f4e3fc8ba5ea`
