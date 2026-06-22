# 跳層引導DiT簡易版

這是 SkipLayerGuidanceDiT 節點的簡化版本，僅在去噪過程中修改無條件傳遞。此節點透過根據指定的時機和層參數，在無條件傳遞期間選擇性地跳過 DiT（擴散變壓器）模型中的特定變壓器層，來對這些層應用跳層引導。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `模型` | 要套用跳層引導的模型 | MODEL | 是 | - |
| `雙層` | 要跳過的雙區塊層索引，以逗號分隔（預設："7, 8, 9"） | STRING | 否 | - |
| `單層` | 要跳過的單區塊層索引，以逗號分隔（預設："7, 8, 9"） | STRING | 否 | - |
| `起始百分比` | 跳層引導開始時的去噪過程起始百分比（預設：0.0） | FLOAT | 否 | 0.0 - 1.0 |
| `結束百分比` | 跳層引導停止時的去噪過程結束百分比（預設：1.0） | FLOAT | 否 | 0.0 - 1.0 |

**注意：** 僅當 `double_layers` 和 `single_layers` 都包含有效的層索引時，才會套用跳層引導。如果兩者皆為空，則節點會回傳未經修改的原始模型。跳層引導僅在當前去噪步驟的 sigma 值落在 `start_percent` 和 `end_percent` 之間（內部會轉換為 sigma 值）時才會生效。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `模型` | 已對指定層套用跳層引導的修改後模型 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SkipLayerGuidanceDiTSimple/zh-TW.md)

---
**Source fingerprint (SHA-256):** `6795a67a63d9aa8b2adea3d96e49272d88c21d0642bb507e175a2fcf3a125f98`
