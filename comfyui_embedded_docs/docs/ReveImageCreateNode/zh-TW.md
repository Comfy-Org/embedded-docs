# Reve 圖像生成

Reve Image Create 節點使用 Reve AI 模型從文字描述生成圖像。它會將提示詞傳送至 Reve API，並傳回生成的圖像，且可選擇進行放大與背景移除的後處理。此節點已棄用。

## 輸入

### 通用輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `模型` | 用於生成圖像的模型版本。 | DYNAMIC_COMBO | 是 | `"reve-create@20250915"` |
| `提示詞` | 所需圖像的文字描述。最多 2560 個字元。預設：""（空）。 | STRING | 是 | 1 至 2560 characters |
| `放大` | 放大生成的圖像。可能產生額外費用。預設：`"disabled"`。 | DYNAMIC_COMBO | 否 | `"disabled"`<br>`"enabled"` |
| `去背` | 移除生成圖像的背景。可能產生額外費用。預設：False。 | BOOLEAN | 否 | N/A |
| `種子` | `seed` 控制節點是否應重新執行；無論 `seed` 為何，結果皆為非確定性。預設：0。 | INT | 否 | 0 至 2147483647 |

### reve-create@20250915 輸入

當 `model` 設為 `"reve-create@20250915"` 時可用的選項：

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `aspect_ratio` | 輸出圖像的長寬比。 | COMBO | 是 | `"3:2"`<br>`"16:9"`<br>`"9:16"`<br>`"2:3"`<br>`"4:3"`<br>`"3:4"`<br>`"1:1"` |
| `test_time_scaling` | 較高的值會產生更好的圖像，但會消耗更多點數。預設：1。進階選項。 | INT | 否 | 1 至 5 |

### Upscale 輸入

當 `upscale` 設為 `"enabled"` 時可用的選項：

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `upscale_factor` | 放大倍率（2x、3x 或 4x）。預設：2。 | INT | 否 | 2 至 4 |

**注意：** `prompt` 必須包含 1 到 2560 個字元。`upscale_factor` 輸入只會在 `upscale` 設為 `"enabled"` 時出現。`seed` 參數不保證確定性輸出——無論 `seed` 值為何，結果皆為非確定性。`upscale` 與 `remove_background` 都可能產生額外費用。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `image` | Reve 模型根據輸入提示詞生成的圖像。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReveImageCreateNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `69178bc7d11e32ca179be5f598fbe60c4d41955b87e1c797e79cf224917a930c`
