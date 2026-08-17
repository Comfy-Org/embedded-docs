# PatchModelAddDownscale（Kohya Deep Shrink）

PatchModelAddDownscale 節點透過對模型中的特定區塊執行下採樣和上採樣操作，實作 Kohya Deep Shrink 功能。它在處理過程中降低中間特徵的解析度，然後將其恢復到原始大小，這可以在維持品質的同時提升效能。此節點允許精確控制這些縮放操作在模型執行期間的發生時間與方式。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 要套用下採樣修補的模型 | MODEL | 是 | - |
| `block_number` | 將套用下採樣的特定區塊編號（預設值：3） | INT | 否 | 1-32 |
| `downscale_factor` | 用於下採樣特徵的倍率（預設值：2.0） | FLOAT | 否 | 0.1-9.0 |
| `start_percent` | 去噪過程中開始下採樣的位置（預設值：0.0） | FLOAT | 否 | 0.0-1.0 |
| `end_percent` | 去噪過程中停止下採樣的位置（預設值：0.35） | FLOAT | 否 | 0.0-1.0 |
| `downscale_after_skip` | 是否在跳躍連線之後套用下採樣（預設值：True） | BOOLEAN | 否 | - |
| `downscale_method` | 用於下採樣操作的內插方法 | COMBO | 否 | "bicubic"<br>"nearest-exact"<br>"bilinear"<br>"area"<br>"bislerp" |
| `upscale_method` | 用於上採樣操作的內插方法 | COMBO | 否 | "bicubic"<br>"nearest-exact"<br>"bilinear"<br>"area"<br>"bislerp" |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `model` | 已套用下採樣修補的修改後模型 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PatchModelAddDownscale/zh-TW.md)

---
**Source fingerprint (SHA-256):** `aa9434a521ab585b290a3bd8db804469bd3bb02103a0d830b6be6eb8e8c26a5e`
