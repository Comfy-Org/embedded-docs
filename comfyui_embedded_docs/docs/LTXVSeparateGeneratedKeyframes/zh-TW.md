# LTXV 分離生成的關鍵影格

## 概述

LTXV Separate Generated Keyframes 節點會將由 LTXV Add Generated Keyframes 添加的生成關鍵幀從採樣後的 latent 中分離出來，並從 conditioning 中移除它們。在用於空間上採樣視頻 latent 之前使用它。不要先運行 LTXV Crop Guides——它會將生成關鍵幀視為一次性引導並丟棄它們。

## 輸入

| 參數 | 描述 | 資料類型 | 必需 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `positive` | 正向 conditioning，包含生成關鍵幀的元數據。輸出時會從中移除元數據。 | CONDITIONING | 是 | N/A |
| `negative` | 負向 conditioning，包含生成關鍵幀的元數據。輸出時會從中移除元數據。 | CONDITIONING | 是 | N/A |
| `latent` | 視頻 latent，包含生成關鍵幀。輸出時會從中剝離這些關鍵幀。 | LATENT | 是 | N/A |
| `keyframes_to_batch` | 將關鍵幀作為單幀 latent 的批次返回。關閉此選項則會將它們作為一個多幀 latent 返回，這是 latent 上採樣器和後續的 Add Generated Keyframes 所期望的格式。 | BOOLEAN | 否 | default: False |

### 輸入注意事項

- `positive` 必須包含生成關鍵幀的元數據，否則節點會引發錯誤，提示您先使用 LTXV Add Generated Keyframes 添加它們。
- `latent` 必須是普通的視頻 latent（一個 5D 張量）。如果視頻和音頻 latent 仍合併在一起，請先使用 Separate AV Latent 將它們分開。
- 添加關鍵幀時記錄的每個 latent 幀的 token 數量必須與提供的 `latent` 的每幀 token 數量匹配。如果在添加關鍵幀後對 latent 進行了重新縮放，它們將不再對齊，節點會引發錯誤——請在對 latent 進行上採樣之前將它們分開。
- 記錄的關鍵幀幀範圍必須適合提供的 `latent` 內部，否則節點會引發錯誤，指出關鍵幀是針對不同的 latent 記錄的。
- 記錄的引導注意力條目索引必須仍然存在於 conditioning 中。如果在添加關鍵幀後重建了 conditioning，節點會引發錯誤。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `positive` | 已移除生成關鍵幀元數據的正向 conditioning。 | CONDITIONING |
| `negative` | 已移除生成關鍵幀元數據的負向 conditioning。 | CONDITIONING |
| `latent` | 已剝離生成關鍵幀的視頻 latent。 | LATENT |
| `keyframes` | 剝離出的關鍵幀，標記為 generated_keyframe_indices 和 generated_keyframe_num_frames。將這些饋送給後續的 Add Generated Keyframes 以初始化新槽位，或饋送給 Generated Keyframes To Guides 以將它們固定為凍結的圖像引導（如果畫布長度發生變化，索引會重新映射）。 | LATENT |

## 注意事項

- `keyframes_to_batch` 參數決定關鍵幀是作為單幀 latent 的批次返回，還是作為一個多幀 latent 返回。
- 該節點確保在進行任何進一步處理之前，從 conditioning 和 latent 中移除生成關鍵幀。
- `keyframes` 輸出可用於為生成關鍵幀初始化新槽位，或將它們固定為凍結的圖像引導。
- 如果 latent 不包含生成關鍵幀，或者關鍵幀與預期格式不匹配，節點會引發 `ValueError`。
- 該節點假設生成關鍵幀是使用 LTXV Add Generated Keyframes 節點添加的，並且它們與當前 latent 兼容。

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVSeparateGeneratedKeyframes/zh-TW.md)

---
**Source fingerprint (SHA-256):** `295e49181e87445a1c47b2e9413d95b20585b12e89f26f13129ac5d97f913007`
