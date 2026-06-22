# MediaPipe Face Mask

## 概述

此節點根據 MediaPipe 偵測到的臉部特徵點，建立一個二進位遮罩（黑白影像）。它會為每個偵測到的臉部區域繪製填充的多邊形形狀，並在批次中為每個影格產生一個遮罩。當同一個影格中偵測到多張臉部時，它們的遮罩會合併為單一遮罩。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `face_landmarks` | 來自 MediaPipe 臉部偵測節點的臉部特徵點資料。 | FACE_LANDMARKS | 是 | - |
| `regions` | 選擇要納入遮罩的臉部區域。`"all"` 會從所有臉部區域（臉部橢圓、嘴唇、眼睛、虹膜）的聯集建立遮罩。`"custom"` 則允許您個別切換每個區域。預設值：`"all"` | COMBO | 是 | `"all"`<br>`"custom"` |

當 `regions` 設定為 `"custom"` 時，以下額外的布林參數將變為可用：

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `face_oval` | 將臉部橢圓區域納入遮罩。預設值：True | BOOLEAN | 否 | True/False |
| `lips` | 將嘴唇區域納入遮罩。預設值：True | BOOLEAN | 否 | True/False |
| `eyes` | 將眼睛區域納入遮罩。預設值：True | BOOLEAN | 否 | True/False |
| `irises` | 將虹膜區域納入遮罩。預設值：True | BOOLEAN | 否 | True/False |

**注意：** 使用 `"all"` 模式時，遮罩會包含所有區域的組合。由於臉部橢圓區域已涵蓋其他區域，選擇 `"all"` 實際上會產生與僅選擇臉部橢圓區域相同的結果。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `MASK` | 一個二進位遮罩張量，其中臉部區域為白色（值 1.0），背景為黑色（值 0.0）。此遮罩具有與輸入影像相同的尺寸，並在批次中包含每個影格一個遮罩。 | MASK |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MediaPipeFaceMask/zh-TW.md)

---
**Source fingerprint (SHA-256):** `92270002a42ed59bc75e676a6881e1899186d3c8a1bb4dd4c0d39b3762b5bb66`
