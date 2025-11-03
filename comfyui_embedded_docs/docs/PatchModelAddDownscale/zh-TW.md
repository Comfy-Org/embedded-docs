> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PatchModelAddDownscale/zh-TW.md)

PatchModelAddDownscale 節點透過對模型中的特定區塊應用降尺度與升尺度操作，實現了 Kohya Deep Shrink 功能。它在處理過程中降低中間特徵的解析度，然後將其恢復到原始尺寸，這能在維持品質的同時提升效能。該節點允許精確控制在模型執行期間這些縮放操作發生的時機與方式。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | 是 | - | 要應用降尺度修補的模型 |
| `block_number` | INT | 否 | 1-32 | 要應用降尺度的特定區塊編號（預設值：3） |
| `downscale_factor` | FLOAT | 否 | 0.1-9.0 | 特徵降尺度的縮小係數（預設值：2.0） |
| `start_percent` | FLOAT | 否 | 0.0-1.0 | 降尺度開始的去噪過程起始點（預設值：0.0） |
| `end_percent` | FLOAT | 否 | 0.0-1.0 | 降尺度停止的去噪過程結束點（預設值：0.35） |
| `downscale_after_skip` | BOOLEAN | 否 | - | 是否在跳躍連接後應用降尺度（預設值：True） |
| `downscale_method` | COMBO | 否 | "bicubic"<br>"nearest-exact"<br>"bilinear"<br>"area"<br>"bislerp" | 用於降尺度操作的插值方法 |
| `upscale_method` | COMBO | 否 | "bicubic"<br>"nearest-exact"<br>"bilinear"<br>"area"<br>"bislerp" | 用於升尺度操作的插值方法 |

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `model` | MODEL | 已應用降尺度修補的修改後模型 |