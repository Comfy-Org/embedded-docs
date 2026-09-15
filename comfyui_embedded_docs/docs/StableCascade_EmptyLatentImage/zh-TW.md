# StableCascade 空白潛在影像

`StableCascade_EmptyLatentImage` 節點會為 Stable Cascade 模型建立空的潛在張量。它會產生兩個獨立的潛在表示：一個用於 Stage C，另一個用於 Stage B，其維度會根據輸入解析度與壓縮設定計算得出。此節點為 Stable Cascade 生成管線提供起始點。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `寬度` | 輸出圖像的寬度（單位：像素，預設值：1024，步長：8） | INT | 是 | 256 to MAX_RESOLUTION |
| `高度` | 輸出圖像的高度（單位：像素，預設值：1024，步長：8） | INT | 是 | 256 to MAX_RESOLUTION |
| `壓縮` | 決定 Stage C 潛在維度的壓縮係數（預設值：42，步長：1）。這是進階參數。 | INT | 是 | 4 至 128 |
| `批次大小` | 一批中要產生的潛在樣本數量（預設值：1） | INT | 是 | 1 至 4096 |

注意：`compression` 值會控制 Stage C 潛在大小：其高度與寬度為輸入 `height` 與 `width` 除以 `compression`。Stage B 潛在表示一律使用固定壓縮值 4。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `stage_c` | Stage C 潛在張量，維度為 [batch_size, 16, height//compression, width//compression] | LATENT |
| `stage_b` | Stage B 潛在張量，維度為 [batch_size, 4, height//4, width//4] | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_EmptyLatentImage/zh-TW.md)

---
**Source fingerprint (SHA-256):** `f336f87d0ec14b3716efda2cfaa194b1f80707d64821bb56ade7d88d9bd5b53f`
