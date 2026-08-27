# SD_4XUpscale_Conditioning

SD_4XUpscale_Conditioning 節點用於準備擴散模型影像放大所需的條件資料。它接收輸入影像與條件資料，套用縮放與雜訊增強，產生修改後的條件，以引導放大過程。此節點輸出正向與負向條件，以及對應放大尺寸的潛在表示。

## 輸入

| 參數 | 說明 | 資料類型 | 是否必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `images` | 要進行放大的輸入影像 | IMAGE | 是 | - |
| `正向` | 正向條件資料，用於引導生成朝向期望的內容 | CONDITIONING | 是 | - |
| `負向` | 負向條件資料，用於引導生成遠離不想要的內容 | CONDITIONING | 是 | - |
| `縮放比例` | 套用到輸入影像的縮放倍率（預設值：4.0） | FLOAT | 否 | 0.0 - 10.0 |
| `雜訊增強` | 放大過程中加入的雜訊量（預設值：0.0） | FLOAT | 否 | 0.0 - 1.0 |

注意：`noise_augmentation` 為進階參數，在節點介面中顯示於「進階」（Advanced）切換區域。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `正向` | 已套用放大資訊的修改後正向條件 | CONDITIONING |
| `負向` | 已套用放大資訊的修改後負向條件 | CONDITIONING |
| `潛在空間` | 對應放大尺寸的空潛在表示 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SD_4XUpscale_Conditioning/zh-TW.md)

---
**Source fingerprint (SHA-256):** `f215e890bd86f42d4da9c6f575fc92e65844e2e2056c5610310d8089e5d61902`
