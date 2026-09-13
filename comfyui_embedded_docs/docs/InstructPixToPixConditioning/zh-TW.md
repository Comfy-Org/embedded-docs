# 指令式像素轉像素條件設定

The InstructPixToPixConditioning 節點會為 InstructPix2Pix 圖像編輯準備 conditioning 資料，方式是將正向與負向文字提示與圖像資料結合。它會透過 VAE 將輸入圖像編碼為 latent 表示，並將該 latent 附加到正向與負向 conditioning，同時也回傳一個對應的空 latent。圖像尺寸會自動裁切為 8 像素的倍數，以便 VAE 能處理。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `正向` | 包含文字提示與所需圖像特徵設定的正向 conditioning 資料 | CONDITIONING | 是 | - |
| `負向` | 包含文字提示與不所需圖像特徵設定的負向 conditioning 資料 | CONDITIONING | 是 | - |
| `vae` | 用於將輸入圖像編碼為 latent 表示的 VAE 模型 | VAE | 是 | - |
| `像素` | 要處理並編碼至 latent 空間的輸入圖像 | IMAGE | 是 | - |

**注意：** 輸入圖像尺寸會透過置中裁切自動調整為寬度和高度皆為 8 像素的倍數，以確保與 VAE 編碼流程相容。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `positive` | 正向 conditioning 資料，並將編碼後的圖像 latent 以 `concat_latent_image` 附加 | CONDITIONING |
| `negative` | 負向 conditioning 資料，並將編碼後的圖像 latent 以 `concat_latent_image` 附加 | CONDITIONING |
| `latent` | 與編碼圖像尺寸相同的全零 latent 張量 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/InstructPixToPixConditioning/zh-TW.md)

---
**Source fingerprint (SHA-256):** `e9a5a05cdeafe9337ca2033111f1ad4f7314fa33d71a4764f62919857efc79f4`
