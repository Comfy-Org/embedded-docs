# 預覽 Splat

PreviewGaussianSplat 節點可讓您直接在 ComfyUI 介面中預覽 3D 高斯潑濺（Gaussian Splat）檔案，而無需將其儲存到輸出目錄。它會將檔案暫時儲存在暫存資料夾中，在 3D 預覽視窗中顯示，並將模型資料、攝影機資訊和預覽尺寸傳遞給其他節點。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model_3d` | 一個高斯潑濺 3D 檔案。 | FILE3D | 是 | splat, ply, spz, ksplat |
| `model_3d_info` | 關於 3D 模型的可選中繼資料資訊。 | LOAD3DMODELINFO | 否 | - |
| `viewport_state` | 3D 視埠的目前狀態，包括攝影機和模型資訊。 | LOAD3D | 是 | - |
| `camera_info` | 預覽用的可選攝影機資訊。 | LOAD3DCAMERA | 否 | - |
| `width` | 預覽渲染的寬度（像素），預設值：1024。 | INT | 是 | 1 to 4096 |
| `height` | 預覽渲染的高度（像素），預設值：1024。 | INT | 是 | 1 to 4096 |

注意：當未提供 `camera_info` 或 `model_3d_info` 時，節點會改為使用 `viewport_state` 中的對應值。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `model_3d` | 輸入的 3D 高斯潑濺檔案，未經修改地傳遞。 | FILE3D |
| `model_3d_info` | 關於 3D 模型的中繼資料資訊，來自輸入或視埠狀態。 | LOAD3DMODELINFO |
| `camera_info` | 預覽用的攝影機資訊，來自輸入或視埠狀態。 | LOAD3DCAMERA |
| `width` | 預覽渲染的寬度。 | INT |
| `height` | 預覽渲染的高度。 | INT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewGaussianSplat/zh-TW.md)

---
**Source fingerprint (SHA-256):** `7157a0b34d7bda3e7ec86cb2ac09e0e10ff96ea7037bb6c9d6ad2c879fdedbb2`
