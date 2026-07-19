# 重複 Latent 批次

### 概述

RepeatLatentBatch 節點旨在將給定的潛在表示批次複製指定次數，並可能包含噪聲遮罩和批次索引等附加數據。此功能對於需要相同潛在數據多個實例的操作至關重要，例如數據增強或特定的生成任務。

### 輸入

| 參數 | 描述 | 資料類型 |
| --- | --- | --- |
| `樣本` | 'samples' 參數代表要複製的潛在表示。它對於定義將進行重複的數據至關重要。 | `LATENT` |
| `數量` | 'amount' 參數指定輸入樣本應重複的次數。它直接影響輸出批次的大小，從而影響計算負載和生成數據的多樣性。 | `INT` |

### 輸出

| 參數 | 描述 | 資料類型 |
| --- | --- | --- |
| `latent` | 輸出是輸入潛在表示的修改版本，根據指定的 'amount' 進行複製。如果適用，它可能包含複製的噪聲遮罩和調整後的批次索引。 | `LATENT` |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RepeatLatentBatch/zh-TW.md)
