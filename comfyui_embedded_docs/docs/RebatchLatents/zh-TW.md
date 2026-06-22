# 重新分批 Latents

RebatchLatents 節點旨在根據指定的批次大小，將一批潛在表示重新組織成新的批次配置。它確保潛在樣本被適當地分組，處理維度和尺寸的變化，以利於進一步的處理或模型推論。

## 輸入

| 參數 | 描述 | 資料類型 |
| --- | --- | --- |
| `latents` | 'latents' 參數代表要重新批次的輸入潛在表示。它對於決定輸出批次的結構和內容至關重要。 | `LATENT` |
| `批次大小` | 'batch_size' 參數指定輸出中每個批次所需的樣本數量。它直接影響輸入潛在表示分組和劃分為新批次的方式。 | `INT` |

## 輸出

| 參數 | 描述 | 資料類型 |
| --- | --- | --- |
| `latent` | 輸出是根據指定批次大小重新組織的潛在表示批次。它有助於進一步的處理或分析。 | `LATENT` |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RebatchLatents/zh-TW.md)
