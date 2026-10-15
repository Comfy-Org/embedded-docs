# Set Reference Multi Latent

此節點會將一張或多張參考影像編碼，並將其 latent 附加到編輯模型所消費的 conditioning 中。它是 Set Reference Latent 的多影像對應版本：你連接一個 VAE 及一組參考影像，節點會將每個編碼後的 latent 附加到正向 conditioning，並且在連接負向 conditioning 時，也會附加到負向 conditioning。當模型期望一次使用多張參考影像，而非單一 latent 時，請使用此節點。

## 輸入

### 通用輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `positive` | 要使用參考 latent 修改的正向 conditioning。 | CONDITIONING | 是 | - |
| `negative` | 可選的負向 conditioning，會接收相同的參考 latent。保持未連接，即可在 `negative` 輸出上重複使用修改後的正向 conditioning。 | CONDITIONING | 否 | - |
| `vae` | 用於編碼已連接參考影像的 VAE。未連接 VAE 時，參考影像會被忽略。 | VAE | 否 | - |
| `resolution` | 每張參考影像在編碼前的準備方式。`"keep resolution"` 會以傳入尺寸進行編碼；`"resize"` 會將其縮放至目標百萬像素數，同時保留長寬比，這會顯示 `megapixels`。（預設值："keep resolution"） | DYNAMIC_COMBO | 是 | `"keep resolution"`<br>`"resize"` |
| `images` | 可增長插槽：連接一張或多張參考影像（`image_1`、`image_2`、...）以作為參考。影像會依插槽順序編碼，並依該順序附加至 conditioning。 | IMAGE | 否 | 1 至 100 |

### 調整尺寸輸入

當 `resolution` 設為 `"resize"` 時，會顯示這些選項。

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `megapixels` | 每張參考影像的目標尺寸，並保留長寬比。1.0 約為 1024 x 1024 像素。（預設值：1.0） | FLOAT | 是 | 0.01 至 16.0 |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `positive` | 已附加編碼後參考 latent 的正向 conditioning。 | CONDITIONING |
| `negative` | 已附加相同參考 latent 的負向 conditioning。若未連接任何負向 conditioning，則傳回正向輸出。 | CONDITIONING |
| `empty_latent` | 第一張參考 latent 乘以 0.0，可用於初始化 sampler。若未連接任何參考影像，則為空。 | LATENT |

## 備註

- latent 是附加而非取代，因此串接多個 Set Reference Multi Latent 節點會累積參考。
- 每張連接的影像會個別編碼，因此參考影像不必共用相同尺寸。
- 若未連接任何影像，`positive` 與 `negative` 會原樣傳回，且 `empty_latent` 為空。

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReferenceMultiLatent/zh-TW.md)

---
**Source fingerprint (SHA-256):** `06f98e7c21e8750a2bdf365cb80fac990bcf01246f183c60ef83bd195fc1225b`
