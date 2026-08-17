# 空白 Flux 轉 Latent

此節點會建立一個空白的潛在表示。它會產生一個填充為零的張量，作為 Flux 模型去噪過程的起點。潛在的維度由輸入的 `width` 和 `height` 決定，並以 16 為倍數縮小。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `width` | 要生成之最終影像的寬度。潛在寬度會是此值除以 16。預設值為 1024。 | INT | 是 | 16 至 16384 |
| `height` | 要生成之最終影像的高度。潛在高度會是此值除以 16。預設值為 1024。 | INT | 是 | 16 至 16384 |
| `batch_size` | 單一批次中要生成的潛在樣本數量。預設值為 1。 | INT | 否 | 1 至 4096 |

**注意：** `width` 和 `height` 輸入必須能被 16 整除，因為此節點會在內部將它們除以這個倍數來建立潛在維度。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `samples` | 一個填充為零的潛在張量。其形狀為 `[batch_size, 128, height // 16, width // 16]`。 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyFlux2LatentImage/zh-TW.md)

---
**Source fingerprint (SHA-256):** `f8356568f0ab521a3f246d1f672492e74f9a2f449694961b913bd14a5f0f3878`
