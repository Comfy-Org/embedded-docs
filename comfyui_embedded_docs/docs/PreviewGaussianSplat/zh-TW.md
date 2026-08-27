# 預覽 Splat

PreviewGaussianSplat 節點會在預覽視窗中顯示 3D gaussian splat 檔案，而不將其儲存到 ComfyUI 輸出目錄。它接受各種 gaussian splat 格式的 3D 模型檔案，儲存暫存副本以供預覽，並將模型資料傳遞給工作流程進行後續處理。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model_3d` | 一個 gaussian splat 3D 檔案。 | FILE3D | 是 | splat<br>ply<br>spz<br>ksplat |
| `model_3d_info` | 可選的 3D 模型元數據資訊。當未連接時，節點會使用 `viewport_state` 中的模型資訊。 | LOAD3DMODELINFO | 否 | - |
| `viewport_state` | 3D 視口的目前狀態，包括相機和模型資訊。 | LOAD3D | 是 | - |
| `camera_info` | 可選的預覽相機資訊。當未連接時，節點會使用 `viewport_state` 中的相機資訊。 | LOAD3DCAMERA | 否 | - |
| `width` | 預覽渲染的寬度（像素），預設值：1024。 | INT | 是 | 1 到 4096 |
| `height` | 預覽渲染的高度（像素），預設值：1024。 | INT | 是 | 1 到 4096 |

注意：當未提供 `camera_info` 或 `model_3d_info` 時，節點會回退使用儲存在 `viewport_state` 中的相機和模型資訊。

## 輸出

| 輸出名 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `model_3d` | 輸入的 3D gaussian splat 檔案，原樣傳遞。 | FILE3D |
| `model_3d_info` | 3D 模型的元數據資訊，來自輸入或從視口狀態推導。 | LOAD3DMODELINFO |
| `camera_info` | 預覽的相機資訊，來自輸入或從視口狀態推導。 | LOAD3DCAMERA |
| `width` | 預覽渲染的寬度。 | INT |
| `height` | 預覽渲染的高度。 | INT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewGaussianSplat/zh-TW.md)

---
**Source fingerprint (SHA-256):** `7157a0b34d7bda3e7ec86cb2ac09e0e10ff96ea7037bb6c9d6ad2c879fdedbb2`
