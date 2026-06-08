## 概述
LatentSubtract 節點設計用於從一個潛在表示中減去另一個潛在表示。此操作可透過有效移除一個潛在空間中所代表的特徵或屬性，來操縱或修改生成模型輸出的特性。

## 輸入
| 參數 | 說明 | 資料類型 |
| --- | --- | --- |
| `samples1` | 作為被減數的第一組潛在樣本，是減法運算的基礎。 | `LATENT` |
| `samples2` | 將從第一組樣本中減去的第二組潛在樣本。此操作可透過移除屬性或特徵來改變生成模型的輸出結果。 | `LATENT` |

## 輸出
| 參數 | 說明 | 資料類型 |
| --- | --- | --- |
| `latent` | 從第一組潛在樣本中減去第二組潛在樣本的結果。此修改後的潛在表示可用於進一步的生成任務。 | `LATENT` |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentSubtract/zh-TW.md)
