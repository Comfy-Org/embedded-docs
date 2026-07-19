# 萬幻影主體轉影片

WanPhantomSubjectToVideo 節點透過處理條件化輸入和可選的參考影像來生成影片內容。它會建立用於影片生成的潛在表示，並在提供輸入影像時納入視覺引導。此節點為影片模型準備具有時間維度串接的條件化資料，並輸出修改後的條件化資料以及生成的潛在影片資料。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `正面提示` | 用於引導影片生成的正向條件化輸入 | CONDITIONING | 是 | - |
| `負面提示` | 用於避免特定特徵的負向條件化輸入 | CONDITIONING | 是 | - |
| `VAE` | 用於在提供影像時進行編碼的 VAE 模型 | VAE | 是 | - |
| `寬度` | 輸出影片的寬度（像素）（預設值：832，必須能被 16 整除） | INT | 是 | 16 至 MAX_RESOLUTION |
| `高度` | 輸出影片的高度（像素）（預設值：480，必須能被 16 整除） | INT | 是 | 16 至 MAX_RESOLUTION |
| `長度` | 生成影片的幀數（預設值：81，必須能被 4 整除） | INT | 是 | 1 至 MAX_RESOLUTION |
| `批次大小` | 同時生成的影片數量（預設值：1） | INT | 是 | 1 至 4096 |
| `圖片` | 用於時間維度條件化的可選參考影像 | IMAGE | 否 | - |

**注意：** 當提供 `images` 時，它們會自動放大以符合指定的 `width` 和 `height`，並且僅使用前 `length` 幀進行處理。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `正面提示` | 當提供影像時，經過時間維度串接修改後的正向條件化資料 | CONDITIONING |
| `負面文字` | 當提供影像時，經過時間維度串接修改後的負向條件化資料 | CONDITIONING |
| `負面圖片文字` | 當提供影像時，具有歸零時間維度串接的負向條件化資料 | CONDITIONING |
| `潛在空間` | 生成的潛在影片表示，具有指定的尺寸和長度 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanPhantomSubjectToVideo/zh-TW.md)

---
**Source fingerprint (SHA-256):** `2e3e8277dca9e998220fc5939c2cc72fdc15e80cc4b95daa33f5b92e2270dd73`
