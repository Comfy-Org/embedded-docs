# 預覽點雲

此「預覽點雲」節點可讓您直接在 ComfyUI 介面中檢視 3D 點雲檔案，而無需將其儲存到 ComfyUI 輸出目錄。它會將點雲儲存到臨時位置，並在 3D 預覽視窗中顯示，同時也將模型資料、相機資訊和視口狀態傳遞以供進一步處理。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model_3d` | 點雲檔案 (.ply) | FILE3D | 是 | - |
| `model_3d_info` | 3D 模型的相關資訊 | LOAD3DMODELINFO | 否 | - |
| `viewport_state` | 目前的視口狀態 | LOAD3D | 是 | - |
| `camera_info` | 3D 視圖的相機資訊 | LOAD3DCAMERA | 否 | - |
| `width` | 預覽視窗的寬度（預設：1024） | INT | 是 | 1 至 4096 |
| `height` | 預覽視窗的高度（預設：1024） | INT | 是 | 1 至 4096 |

注意：當 `camera_info` 或 `model_3d_info` 未連接時，節點會回退使用 `viewport_state` 中所儲存的對應值。點雲檔案會儲存至 ComfyUI 的臨時目錄，不會寫入輸出目錄。這是一個輸出節點，因此主要用於在介面中顯示預覽結果。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `model_3d` | 點雲模型資料 | FILE3D |
| `model_3d_info` | 3D 模型的相關資訊 | LOAD3DMODELINFO |
| `camera_info` | 3D 視圖的相機資訊 | LOAD3DCAMERA |
| `width` | 預覽視窗的寬度 | INT |
| `height` | 預覽視窗的高度 | INT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewPointCloud/zh-TW.md)

---
**Source fingerprint (SHA-256):** `a192096df29c4d7029f6e7f4f32e0a2f48de5b3d0cd437bd5b03d79e15eb0987`
