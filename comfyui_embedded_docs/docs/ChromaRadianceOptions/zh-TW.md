# ChromaRadiance 選項

The ChromaRadianceOptions 節點允許您為 Chroma Radiance 模型配置進階設定。它會將包裝器附加到現有模型，並且僅在當前 sigma 值落在所配置的範圍內時，於去雜訊過程中套用所選選項，從而控制 NeRF tile 大小與文字 token ID 的處理方式。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `模型` | 要套用 Chroma Radiance 選項的模型 | MODEL | 是 | - |
| `保留包裝器` | 啟用時，若存在現有的模型函式包裝器，則會委派給它。通常應保持啟用。（預設：True） | BOOLEAN | 否 | - |
| `起始 sigma` | 這些選項將生效的第一個 sigma。（預設：1.0） | FLOAT | 否 | 0.0 至 1.0 |
| `結束 sigma` | 這些選項將生效的最後一個 sigma。（預設：0.0） | FLOAT | 否 | 0.0 至 1.0 |
| `NeRF 圖塊大小` | 允許覆寫預設的 NeRF tile 大小。-1 表示使用預設值（32）。0 表示使用非 tile 模式（可能需要大量 VRAM）。（預設：-1） | INT | 否 | -1 and above |
| `強制使用連續文本標記ID` | 強制使用循序文字 token ID，而非零值。應使用於 2026-05-22 到 2026-06-01 之間、以這種方式訓練，但 state dict 中不包含 `__sequential__` 鍵的檢查點。（預設：False） | BOOLEAN | 否 | - |

**注意：** Chroma Radiance 選項僅在當前 sigma 值落在 `end_sigma` 與 `start_sigma` 之間（含端點）時才會生效。`nerf_tile_size` 選項僅在設為 0 或更高值時才會套用（值為 -1 時會使用預設 tile 大小 32，且不會儲存任何覆寫）。`force_sequential_txt_ids` 選項僅在設為 True 時才會套用。當 `nerf_tile_size` 為 -1 且 `force_sequential_txt_ids` 為 False 時，不會配置任何選項，模型會以未變更的形式傳回，且不會套用任何包裝器。

**注意：** 除了 `model` 以外的所有輸入皆為進階選項。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `model` | 已套用 Chroma Radiance 選項的模型；若沒有作用中的選項，則為未變更的模型 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ChromaRadianceOptions/zh-TW.md)

---
**Source fingerprint (SHA-256):** `761f1946fe1fd77158e97f6f34d002e2445cc00e008741f8c37cde5673900409`
