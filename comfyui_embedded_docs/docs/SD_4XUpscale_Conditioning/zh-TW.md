# SD_4XUpscale_Conditioning

此節點準備用於擴散模型的影像放大條件資料。它接收輸入影像與條件資料，接著套用縮放與雜訊增強，建立修改後的條件，以引導放大過程。節點會輸出正向與負向條件，以及對應放大尺寸的潛在表示。

## 輸入
| 參數 | 描述 | 資料類型 | 必須 | 範圍 |
| --- | --- | --- | --- | --- |
| `images` | 要放大的輸入影像 | IMAGE | 是 | - |
| `positive` | 引導生成朝向所需內容的正向條件資料 | CONDITIONING | 是 | - |
| `negative` | 引導生成遠離不希望內容的負向條件資料 | CONDITIONING | 是 | - |
| `scale_ratio` | 套用於輸入影像的縮放係數（預設：4.0） | FLOAT | 是 | 0.0 - 10.0 |
| `noise_augmentation` | 放大過程中加入的雜訊量（預設：0.0） | FLOAT | 是 | 0.0 - 1.0 |

目標放大尺寸是將輸入影像尺寸乘以 `scale_ratio` 計算而得。條件中所嵌入的影像以及輸出的潛在表示，皆以這些目標尺寸的四分之一建立。

## 輸出
| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `positive` | 已套用放大資訊的修改後正向條件 | CONDITIONING |
| `negative` | 已套用放大資訊的修改後負向條件 | CONDITIONING |
| `latent` | 符合放大尺寸的空潛在表示 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SD_4XUpscale_Conditioning/zh-TW.md)

---
**Source fingerprint (SHA-256):** `f215e890bd86f42d4da9c6f575fc92e65844e2e2056c5610310d8089e5d61902`
