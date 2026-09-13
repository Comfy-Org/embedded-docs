# 體素轉網格

VoxelToMesh 節點會透過在指定閾值擷取表面，將 3D 體素資料轉換為網格幾何。它提供兩種表面擷取演算法：一種是 basic 方法，會建立簡單的盒狀面；另一種是 surface net 方法，可產生更平滑、更詳細的網格。此節點會處理輸入中的每個體素網格，並產生構成 3D 網格表示的頂點與面。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `voxel` | 要轉換為網格幾何的輸入體素資料 | VOXEL | 是 | - |
| `演算法` | 用於表面擷取的演算法。"surface net" 會產生較平滑的網格，而 "basic" 會建立簡單的盒狀面（預設值："surface net"） | COMBO | 是 | `"surface net"`<br>`"basic"` |
| `臨界值` | 表面擷取的閾值。值高於此閾值的體素會被視為實心（預設值：0.6） | FLOAT | 是 | -1.0 至 1.0 |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `MESH` | 產生的 3D 網格，包含所有輸入體素網格的頂點與面。如果所有體素網格產生的網格具有相同形狀，則輸出會是堆疊張量；否則會傳回可變長度的批次 | MESH |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VoxelToMesh/zh-TW.md)

---
**Source fingerprint (SHA-256):** `b600be13f1a484d8c0cc1f9c3918630d00c15d35008bcac0f677b21ef64b5d98`
