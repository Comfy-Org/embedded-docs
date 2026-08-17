# 3D 預覽（進階）

此節點提供進階的 3D 模型預覽功能，並輸出相機與模型資訊。它可預覽 3D 模型檔案，而不將該檔案儲存至 ComfyUI 的輸出目錄，而是將模型寫入暫存檔案以供 UI 顯示。模型資料、模型資訊、相機資訊與視埠尺寸也會一併傳遞，供下游進一步處理。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model_3d` | 來自上游 3D 節點的 3D 模型檔案。 | FILE3D | 是 | GLB, GLTF, FBX, OBJ, STL, USDZ, or any supported 3D format |
| `model_3d_info` | 選用的模型資訊中繼資料。 | LOAD3DMODELINFO | 否 | - |
| `viewport_state` | 目前包含相機與模型資訊的視埠狀態。 | LOAD3D | 是 | - |
| `camera_info` | 3D 視圖的選用相機組態。 | LOAD3DCAMERA | 否 | - |
| `width` | 預覽寬度（像素）。 | INT | 是 | 1 to 4096 (default: 1024) |
| `height` | 預覽高度（像素）。 | INT | 是 | 1 to 4096 (default: 1024) |

注意：當 `camera_info` 未連接時，節點會使用 `viewport_state` 中的 `camera_info` 值。當 `model_3d_info` 未連接時，節點會使用 `viewport_state` 中的 `model_3d_info` 值；若視埠狀態中沒有該值，則使用空清單。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `model_3d` | 從輸入傳遞而來的 3D 模型檔案。 | FILE3D |
| `model_3d_info` | 模型資訊中繼資料，來自輸入或視埠狀態。 | LOAD3DMODELINFO |
| `camera_info` | 相機組態，來自輸入或視埠狀態。 | LOAD3DCAMERA |
| `width` | 預覽寬度（像素）。 | INT |
| `height` | 預覽高度（像素）。 | INT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Preview3DAdvanced/zh-TW.md)

---
**Source fingerprint (SHA-256):** `eda8c8fdd6ce7c39caf00c3054fc58e6dcab124fc3774d17af2deae651fbbf2e`
