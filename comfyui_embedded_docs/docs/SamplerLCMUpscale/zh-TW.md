# SamplerLCMUpscale

此節點提供一種專門的取樣方法，結合 Latent Consistency Model (LCM) 取樣與漸進式影像放大。在取樣期間，影像會使用所選的插值方法，逐步放大至目標縮放比例，讓單次取樣流程即可產生更高解析度的結果。此節點會輸出一個已設定的取樣器物件，可連接到取樣節點。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `縮放比例` | 放大期間要套用的總縮放係數。值為 1.0 時會維持原始解析度（預設：1.0） | FLOAT | 是 | 0.1 - 20.0 |
| `縮放步驟` | 用於放大過程的步數。使用 -1 時會根據取樣排程自動計算（預設：-1） | INT | 是 | -1 - 1000 |
| `放大方法` | 每個放大步驟中用於放大影像的插值方法（預設："bislerp"） | COMBO | 是 | "bislerp"<br>"nearest-exact"<br>"bilinear"<br>"area"<br>"bicubic" |

`scale_ratio` 和 `scale_steps` 是進階參數。影像會在其原始尺寸到目標 `scale_ratio` 之間，透過放大步驟逐步放大。當 `scale_steps` 為 -1 時，放大步數會自動計算為取樣步數的一半左右，且最少為 2；當提供正值時，節點會在內部進行調整，並根據取樣步數總數加以限制。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `sampler` | 一個已設定的取樣器物件，會執行具備漸進式放大的 LCM 取樣，可直接用於取樣流程中 | SAMPLER |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerLCMUpscale/zh-TW.md)

---
**Source fingerprint (SHA-256):** `5d6f6472fbb4d2c66a8a8b9d6dc34dcc52ac8272589fd6c29e4084d6cab3141b`
