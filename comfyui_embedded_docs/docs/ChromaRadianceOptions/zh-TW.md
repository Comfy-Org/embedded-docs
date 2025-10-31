> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ChromaRadianceOptions/zh-TW.md)

ChromaRadianceOptions 節點允許您配置 Chroma Radiance 模型的高級設定。它會封裝現有模型，並在去噪過程中根據 sigma 值應用特定選項，從而實現對 NeRF 切片大小和其他輻射相關參數的微調控制。

## 輸入參數

| 參數名稱 | 資料類型 | 輸入類型 | 預設值 | 數值範圍 | 描述 |
|-----------|-----------|------------|---------|-------|-------------|
| `model` | MODEL | 必填 | - | - | 要應用 Chroma Radiance 選項的模型 |
| `preserve_wrapper` | BOOLEAN | 選填 | True | - | 啟用時，如果存在現有的模型函數封裝器，將會委派給它。通常應保持啟用狀態。 |
| `start_sigma` | FLOAT | 選填 | 1.0 | 0.0 - 1.0 | 這些選項開始生效的第一個 sigma 值。 |
| `end_sigma` | FLOAT | 選填 | 0.0 | 0.0 - 1.0 | 這些選項停止生效的最後一個 sigma 值。 |
| `nerf_tile_size` | INT | 選填 | -1 | -1 及以上 | 允許覆蓋預設的 NeRF 切片大小。-1 表示使用預設值 (32)。0 表示使用非切片模式（可能需要大量 VRAM）。 |

**注意：** Chroma Radiance 選項僅在當前 sigma 值落在 `end_sigma` 和 `start_sigma` 之間（包含邊界值）時生效。`nerf_tile_size` 參數僅在設定為 0 或更高值時才會被應用。

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `model` | MODEL | 已應用 Chroma Radiance 選項的修改後模型 |