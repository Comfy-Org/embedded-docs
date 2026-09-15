# 空白 Flux 轉 Latent

Empty Flux 2 Latent 節點會建立一個以零填充的空白潛在表示。它用於作為 Flux 模型去噪過程的起始點。潛在維度取自輸入的 `width` 和 `height`，並各自除以 16。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `寬度` | 要生成的最終影像寬度。潛在寬度將為此值除以 16。預設值為 1024。 | INT | 是 | 16 至 16384 |
| `高度` | 要生成的最終影像高度。潛在高度將為此值除以 16。預設值為 1024。 | INT | 是 | 16 至 16384 |
| `批次大小` | 單一批次中要生成的潛在樣本數量。預設值為 1。 | INT | 否 | 1 至 4096 |

**注意：** `width` 和 `height` 輸入使用步長 16，因此它們必須能被 16 整除。這是因為此節點會將它們除以這個因數來建立潛在維度。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `samples` | 一個以零填充的潛在張量。形狀為 `[batch_size, 128, height // 16, width // 16]`。 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyFlux2LatentImage/zh-TW.md)

---
**Source fingerprint (SHA-256):** `f8356568f0ab521a3f246d1f672492e74f9a2f449694961b913bd14a5f0f3878`
