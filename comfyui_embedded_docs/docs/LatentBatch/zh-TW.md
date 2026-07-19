# 潛空間批次

LatentBatch 節點旨在將兩組潛在樣本合併為單一批次，並在合併前根據需要調整其中一組的尺寸以匹配另一組。此操作有助於結合不同的潛在表示，以便進行後續處理或生成任務。

## 輸入

| 參數 | 說明 | 資料類型 |
| --- | --- | --- |
| `samples1` | 第一組要合併的潛在樣本。它在決定合併後批次的最終形狀方面扮演關鍵角色。 | `LATENT` |
| `samples2` | 第二組要合併的潛在樣本。若其尺寸與第一組不同，則會調整大小以確保合併前的相容性。 | `LATENT` |

## 輸出

| 參數 | 說明 | 資料類型 |
| --- | --- | --- |
| `latent` | 合併後的潛在樣本組，現已結合成單一批次，可供後續處理使用。 | `LATENT` |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentBatch/zh-TW.md)
