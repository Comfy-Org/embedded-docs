# ChromaRadiance 選項

ChromaRadianceOptions 節點可讓您為 Chroma Radiance 模型設定進階選項。它會包裝現有的模型，並在去噪過程中根據 sigma 值套用特定選項，藉此精細控制 NeRF tile 大小及其他與輻射場相關的參數。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | 要套用 Chroma Radiance 選項的模型 | MODEL | 是 | - |
| `preserve_wrapper` | 啟用時，會委派給現有的模型函式包裝器（若存在）。一般應保持啟用。（預設值：True） | BOOLEAN | 否 | - |
| `start_sigma` | 這些選項生效的第一個 sigma 值。（預設值：1.0） | FLOAT | 否 | 0.0 至 1.0 |
| `end_sigma` | 這些選項生效的最後一個 sigma 值。（預設值：0.0） | FLOAT | 否 | 0.0 至 1.0 |
| `nerf_tile_size` | 允許覆寫預設的 NeRF tile 大小。-1 表示使用預設值（32）。0 表示使用非平鋪模式（可能需大量 VRAM）。（預設值：-1） | INT | 否 | -1 及以上 |
| `force_sequential_txt_ids` | 強制使用連續的文字 token ID，而非零值。應於 2026-05-22 至 2026-06-01 的 checkpoint 使用，這些 checkpoint 以此方式訓練，但 state dict 中不包含 `__sequential__` 鍵。（預設值：False） | BOOLEAN | 否 | - |

**注意：** Chroma Radiance 選項僅在目前的 sigma 值介於 `end_sigma` 與 `start_sigma`（含）之間時生效。`nerf_tile_size` 參數僅在設定為 0 或更高值時套用。`force_sequential_txt_ids` 參數僅在設定為 True 時套用。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `model` | 已套用 Chroma Radiance 選項的修改後模型 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ChromaRadianceOptions/zh-TW.md)

---
**Source fingerprint (SHA-256):** `761f1946fe1fd77158e97f6f34d002e2445cc00e008741f8c37cde5673900409`
