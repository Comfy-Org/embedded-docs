> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VoxelToMesh/zh-TW.md)

# VoxelToMeshBasic 節點

VoxelToMeshBasic 節點透過在指定的閾值下提取表面，將 3D 體素資料轉換為網格幾何形狀。它處理輸入中的每個體素網格，並生成構成 3D 網格表示的頂點和面。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `voxel` | VOXEL | 是 | - | 要轉換為網格幾何形狀的輸入體素資料 |
| `threshold` | FLOAT | 是 | -1.0 至 1.0 | 表面提取的閾值（預設值：0.6） |

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `MESH` | MESH | 生成的 3D 網格，包含來自所有輸入體素網格的疊加頂點和面 |

---
**Source fingerprint (SHA-256):** `36df962c84c99a83f243a59b6387874e42e7d05323bd84079dbab112d2f1b67c`
