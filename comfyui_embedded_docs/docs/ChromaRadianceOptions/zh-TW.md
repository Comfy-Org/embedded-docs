# ChromaRadiance 選項

ChromaRadianceOptions 節點可讓您為 Chroma Radiance 模型配置進階設定。它會包裝現有模型，並在去噪過程中根據 sigma 值套用特定選項，實現對 NeRF 平鋪大小及其他輻射相關參數的精細控制。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `模型` | 要套用 Chroma Radiance 選項的模型 | MODEL | 是 | - |
| `保留包裝器` | 啟用時，若存在現有的模型函式包裝器，將委派給它。通常應保持啟用。（預設：True） | BOOLEAN | 否 | - |
| `起始 sigma` | 這些選項生效的第一個 sigma 值。（預設：1.0） | FLOAT | 否 | 0.0 至 1.0 |
| `結束 sigma` | 這些選項生效的最後一個 sigma 值。（預設：0.0） | FLOAT | 否 | 0.0 至 1.0 |
| `NeRF 圖塊大小` | 允許覆寫預設的 NeRF 平鋪大小。設為 -1 表示使用預設值（32）；設為 0 表示使用非平鋪模式（可能消耗大量 VRAM）。（預設：-1） | INT | 否 | -1 and above |
| `強制使用連續文本標記ID` | 強制使用連續的文字 token ID，而不是零。應使用於 2026-05-22 至 2026-06-01 期間以這種方式訓練但 state dict 中不包含 `__sequential__` 鍵的檢查點。（預設：False） | BOOLEAN | 否 | - |

**注意：** Chroma Radiance 選項僅在目前 sigma 值介於 `end_sigma` 和 `start_sigma`（含）之間時生效。`nerf_tile_size` 參數僅在設為 0 或更高值時套用。`force_sequential_txt_ids` 參數僅在設為 True 時套用。當 `nerf_tile_size` 為 -1 且 `force_sequential_txt_ids` 為 False 時，不會設定任何選項，模型將原樣返回，不套用任何包裝器。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `model` | 套用 Chroma Radiance 選項後的模型；若沒有啟用任何選項，則為未更改的模型 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ChromaRadianceOptions/zh-TW.md)

---
**Source fingerprint (SHA-256):** `761f1946fe1fd77158e97f6f34d002e2445cc00e008741f8c37cde5673900409`
