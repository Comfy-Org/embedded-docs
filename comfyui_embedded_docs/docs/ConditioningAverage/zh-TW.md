> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningAverage/zh-TW.md)

`ConditioningAverage` 節點用於根據指定的權重混合兩組不同的條件資料（例如文字提示），生成一個介於兩者之間的新條件向量。透過調整權重參數，您可以靈活控制每個條件資料對最終結果的影響。這特別適用於提示插值、風格融合和其他進階使用情境。

如下所示，透過調整 `conditioning_to` 的強度，可以輸出介於兩個條件資料之間的結果。

![example](./asset/example.webp)

## 輸入參數

| 參數名稱               | Comfy 資料類型 | 描述 |
|------------------------|---------------|-------------|
| `conditioning_to`      | `CONDITIONING`| 目標條件向量，作為加權平均的主要基礎。 |
| `conditioning_from`    | `CONDITIONING`| 來源條件向量，將根據特定權重混合到目標條件中。 |
| `conditioning_to_strength` | `FLOAT`    | 目標條件資料的強度，範圍 0.0-1.0，預設值 1.0，步長 0.01。 |

## 輸出參數

| 參數名稱        | Comfy 資料類型 | 描述 |
|------------------|---------------|-------------|
| `conditioning`   | `CONDITIONING`| 混合後產生的條件向量，反映加權平均的結果。 |

## 典型使用情境

- **提示插值：** 在兩個不同的文字提示之間平滑過渡，生成具有中間風格或語義的內容。
- **風格融合：** 結合不同的藝術風格或語義條件，創造新穎的效果。
- **強度調整：** 透過調整權重，精確控制特定條件資料對結果的影響。
- **創意探索：** 透過混合不同的提示，探索多樣化的生成效果。