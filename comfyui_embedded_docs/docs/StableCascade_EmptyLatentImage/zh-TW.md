# StableCascade 空白潛在影像

StableCascade_EmptyLatentImage 節點為 Stable Cascade 模型建立空的潛在張量。它會產生兩個獨立的潛在表示——一個用於 stage C，另一個用於 stage B——其維度會根據輸入解析度與壓縮設定而決定。此節點提供了 Stable Cascade 生成管線的起點。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `寬度` | 輸出影像的寬度（像素）（預設值：1024，步長：8） | INT | 是 | 256 to MAX_RESOLUTION |
| `高度` | 輸出影像的高度（像素）（預設值：1024，步長：8） | INT | 是 | 256 to MAX_RESOLUTION |
| `壓縮` | 決定 stage C 潛在維度的壓縮因子（預設值：42，步長：1）。這是一個進階參數。 | INT | 是 | 4 至 128 |
| `批次大小` | 批次中要生成的潛在樣本數量（預設值：1） | INT | 否 | 1 至 4096 |

注意：`compression` 值控制 stage C 的潛在大小：其高度與寬度分別為輸入的 `height` 和 `width` 除以 `compression`。stage B 的潛在則固定使用 4 的壓縮倍率。

## 輸出

| 輸出名 | 描述 | 資料類型 |
| --- | --- | --- |
| `stage_c` | stage C 的潛在張量，維度為 [batch_size, 16, height//compression, width//compression] | LATENT |
| `stage_b` | stage B 的潛在張量，維度為 [batch_size, 4, height//4, width//4] | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_EmptyLatentImage/zh-TW.md)

---
**Source fingerprint (SHA-256):** `f336f87d0ec14b3716efda2cfaa194b1f80707d64821bb56ade7d88d9bd5b53f`
