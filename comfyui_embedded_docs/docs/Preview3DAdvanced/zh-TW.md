# 3D 預覽（進階）

此節點會在不將檔案儲存至 ComfyUI 輸出目錄的情況下，於 UI 中顯示 3D 模型預覽。它會將模型儲存至暫存檔案，並將模型資料、模型資訊、相機資訊與預覽尺寸傳遞給下游進一步處理。

## 輸入
| 參數 | 描述 | 資料型別 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model_3d` | 來自上游 3D 節點的 3D 模型檔案。 | FILE3D | 是 | GLB, GLTF, FBX, OBJ, STL, USDZ, or any supported 3D format |
| `model_3d_info` | 選用的模型資訊中繼資料。進階選項。 | LOAD3DMODELINFO | 否 | - |
| `viewport_state` | 包含相機與模型資訊的目前視埠狀態。 | LOAD3D | 是 | - |
| `camera_info` | 3D 檢視的選用相機設定。進階選項。 | LOAD3DCAMERA | 否 | - |
| `寬度` | 預覽寬度（像素）。預設值：1024。 | INT | 是 | 1 至 4096 |
| `高度` | 預覽高度（像素）。預設值：1024。 | INT | 是 | 1 至 4096 |

注意：當 `camera_info` 或 `model_3d_info` 未連接時，若有可用的 `viewport_state`，其值會取自 `viewport_state`。若 `viewport_state` 沒有模型資訊，`model_3d_info` 會預設為空清單。若 `viewport_state` 不是字典，則將其視為空值。

## 輸出
| 輸出名稱 | 描述 | 資料型別 |
|-------------|-------------|-----------|
| `model_file` | 從輸入傳遞而來的 3D 模型檔案。 | FILE3D |
| `camera_info` | 來自輸入或視埠狀態的模型資訊中繼資料。 | LOAD3DMODELINFO |
| `model_3d_info` | 來自輸入或視埠狀態的相機設定。 | LOAD3DCAMERA |
| `寬度` | 預覽寬度（像素）。 | INT |
| `高度` | 預覽高度（像素）。 | INT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Preview3DAdvanced/zh-TW.md)

---
**Source fingerprint (SHA-256):** `eda8c8fdd6ce7c39caf00c3054fc58e6dcab124fc3774d17af2deae651fbbf2e`
