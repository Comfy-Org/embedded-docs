# 3D 預覽（進階）

此節點提供進階的 3D 模型預覽功能，並輸出攝影機與模型資訊。它會將 3D 模型儲存至暫存檔案並在 UI 中顯示，同時將模型資料、攝影機資訊及視口尺寸傳遞至下游進行進一步處理。

## ## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|------|------|----------|------|------|
| `model_3d` | 來自上游 3D 節點的 3D 模型檔案。 | FILE3D | 是 | GLB、GLTF、FBX、OBJ、STL、USDZ 或任何支援的 3D 格式 |
| `model_3d_info` | 可選的模型資訊元資料。 | LOAD3DMODELINFO | 否 | - |
| `viewport_state` | 包含攝影機與模型資訊的當前視口狀態。 | LOAD3D | 是 | - |
| `camera_info` | 3D 視圖的可選攝影機配置。 | LOAD3DCAMERA | 否 | - |
| `寬度` | 預覽的像素寬度。 | INT | 是 | 1 至 4096（預設值：1024） |
| `高度` | 預覽的像素高度。 | INT | 是 | 1 至 4096（預設值：1024） |

## ## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|----------|------|----------|
| `model_3d` | 從輸入傳遞而來的 3D 模型檔案。 | FILE3D |
| `model_3d_info` | 模型資訊元資料，來自輸入或視口狀態。 | LOAD3DMODELINFO |
| `camera_info` | 攝影機配置，來自輸入或視口狀態。 | LOAD3DCAMERA |
| `寬度` | 預覽的像素寬度。 | INT |
| `高度` | 預覽的像素高度。 | INT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Preview3DAdvanced/zh-TW.md)

---
**Source fingerprint (SHA-256):** `7efe8720f88f7d6234387cd633ea629cbf43a0abea1a9aca6c5dcd43bf7f2145`
