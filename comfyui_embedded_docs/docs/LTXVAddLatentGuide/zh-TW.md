# LTXV 新增 Latent 引導

LTXV Add Latent Guide 節點會將已編碼的 latent 固定為引導，適用於引導來自較早階段而非影像的情況。其效果與 LTXV Add Guide 相同，但不需要進行 VAE 解碼/編碼的來回處理。當引導的空間尺寸小於目標（例如 IC-LoRA 或細節化參考）時，會將其膨脹到稀疏網格上，並以相同比例擴展其 RoPE 結束位置，使其涵蓋目標畫布，而不只侷限於目標畫布的左上角。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `positive` | 正向條件輸入。 | CONDITIONING | 是 | N/A |
| `negative` | 負向條件輸入。 | CONDITIONING | 是 | N/A |
| `vae` | 用於讀取影格放置之下採樣索引公式的 VAE 模型。 | VAE | 是 | N/A |
| `latent` | 引導要固定到的目標影片 latent。 | LATENT | 是 | N/A |
| `guiding_latent` | 引導 latent。其空間尺寸在兩個軸上都必須以相同整數整除目標的空間尺寸；尺寸相等時會依原樣固定，尺寸為一半時會視為 x2 IC-LoRA 參考。 | LATENT | 是 | N/A |
| `latent_idx` | 開始放置引導的 latent 影格索引，以 latent 影格而非像素影格計算。負值會將引導放置在 latent 起點之前的影格，而不是從其結尾往回計算。預設：0。 | INT | 是 | -9999 至 9999 |
| `strength` | 上限為 1.0。膨脹後的引導會以負的去噪遮罩標記其填充位置，讓模型捨棄這些位置；若高於 1.0，保留位置也會變成負值，導致整個引導被捨棄。若要放大到超過 1.0，請改用 `attention_mask`。預設：1.0。 | FLOAT | 是 | 0.0 至 1.0, step 0.01 |
| `attention_mask` | 可選的像素空間空間遮罩。透過自注意力控制各區域的條件影響，並乘以 `strength`。 | MASK | 否 | N/A |

### 備註

- `latent` 與 `guiding_latent` 都必須是 5D 影片 latent，形狀為 (batch, channels, frames, height, width)。
- 引導必須能容納於目標 latent 內：引導的影格數加上 `latent_idx` 後，不得超出目標 latent 的結尾。允許使用負的 `latent_idx` 值，這會將引導放置在 latent 起點之前。
- 引導的空間尺寸在高度軸與寬度軸上，都必須能以整數整除目標的空間尺寸。
- 高度比例與寬度比例必須相同（正方形比例）。非正方形比例會引發錯誤，因為膨脹與 RoPE 放置會對兩個軸使用單一的下採樣係數。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `positive` | 已附加引導的正向條件。 | CONDITIONING |
| `negative` | 已附加引導的負向條件。 | CONDITIONING |
| `latent` | 已套用引導的 latent 輸出，包含更新後的 `noise_mask`。 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAddLatentGuide/zh-TW.md)

---
**Source fingerprint (SHA-256):** `19542500484dbc57fdbeeab8ba05bc2978246b3be5decc413825f616cab46f73`
