# PatchModelAddDownscale 節點文檔

PatchModelAddDownscale 節點透過對模型中的特定區塊執行降採樣和升採樣操作，實現 Kohya Deep Shrink 功能。它在處理過程中降低中間特徵的解析度，然後將其恢復為原始大小，從而在保持品質的同時提升效能。此節點可精確控制這些縮放操作在模型執行期間的發生時間和方式。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 要套用降採樣修補的模型 | MODEL | 是 | - |
| `區塊編號` | 將套用降採樣的特定區塊編號（預設值：3） | INT | 否 | 1-32 |
| `縮小比例` | 降採樣特徵的倍數（預設值：2.0） | FLOAT | 否 | 0.1-9.0 |
| `起始百分比` | 降採樣開始的降噪過程起始點（預設值：0.0） | FLOAT | 否 | 0.0-1.0 |
| `結束百分比` | 降採樣結束的降噪過程終止點（預設值：0.35） | FLOAT | 否 | 0.0-1.0 |
| `跳過後縮小` | 是否在跳躍連接後套用降採樣（預設值：True） | BOOLEAN | 否 | - |
| `縮小方法` | 用於降採樣操作的插值方法 | COMBO | 否 | "bicubic"<br>"nearest-exact"<br>"bilinear"<br>"area"<br>"bislerp" |
| `放大方法` | 用於升採樣操作的插值方法 | COMBO | 否 | "bicubic"<br>"nearest-exact"<br>"bilinear"<br>"area"<br>"bislerp" |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `model` | 已套用降採樣修補的修改後模型 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PatchModelAddDownscale/zh-TW.md)

---
**Source fingerprint (SHA-256):** `93ece77ad2dce3c1cdd554583ae1f2e6be51a43ab072d408869dddbcc7798c40`
