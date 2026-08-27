# SamplerLCMUpscale

此節點提供了一種結合潛在一致性模型（LCM）取樣與圖像放大功能的專門取樣方法。它在取樣過程中透過多種插值方法逐步放大圖像，使得可以在單次取樣流程中生成更高解析度的輸出。輸出是一個已配置的取樣器物件，可連接到取樣節點。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `縮放比例` | 放大期間套用的總縮放比例。值為 1.0 時保持原始解析度（預設值：1.0） | FLOAT | 是 | 0.1 - 20.0 |
| `縮放步驟` | 用於放大過程的步驟數。使用 -1 可根據取樣排程自動計算（預設值：-1） | INT | 是 | -1 - 1000 |
| `放大方法` | 每個放大步驟中用於圖像放大的插值方法（預設值："bislerp"） | COMBO | 是 | "bislerp"<br>"nearest-exact"<br>"bilinear"<br>"area"<br>"bicubic" |

`scale_ratio` 和 `scale_steps` 是進階參數。圖像會從原始大小逐步放大到目標 `scale_ratio`，並在放大步驟中平均分配。當 `scale_steps` 為 -1 時，放大步驟數會自動計算為約為取樣步驟數的一半，且最小值為 2；當提供正值時，節點會在內部調整該值，並根據總取樣步驟數進行限制。

## 輸出

| 輸出名 | 描述 | 資料類型 |
| --- | --- | --- |
| `sampler` | 一個已配置的取樣器物件，可執行帶有逐步放大的 LCM 取樣，可直接用於取樣管線 | SAMPLER |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerLCMUpscale/zh-TW.md)

---
**Source fingerprint (SHA-256):** `5d6f6472fbb4d2c66a8a8b9d6dc34dcc52ac8272589fd6c29e4084d6cab3141b`
