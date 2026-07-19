# Save3DAdvanced

此節點將 3D 模型儲存到 ComfyUI 輸出目錄中的檔案，並提供對輸出尺寸及攝影機/視埠設定的進階控制。它也會將 3D 模型、模型資訊、攝影機資訊和尺寸傳遞給下游節點。

## ## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model_3d` | 來自上游 3D 節點的 3D 模型檔案。 | FILE3D | 是 | GLB, GLTF, FBX, OBJ, STL, USDZ, Any |
| `filename_prefix` | 儲存檔案名稱的前綴（預設："3d/ComfyUI"）。 | STRING | 是 | 自由文字 |
| `viewport_state` | 來自「載入 3D」節點的視埠狀態，包含攝影機和模型資訊。 | LOAD3D | 是 | - |
| `model_3d_info` | 可選的 3D 模型資訊，用於覆蓋視埠狀態。 | LOAD3DMODELINFO | 否 | - |
| `camera_info` | 可選的攝影機資訊，用於覆蓋視埠狀態。 | LOAD3DCAMERA | 否 | - |
| `width` | 輸出預覽的寬度（像素，預設：1024）。 | INT | 是 | 1 至 4096 |
| `height` | 輸出預覽的高度（像素，預設：1024）。 | INT | 是 | 1 至 4096 |

## ## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `model_3d` | 從輸入傳遞而來的 3D 模型檔案。 | FILE3D |
| `model_3d_info` | 模型資訊，來自視埠狀態或可選輸入。 | LOAD3DMODELINFO |
| `camera_info` | 攝影機資訊，來自視埠狀態或可選輸入。 | LOAD3DCAMERA |
| `width` | 從輸入傳遞而來的寬度值。 | INT |
| `height` | 從輸入傳遞而來的高度值。 | INT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Save3DAdvanced/zh-TW.md)

---
**Source fingerprint (SHA-256):** `2c7d42b1875bb292e675526a2b38fcc8856c8ac45de25ac7b69d92323f0b7ae0`
