# SavePointCloud

儲存點雲節點會將 3D 點雲檔案儲存至輸出目錄，並可選擇性地為 3D 檢視器提供預覽資料。它負責處理檔案命名與儲存，同時傳遞相機與模型資訊以供顯示用途。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model_3d` | 點雲檔案 (.ply) | FILE3D_POINT_CLOUD_ANY 或 FILE3D_PLY | 是 | - |
| `filename_prefix` | 儲存檔案名稱的前綴（預設："3d/ComfyUI"） | STRING | 是 | - |
| `viewport_state` | 包含相機與模型資訊的當前視埠狀態 | LOAD3D | 是 | - |
| `model_3d_info` | 供 3D 檢視器使用的額外模型資訊 | LOAD3D_MODEL_INFO | 否 | - |
| `camera_info` | 供 3D 檢視器使用的相機資訊 | LOAD3D_CAMERA | 否 | - |
| `width` | 預覽顯示的寬度（像素，預設：1024） | INT | 是 | 1 至 4096 |
| `height` | 預覽顯示的高度（像素，預設：1024） | INT | 是 | 1 至 4096 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `model_3d` | 已儲存的點雲檔案 | FILE3D_POINT_CLOUD_ANY |
| `model_3d_info` | 供 3D 檢視器使用的模型資訊 | LOAD3D_MODEL_INFO |
| `camera_info` | 供 3D 檢視器使用的相機資訊 | LOAD3D_CAMERA |
| `width` | 預覽顯示的寬度 | INT |
| `height` | 預覽顯示的高度 | INT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SavePointCloud/zh-TW.md)

---
**Source fingerprint (SHA-256):** `ce8f005c431843a57d87a4aff2eed7a1604ebdf360f83b3aaaadc3ed364d218a`
