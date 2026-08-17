# Reve 圖像生成

Reve Image Create 節點使用 Reve AI 模型，根據文字描述生成圖像。它會將文字提示詞傳送至 Reve API，並傳回生成的圖像。您可以控制圖像的長寬比，並套用選用的後處理效果，例如放大與移除背景。此節點已棄用。

## 輸入

### 通用輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | 用於生成的模型版本。選擇此模型會顯示 `aspect_ratio` 和 `test_time_scaling` 設定。 | DYNAMIC_COMBO | 是 | `"reve-create@20250915"` |
| `prompt` | 所需圖像的文字描述。最多 2560 個字元。預設值：空白。 | STRING | 是 | N/A |
| `seed` | `seed` 控制節點是否應重新執行；無論種子為何，結果都不具確定性。預設值：0。 | INT | 否 | 0 to 2147483647 |
| `upscale` | 放大生成的圖像。可能會增加額外費用。當設定為 `enabled` 時，會顯示 `upscale_factor` 設定。預設值：`disabled`。 | DYNAMIC_COMBO | 否 | `"disabled"`<br>`"enabled"` |
| `remove_background` | 移除生成圖像的背景。可能會增加額外費用。預設值：false。 | BOOLEAN | 否 | true<br>false |

### reve-create@20250915 輸入

當 `model` 設定為 `"reve-create@20250915"` 時，會顯示這些設定。

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `aspect_ratio` | 輸出圖像的長寬比。 | COMBO | 是 | `"3:2"`<br>`"16:9"`<br>`"9:16"`<br>`"2:3"`<br>`"4:3"`<br>`"3:4"`<br>`"1:1"` |
| `test_time_scaling` | 數值越高，生成的圖像品質越好，但會消耗更多點數。預設值：1。 | INT | 否 | 1 to 5 |

### 放大輸入

當 `upscale` 設定為 `"enabled"` 時，會顯示這些設定。

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `upscale_factor` | 放大倍率（2x、3x 或 4x）。預設值：2。 | INT | 否 | 2 to 4 (step 1) |

**注意：** `seed` 參數不保證輸出具有確定性。`upscale` 參數控制是否將放大作為後處理步驟套用。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `image` | 由 Reve 模型根據輸入提示詞所生成的圖像。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReveImageCreateNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `69178bc7d11e32ca179be5f598fbe60c4d41955b87e1c797e79cf224917a930c`
