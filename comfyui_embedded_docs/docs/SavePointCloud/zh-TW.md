# SavePointCloud

儲存點雲節點會將 3D 點雲檔案儲存到您的 ComfyUI 輸出目錄中。它同時會傳遞點雲資料以及可選的相機和模型資訊，供工作流程中的其他節點使用。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model_3d` | 點雲檔案 (.ply) | FILE3D | 是 | - |
| `filename_prefix` | 儲存檔案名稱的前綴（預設："3d/ComfyUI"） | STRING | 是 | - |
| `viewport_state` | 來自 3D 視埠節點的狀態 | LOAD3D | 是 | - |
| `model_3d_info` | 進階用途的可選 3D 模型資訊 | LOAD3DMODELINFO | 否 | - |
| `camera_info` | 進階用途的可選相機資訊 | LOAD3DCAMERA | 否 | - |
| `width` | 預覽影像的寬度（像素）（預設：1024） | INT | 是 | 最小值：1，最大值：4096，步進：1 |
| `height` | 預覽影像的高度（像素）（預設：1024） | INT | 是 | 最小值：1，最大值：4096，步進：1 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `model_3d` | 已儲存的點雲檔案 | FILE3D |
| `model_3d_info` | 3D 模型的相關資訊 | LOAD3DMODELINFO |
| `camera_info` | 視埠的相機資訊 | LOAD3DCAMERA |
| `width` | 預覽影像的寬度 | INT |
| `height` | 預覽影像的高度 | INT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SavePointCloud/zh-TW.md)

---
**Source fingerprint (SHA-256):** `ce8f005c431843a57d87a4aff2eed7a1604ebdf360f83b3aaaadc3ed364d218a`
