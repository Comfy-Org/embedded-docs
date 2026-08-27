# MoGeGeometryToFOV

此節點從 MoGe 幾何物件中儲存的相機內參數推導出視野與焦距。可回傳垂直、水平或對角線視野，單位可為度或弧度。例如，垂直視野輸出可用於提供給 SAM3DBody_Predict 節點。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `moge_geometry` | MoGe 幾何物件。必須包含內參數矩陣，以及影像（image）、點雲（points）或深度（depth）資料中的至少一項；這些資料用於讀取像素高度，以進行焦距換算。 | MOGE_GEOMETRY | 是 | — |
| `axis` | 計算視野所沿用的軸：``"vertical"``（fov_y）、``"horizontal"``（fov_x）或 ``"diagonal"``（預設：``"vertical"``）。 | COMBO | 是 | ``"vertical"``<br>``"horizontal"``<br>``"diagonal"`` |
| `unit` | 視野的輸出單位（預設：``"degrees"``）。 | COMBO | 是 | ``"degrees"``<br>``"radians"`` |

注意：若 `moge_geometry` 不包含內參數（全景幾何沒有內參數），或其中既不包含影像、點雲也不包含深度資料，則此節點會擲回錯誤。

## 輸出

| 輸出名 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `fov` | 沿所選軸的視野，以所選單位（度或弧度）表示。 | FLOAT |
| `focal_pixels` | 以像素為單位的透鏡焦距，由垂直內參數與像素高度推導得出。 | FLOAT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGeGeometryToFOV/zh-TW.md)

---
**Source fingerprint (SHA-256):** `983dc984847f93a8e002c73982571ecb38b7bae9c3dc4c201d9be17f785dcaed`
