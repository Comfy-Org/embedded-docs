# 預覽點雲

預覽點雲節點讓您能夠在 ComfyUI 介面中檢視 3D 點雲檔案。它會將點雲儲存到暫存檔案，並在 3D 預覽視窗中顯示，同時傳遞模型資料和視窗設定以供後續處理。

## ## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model_3d` | 點雲檔案 (.ply) | FILE3D | 是 | - |
| `model_3d_info` | 3D 模型的相關資訊 | LOAD3DMODELINFO | 否 | - |
| `viewport_state` | 目前的視窗狀態 | LOAD3D | 是 | - |
| `camera_info` | 3D 視圖的相機資訊 | LOAD3DCAMERA | 否 | - |
| `width` | 預覽視窗的寬度（預設值：1024） | INT | 是 | 1 至 4096 |
| `height` | 預覽視窗的高度（預設值：1024） | INT | 是 | 1 至 4096 |

## ## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `model_3d` | 點雲模型資料 | FILE3D |
| `model_3d_info` | 3D 模型的相關資訊 | LOAD3DMODELINFO |
| `camera_info` | 3D 視圖的相機資訊 | LOAD3DCAMERA |
| `width` | 預覽視窗的寬度 | INT |
| `height` | 預覽視窗的高度 | INT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewPointCloud/zh-TW.md)

---
**Source fingerprint (SHA-256):** `f3121511841d1962aad881c0ac5b93f24842bf4810e84fe241330e9eab90334a`
