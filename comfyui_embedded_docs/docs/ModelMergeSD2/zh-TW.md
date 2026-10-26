# 模型合併 (SD2)

ModelMergeSD2 節點會透過混合兩個 Stable Diffusion 2.x 模型中相對應的元件來合併它們，並針對時間嵌入、標籤嵌入，以及每個輸入、中間與輸出區塊分別提供獨立權重。其區塊配置與 ModelMergeSD1 相同，因此這兩個節點會提供同一組比例參數。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `模型 1` | 要合併的第一個模型。第二個模型未貢獻的部分皆保留自這個模型 | MODEL | 是 | - |
| `模型 2` | 要合併的第二個模型。其權重會依照下列比例混合進來 | MODEL | 是 | - |
| `time_embed.` | 時間嵌入層的混合比例（預設值：1.0） | FLOAT | 是 | 0.0 至 1.0 （步進值：0.01） |
| `label_emb.` | 標籤嵌入層的混合比例（預設值：1.0） | FLOAT | 是 | 0.0 至 1.0 （步進值：0.01） |
| `input_blocks.0.` 至 `input_blocks.11.` | 12 個輸入區塊各自的混合比例（預設值：1.0） | FLOAT | 是 | 0.0 至 1.0 （步進值：0.01） |
| `middle_block.0.` 至 `middle_block.2.` | 3 個中間區塊各自的混合比例（預設值：1.0） | FLOAT | 是 | 0.0 至 1.0 （步進值：0.01） |
| `output_blocks.0.` 至 `output_blocks.11.` | 12 個輸出區塊各自的混合比例（預設值：1.0） | FLOAT | 是 | 0.0 至 1.0 （步進值：0.01） |
| `out.` | 輸出層的混合比例（預設值：1.0） | FLOAT | 是 | 0.0 至 1.0 （步進值：0.01） |

比例為 0.0 時，該元件會維持 `model1` 中的原樣；比例為 1.0 時，則完全取自 `model2`；介於兩者之間的值會產生加權混合。兩個輸入都必須是具備相同區塊結構的 Stable Diffusion 2.x 模型。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `MODEL` | 合併後的模型，會依照指定比例組合兩個輸入 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeSD2/zh-TW.md)

---
**Source fingerprint (SHA-256):** `b9d53f126139412fbd8b21be72e1dcdb02736519ab4dc9e28c7840d69acb7c87`
