> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PatchModelAddDownscale/zh-TW.md)

PatchModelAddDownscale 節點透過對模型中的特定區塊應用降取樣和升取樣操作，實現了 Kohya Deep Shrink 功能。它在處理過程中降低中間特徵的解析度，然後將其恢復到原始大小，這可以在保持質量的同時提升效能。該節點允許精確控制在模型執行過程中這些縮放操作發生的時機和方式。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | 是 | - | 要應用降取樣修補的模型 |
| `區塊編號` | INT | 否 | 1-32 | 將應用降取樣的特定區塊編號（預設值：3） |
| `縮小比例` | FLOAT | 否 | 0.1-9.0 | 特徵降取樣的縮放係數（預設值：2.0） |
| `起始百分比` | FLOAT | 否 | 0.0-1.0 | 降取樣開始的去噪過程起始點（預設值：0.0） |
| `結束百分比` | FLOAT | 否 | 0.0-1.0 | 降取樣停止的去噪過程結束點（預設值：0.35） |
| `跳過後縮小` | BOOLEAN | 否 | - | 是否在跳躍連接後應用降取樣（預設值：True） |
| `縮小方法` | COMBO | 否 | "bicubic"<br>"nearest-exact"<br>"bilinear"<br>"area"<br>"bislerp" | 用於降取樣操作的插值方法 |
| `放大方法` | COMBO | 否 | "bicubic"<br>"nearest-exact"<br>"bilinear"<br>"area"<br>"bislerp" | 用於升取樣操作的插值方法 |

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `model` | MODEL | 已應用降取樣修補的修改後模型 |