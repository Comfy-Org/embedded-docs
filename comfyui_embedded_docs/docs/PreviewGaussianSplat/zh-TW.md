# 預覽 Splat

PreviewGaussianSplat 節點允許您在 ComfyUI 介面中預覽 3D 高斯潑濺檔案。它接受多種高斯潑濺格式的 3D 模型檔案，並在 3D 預覽視窗中渲染，同時將模型資料傳遞以供後續處理。

## ## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model_3d` | 高斯潑濺 3D 檔案。 | FILE3D | 是 | 支援格式：splat、ply、spz、ksplat |
| `model_3d_info` | 關於 3D 模型的選用中繼資料資訊。 | LOAD3DMODELINFO | 否 | - |
| `viewport_state` | 3D 視埠的當前狀態，包含相機和模型資訊。 | LOAD3D | 是 | - |
| `camera_info` | 預覽的選用相機資訊。 | LOAD3DCAMERA | 否 | - |
| `width` | 預覽渲染的寬度（像素），預設值：1024。 | INT | 是 | 1 至 4096 |
| `height` | 預覽渲染的高度（像素），預設值：1024。 | INT | 是 | 1 至 4096 |

## ## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `model_3d` | 輸入的 3D 高斯潑濺檔案，未經修改直接傳遞。 | FILE3D |
| `model_3d_info` | 3D 模型的中繼資料資訊，來自輸入或從視埠狀態推導得出。 | LOAD3DMODELINFO |
| `camera_info` | 預覽的相機資訊，來自輸入或從視埠狀態推導得出。 | LOAD3DCAMERA |
| `width` | 預覽渲染的寬度。 | INT |
| `height` | 預覽渲染的高度。 | INT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewGaussianSplat/zh-TW.md)

---
**Source fingerprint (SHA-256):** `7b79e9ab25858e7db6e999313cc11226895aeb4d7fee414f56f0d5fd2363b485`
