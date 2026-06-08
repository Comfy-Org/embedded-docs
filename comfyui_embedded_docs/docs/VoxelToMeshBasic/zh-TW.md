## 概述

VoxelToMeshBasic 節點可將 3D 體素資料轉換為網格幾何形狀。它透過套用閾值來處理體積資料，決定體積中的哪些部分會成為最終網格中的實體表面。此節點會輸出包含頂點和面的完整網格結構，可用於 3D 渲染和建模。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `voxel` | 要轉換為網格的 3D 體素資料 | VOXEL | 是 | - |
| `臨界值` | 用於決定哪些體素成為網格表面一部分的閾值（預設值：0.6） | FLOAT | 是 | -1.0 至 1.0 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `MESH` | 包含頂點和面的已生成 3D 網格 | MESH |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VoxelToMeshBasic/zh-TW.md)

---
**Source fingerprint (SHA-256):** `36df962c84c99a83f243a59b6387874e42e7d05323bd84079dbab112d2f1b67c`
