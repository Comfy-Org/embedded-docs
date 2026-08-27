# 萬幻影主體轉影片

WanPhantomSubjectToVideo 節點為 Wan 影片生成準備條件數據和潛在空間。它根據請求的寬度、高度、長度和批次大小建立一個空的潛在影片，並在提供參考圖片時，使用 VAE 對其進行編碼，並將其作為時間維度的視覺引導添加到條件中。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `正面提示` | 用於引導影片生成的正向條件 | CONDITIONING | 是 | - |
| `負面提示` | 負向條件，用於避免特定特徵 | CONDITIONING | 是 | - |
| `VAE` | 當提供參考圖片時，用於對這些圖片進行編碼的 VAE 模型 | VAE | 是 | - |
| `寬度` | 輸出影片的寬度（像素，預設值：832，必須是 16 的倍數） | INT | 是 | 16 to MAX_RESOLUTION |
| `高度` | 輸出影片的高度（像素，預設值：480，必須是 16 的倍數） | INT | 是 | 16 to MAX_RESOLUTION |
| `長度` | 生成影片的幀數（預設值：81，必須是 4 的倍數） | INT | 是 | 1 to MAX_RESOLUTION |
| `批次大小` | 同時生成的影片數量（預設值：1） | INT | 是 | 1 至 4096 |
| `圖片` | 可選的參考圖片，用作時間維度的視覺引導 | IMAGE | 否 | - |

**注意：** 當提供 `images` 時，它們會自動放大以符合指定的 `width` 和 `height`，且僅使用前 `length` 張圖片進行處理。每張圖片會使用 `vae` 進行編碼，並沿時間維度進行拼接，且僅使用每張圖片的 RGB 通道。

## 輸出

| 輸出名 | 描述 | 資料類型 |
| --- | --- | --- |
| `正面提示` | 當提供圖片時，包含已編碼參考圖片的時間維度拼接的正向條件；否則回傳未變更的輸入 `positive` | CONDITIONING |
| `負面文字` | 當提供圖片時，包含已編碼參考圖片的時間維度拼接的負向條件；否則回傳未變更的輸入 `negative` | CONDITIONING |
| `負面圖片文字` | 當提供圖片時，包含零填充時間維度拼接的負向條件；否則回傳未變更的輸入 `negative` | CONDITIONING |
| `潛在空間` | 零填充的潛在影片張量，具有 16 個通道；其幀數由 `length` 決定，空間尺寸由 `height` 和 `width` 決定 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanPhantomSubjectToVideo/zh-TW.md)

---
**Source fingerprint (SHA-256):** `a1853382f6e564f66262b69dd7b06cc58e26b93386a460a98e6fcc2ff6acf12b`
