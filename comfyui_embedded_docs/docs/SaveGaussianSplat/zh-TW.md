# SaveGaussianSplat

此節點將高斯潑濺 3D 檔案儲存至輸出目錄。它負責處理檔案儲存流程，並為 3D 視埠提供預覽資料。

## ## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model_3d` | 一個高斯潑濺 3D 檔案。 | FILE3D | 是 | SplatAny<br>PLY<br>SPLAT<br>SPZ<br>KSPLAT |
| `filename_prefix` | 儲存檔案名稱的前綴（預設值："3d/ComfyUI"）。 | STRING | 是 | 任何有效的檔案名稱前綴 |
| `viewport_state` | 包含相機與模型資訊的當前視埠狀態。 | LOAD3D | 是 | - |
| `model_3d_info` | 視埠的附加模型 3D 資訊。 | LOAD3DMODELINFO | 否 | - |
| `camera_info` | 視埠預覽的相機資訊。 | LOAD3DCAMERA | 否 | - |
| `width` | 預覽的寬度（預設值：1024）。 | INT | 是 | 1 至 4096 |
| `height` | 預覽的高度（預設值：1024）。 | INT | 是 | 1 至 4096 |

## ## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `model_3d` | 已儲存的高斯潑濺 3D 檔案。 | FILE3D |
| `model_3d_info` | 視埠的模型 3D 資訊。 | LOAD3DMODELINFO |
| `camera_info` | 視埠預覽的相機資訊。 | LOAD3DCAMERA |
| `width` | 預覽的寬度。 | INT |
| `height` | 預覽的高度。 | INT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveGaussianSplat/zh-TW.md)

---
**Source fingerprint (SHA-256):** `f2d6b98d2ce1fe11df8ba440b7f46a21e2308966c15daa5ca0bdca7dab1726cc`
