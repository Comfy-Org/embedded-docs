# 預覽 Splat

PreviewGaussianSplat 節點會在預覽視窗中顯示 3D Gaussian splat 檔案，而不會將其儲存到 ComfyUI 輸出目錄。它接受各種 Gaussian splat 格式的 3D 模型檔案，會儲存一份臨時副本以供預覽，並將模型資料傳遞出去，以便在工作流程中進一步處理。此節點標記為實驗性，並作為輸出節點運作。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model_3d` | 一個 Gaussian splat 3D 檔案。 | FILE3D | 是 | splat<br>ply<br>spz<br>ksplat |
| `model_3d_info` | 關於 3D 模型的選用中繼資料資訊。未連接時，節點會使用來自 `viewport_state` 的模型資訊。 | LOAD3DMODELINFO | 否 | - |
| `viewport_state` | 3D 檢視區的目前狀態，包括相機與模型資訊。 | LOAD3D | 是 | - |
| `camera_info` | 用於預覽的選用相機資訊。未連接時，節點會使用來自 `viewport_state` 的相機資訊。 | LOAD3DCAMERA | 否 | - |
| `width` | 預覽渲染的寬度，單位為像素（預設值：1024）。 | INT | 是 | 1 至 4096 |
| `height` | 預覽渲染的高度，單位為像素（預設值：1024）。 | INT | 是 | 1 至 4096 |

注意：當未提供 `camera_info` 或 `model_3d_info` 時，節點會改用儲存在 `viewport_state` 中的相機與模型資訊。若 `viewport_state` 不是有效的檢視區狀態物件，則會將其視為空。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `model_3d` | 輸入的 3D Gaussian splat 檔案，會原樣傳遞出去。 | FILE3D |
| `model_3d_info` | 關於 3D 模型的中繼資料資訊，來自輸入或衍生自檢視區狀態。 | LOAD3DMODELINFO |
| `camera_info` | 用於預覽的相機資訊，來自輸入或衍生自檢視區狀態。 | LOAD3DCAMERA |
| `width` | 預覽渲染的寬度。 | INT |
| `height` | 預覽渲染的高度。 | INT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewGaussianSplat/zh-TW.md)

---
**Source fingerprint (SHA-256):** `4fc86c692724ce406f9bba9aa9ebe22a92e72a25d11abf8f55d1b99044bb1acd`
