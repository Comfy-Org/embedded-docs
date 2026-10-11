# Latent Operation Blend

此節點會建立一個 Latent 操作，將某個 Latent 朝參考 Latent 混合，並回傳該操作，以便接入諸如 Latent Apply Operation 或 Latent Apply Operation CFG 等節點。當參考項的空間尺寸不同時，會以最近鄰插值將其調整為目標 Latent 的尺寸；若參考項的批次較小，則會重複以符合目標批次大小。`strength` 為 0 時，Latent 保持不變。此節點標記為實驗性。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `reference` | 要朝其混合的 Latent。其樣本會轉換為正在處理的 Latent 的裝置與 dtype，然後調整尺寸並重複以與其相符。 | LATENT | 是 | - |
| `strength` | 朝 `reference` 混合的程度：0 會使 Latent 保持不變，1 會與調整尺寸後的參考 Latent 相符（預設：1.0）。 | FLOAT | 是 | 0.0 至 1.0 （步進值：0.0001） |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `operation` | 可套用於 Latent 樣本的混合操作。 | LATENT_OPERATION |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentOperationBlend/zh-TW.md)

---
**Source fingerprint (SHA-256):** `5890089afddf83ddd4edd992606509b118aac9ef13eb89589f73fa75e0b9dd5a`
