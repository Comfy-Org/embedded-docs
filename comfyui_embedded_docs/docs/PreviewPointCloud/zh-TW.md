# 預覽點雲

## 輸入
| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|------|------|---------|------|------|
| `model_3d` | 點雲檔案 (.ply) | FILE3D | 是 | - |
| `model_3d_info` | 3D 模型的資訊。進階輸入。未連接時，會使用 `viewport_state` 中儲存的值。 | LOAD3DMODELINFO | 否 | - |
| `viewport_state` | 目前的視埠狀態，其中可包含用於預覽的攝影機資訊與模型資訊。 | LOAD3D | 是 | - |
| `camera_info` | 3D 檢視的攝影機資訊。進階輸入。未連接時，會使用 `viewport_state` 中儲存的值。 | LOAD3DCAMERA | 否 | - |
| `width` | 預覽視窗的寬度（像素）（預設值：1024）。 | INT | 是 | 1 to 4096 |
| `height` | 預覽視窗的高度（像素）（預設值：1024）。 | INT | 是 | 1 to 4096 |

注意：當 `camera_info` 或 `model_3d_info` 未連接時，節點會使用儲存在 `viewport_state` 中的值。

## 輸出
| 輸出名稱 | 說明 | 資料類型 |
|---------|------|---------|
| `model_3d` | 點雲模型資料，原封不動地傳遞。 | FILE3D |
| `model_3d_info` | 用於預覽的 3D 模型資訊。 | LOAD3DMODELINFO |
| `camera_info` | 用於 3D 檢視的攝影機資訊。 | LOAD3DCAMERA |
| `width` | 預覽視窗的寬度。 | INT |
| `height` | 預覽視窗的高度。 | INT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewPointCloud/zh-TW.md)

---
**Source fingerprint (SHA-256):** `a192096df29c4d7029f6e7f4f32e0a2f48de5b3d0cd437bd5b03d79e15eb0987`
