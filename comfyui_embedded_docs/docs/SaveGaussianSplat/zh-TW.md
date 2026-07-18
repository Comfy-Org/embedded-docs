# SaveGaussianSplat

此節點將高斯潑濺 3D 檔案儲存至 ComfyUI 輸出目錄，並為 3D 檢視器提供預覽資料。

## 輸入
| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model_3d` | 一個高斯潑濺 3D 檔案。 | FILE3D | 是 | - |
| `filename_prefix` | 儲存檔案名稱的前綴（預設："3d/ComfyUI"） | STRING | 是 | - |
| `viewport_state` | 來自 3D 載入器節點的當前視口狀態。 | LOAD3D | 是 | - |
| `model_3d_info` | 用於預覽的額外 3D 模型資訊。 | LOAD3DMODELINFO | 否 | - |
| `camera_info` | 用於預覽的相機資訊。 | LOAD3DCAMERA | 否 | - |
| `width` | 預覽的寬度（像素）（預設：1024） | INT | 是 | 最小值：1，最大值：4096，步長：1 |
| `height` | 預覽的高度（像素）（預設：1024） | INT | 是 | 最小值：1，最大值：4096，步長：1 |

## 輸出
| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `model_3d` | 已儲存的高斯潑濺 3D 檔案。 | FILE3D |
| `model_3d_info` | 用於預覽的 3D 模型資訊。 | LOAD3DMODELINFO |
| `camera_info` | 用於預覽的相機資訊。 | LOAD3DCAMERA |
| `width` | 預覽的寬度。 | INT |
| `height` | 預覽的高度。 | INT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveGaussianSplat/zh-TW.md)

---
**Source fingerprint (SHA-256):** `f2d6b98d2ce1fe11df8ba440b7f46a21e2308966c15daa5ca0bdca7dab1726cc`
