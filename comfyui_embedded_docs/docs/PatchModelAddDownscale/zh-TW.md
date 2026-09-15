# PatchModelAddDownscale（Kohya Deep Shrink）

PatchModelAddDownscale（Kohya Deep Shrink）透過在選定的區塊縮小中間特徵，然後將其縮放回原始大小，對模型套用 Kohya Deep Shrink 技術。縮小僅在去噪過程的選定部分發生，這可以降低處理成本，同時保持最終結果接近原始結果。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 要套用降尺度修補的模型 | MODEL | 是 | - |
| `區塊編號` | 將套用降尺度的特定區塊編號（預設：3） | INT | 是 | 1-32 |
| `縮小比例` | 特徵降尺度的倍率（預設：2.0） | FLOAT | 是 | 0.1-9.0 |
| `起始百分比` | 去噪過程中降尺度開始的起始點（預設：0.0） | FLOAT | 是 | 0.0-1.0 |
| `結束百分比` | 去噪過程中降尺度停止的結束點（預設：0.35） | FLOAT | 是 | 0.0-1.0 |
| `跳過後縮小` | 是否在跳躍連接之後套用降尺度（預設：True） | BOOLEAN | 是 | - |
| `縮小方法` | 用於降尺度操作的插值方法（預設："bicubic"） | COMBO | 是 | "bicubic"<br>"nearest-exact"<br>"bilinear"<br>"area"<br>"bislerp" |
| `放大方法` | 用於升尺度操作的插值方法（預設："bicubic"） | COMBO | 是 | "bicubic"<br>"nearest-exact"<br>"bilinear"<br>"area"<br>"bislerp" |

降尺度修補僅在當前去噪步驟落在 `start_percent` 和 `end_percent` 所定義的範圍內，且僅在 `block_number` 所選取的區塊時才會套用。當啟用 `downscale_after_skip` 時，修補會在跳躍連接之後套用；停用時，則在跳躍連接之前套用。之後特徵會縮放回其原始大小，但僅在當前特徵大小不再符合降尺度前所記錄的大小時才會進行。

參數 `block_number`、`start_percent`、`end_percent` 和 `downscale_after_skip` 在節點介面中標記為進階選項。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `model` | 已套用降尺度修補的修改後模型 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PatchModelAddDownscale/zh-TW.md)

---
**Source fingerprint (SHA-256):** `aa9434a521ab585b290a3bd8db804469bd3bb02103a0d830b6be6eb8e8c26a5e`
