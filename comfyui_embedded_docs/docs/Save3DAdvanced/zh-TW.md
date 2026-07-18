# Save3DAdvanced

此節點將 3D 模型儲存到您的 ComfyUI 輸出目錄，並提供進階預覽功能。它允許您指定輸出檔案名稱、預覽尺寸，並可選擇性地傳遞相機和模型資訊，以獲得增強的 3D 檢視器體驗。

## 輸入
| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model_3d` | 來自上游 3D 節點的 3D 模型檔案。 | FILE3D | 是 | GLB、GLTF、FBX、OBJ、STL、USDZ 或任何 3D 格式 |
| `filename_prefix` | 儲存檔案名稱的前綴。系統會自動附加計數器和副檔名。（預設值："3d/ComfyUI"） | STRING | 是 | 任何有效的檔案名稱字串 |
| `viewport_state` | 目前的視口狀態，通常來自 3D 檢視器節點。 | LOAD3D | 是 | - |
| `model_3d_info` | 用於預覽的選擇性 3D 模型資訊。 | LOAD3DMODELINFO | 否 | - |
| `camera_info` | 用於預覽的選擇性相機資訊。 | LOAD3DCAMERA | 否 | - |
| `width` | 預覽的寬度（像素）。（預設值：1024） | INT | 是 | 1 到 4096 |
| `height` | 預覽的高度（像素）。（預設值：1024） | INT | 是 | 1 到 4096 |

## 輸出
| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `model_3d` | 已儲存的 3D 模型檔案。 | FILE3D |
| `model_3d_info` | 傳遞給下游節點的 3D 模型資訊。 | LOAD3DMODELINFO |
| `camera_info` | 傳遞給下游節點的相機資訊。 | LOAD3DCAMERA |
| `width` | 傳遞給下游節點的寬度值。 | INT |
| `height` | 傳遞給下游節點的高度值。 | INT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Save3DAdvanced/zh-TW.md)

---
**Source fingerprint (SHA-256):** `2c7d42b1875bb292e675526a2b38fcc8856c8ac45de25ac7b69d92323f0b7ae0`
