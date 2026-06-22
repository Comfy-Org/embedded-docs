# Tripo P1：多視角轉模型

## 概述

此節點可從物體或角色的 2 到 4 張參考圖像生成 3D 模型。您提供不同角度（正面、左側、背面、右側）的圖像，節點便會建立 GLB 格式的 3D 網格。正面視圖為必填，您可以選擇性地添加其他三個視圖的任意組合以獲得更好的效果。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `圖片` | 正面視圖（0°）。必填。 | IMAGE | 是 | - |
| `左側圖片` | 左側視圖（90°），即主體的左側。 | IMAGE | 否 | - |
| `背面圖片` | 背面視圖（180°）。 | IMAGE | 否 | - |
| `右側圖片` | 右側視圖（270°），即主體的右側。 | IMAGE | 否 | - |
| `輸出模式` | 生成模型的輸出模式。`"geometry"` 產生原始網格，`"textured"` 添加標準紋理，`"detailed"` 建立高細節紋理模型（預設值：`"textured"`）。 | COMBO | 是 | `"geometry"`<br>`"textured"`<br>`"detailed"` |
| `面數上限` | 輸出網格的最大面數。設為 -1 表示無限制（預設值：-1）。 | INT | 否 | -1 至 100000 |
| `模型種子` | 用於可重現模型生成的種子。設為 0 表示隨機（預設值：0）。 | INT | 否 | 0 至 2147483647 |
| `自動尺寸` | 自動調整模型大小以符合標準邊界框（預設值：False）。 | BOOLEAN | 否 | True / False |
| `匯出 UV` | 匯出模型時包含 UV 座標（預設值：True）。 | BOOLEAN | 否 | True / False |
| `壓縮幾何` | 壓縮幾何資料以減少檔案大小（預設值：False）。 | BOOLEAN | 否 | True / False |

**注意：** 您必須至少提供 2 張圖像：正面視圖（`image`）加上至少一個其他視圖（`image_left`、`image_back` 或 `image_right`）。如果提供的圖像少於 2 張，節點將會報錯。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `模型任務 ID` | 生成的 GLB 模型檔案名稱（僅為向後相容性保留）。 | STRING |
| `GLB` | 此模型生成請求的唯一任務 ID。 | MODEL_TASK_ID |
| `GLB` | 以 GLB 格式生成的 3D 模型。 | FILE3DGLB |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoP1MultiviewToModelNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `29bb87cdc5d3eef891a653c622e8876a37d6e6dc1a43e5c248b184060ead9029`
