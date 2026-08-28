# PatchModelAddDownscale（Kohya Deep Shrink）

PatchModelAddDownscale (Kohya Deep Shrink) 實作了 Kohya Deep Shrink 技術，透過對模型中的特定區塊套用縮小與放大操作。它會在處理期間降低中間特徵的解析度，然後將其恢復為原始大小，藉此在維持品質的同時提升效能。此節點可讓您在模型執行期間精確控制這些縮放操作的時機與方式。

## 輸入

| 參數 | 說明 | 資料型別 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 要套用縮小修補程式的模型 | MODEL | 是 | - |
| `區塊編號` | 將套用縮小操作的特定區塊編號（預設值：3） | INT | 是 | 1-32 |
| `縮小比例` | 縮小特徵的倍數（預設值：2.0） | FLOAT | 是 | 0.1-9.0 |
| `起始百分比` | 去噪過程中開始縮小的起始點（預設值：0.0） | FLOAT | 是 | 0.0-1.0 |
| `結束百分比` | 去噪過程中停止縮小的結束點（預設值：0.35） | FLOAT | 是 | 0.0-1.0 |
| `跳過後縮小` | 是否在跳躍連接之後套用縮小操作（預設值：True） | BOOLEAN | 是 | - |
| `縮小方法` | 用於縮小操作的插值方法 | COMBO | 是 | "bicubic"<br>"nearest-exact"<br>"bilinear"<br>"area"<br>"bislerp" |
| `放大方法` | 用於放大操作的插值方法 | COMBO | 是 | "bicubic"<br>"nearest-exact"<br>"bilinear"<br>"area"<br>"bislerp" |

縮小修補程式僅在目前去噪步驟落在 `start_percent` 和 `end_percent` 定義的範圍內，且僅在 `block_number` 選取的區塊上套用。當啟用 `downscale_after_skip` 時，修補程式會在跳躍連接之後套用；當停用時，則會在跳躍連接之前套用。

## 輸出

| 輸出名稱 | 說明 | 資料型別 |
| --- | --- | --- |
| `model` | 已套用縮小修補程式的修改後模型 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PatchModelAddDownscale/zh-TW.md)

---
**Source fingerprint (SHA-256):** `aa9434a521ab585b290a3bd8db804469bd3bb02103a0d830b6be6eb8e8c26a5e`
