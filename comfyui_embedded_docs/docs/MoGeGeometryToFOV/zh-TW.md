# MoGeGeometryToFOV

此節點從 MoGe 幾何物件中儲存的相機內參推導出視場角與焦距。它可以回傳垂直、水平或對角線的視場角（FOV），單位為度或弧度。垂直視場角輸出可用於例如饋送 SAM3DBody_Predict 節點。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `moge_geometry` | MoGe 幾何物件。它必須包含內參矩陣，以及 image、points 或 depth 資料中至少一種，用於讀取像素高度以進行焦距換算。 | MOGE_GEOMETRY | 是 | — |
| `軸` | 計算視場角所沿的軸：「vertical」(fov_y)、「horizontal」(fov_x) 或「diagonal」（預設：「vertical」）。 | COMBO | 是 | "vertical"<br>"horizontal"<br>"diagonal" |
| `單位` | 視場角輸出的單位（預設：「degrees」）。 | COMBO | 是 | "degrees"<br>"radians" |

注意：如果 `moge_geometry` 不包含內參（全景幾何沒有內參），或其中沒有 image、points、depth 任何一種資料，此節點將引發錯誤。

## 輸出

| 輸出名 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `fov` | 沿所選軸的視場角，單位為所選單位（度或弧度）。 | FLOAT |
| `focal_pixels` | 鏡頭焦距（以像素為單位），由垂直內參與像素高度推導而來。 | FLOAT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGeGeometryToFOV/zh-TW.md)

---
**Source fingerprint (SHA-256):** `983dc984847f93a8e002c73982571ecb38b7bae9c3dc4c201d9be17f785dcaed`
