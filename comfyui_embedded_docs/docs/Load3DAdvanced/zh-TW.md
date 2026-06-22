# Load3DAdvanced

此節點從您的 ComfyUI 輸入目錄載入 3D 模型檔案，並提供模型資料以及相機和視口資訊。它支援常見的 3D 檔案格式，並允許您指定用於渲染的輸出影像尺寸。

## ## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model_file` | 要載入的 3D 模型檔案。選擇 "none" 可跳過載入模型。 | STRING | 是 | `"none"`<br>input/3d 目錄中可用的 3D 檔案列表 |
| `viewport_state` | 來自 3D 檢視器的當前視口狀態，包含相機和模型資訊。 | LOAD3D | 是 | - |
| `width` | 輸出影像的寬度（像素），預設值：1024 | INT | 是 | 最小值：1<br>最大值：4096<br>步進值：1 |
| `height` | 輸出影像的高度（像素），預設值：1024 | INT | 是 | 最小值：1<br>最大值：4096<br>步進值：1 |

**參數說明：**
- `model_file` 參數僅顯示具有以下副檔名的檔案：.gltf、.glb、.obj、.fbx、.stl
- 檔案必須放置在您 ComfyUI 安裝目錄的 `input/3d` 資料夾中
- 如果 `model_file` 設定為 "none"，則不會載入任何 3D 模型資料（輸出 `model_3d` 將為空）

## ## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `model_3d` | 已載入的 3D 模型資料，若未選擇模型檔案則為空 | FILE3DANY |
| `model_3d_info` | 來自視口狀態的已載入 3D 模型資訊 | LOAD3DMODELINFO |
| `camera_info` | 來自視口狀態的相機資訊 | LOAD3DCAMERA |
| `width` | 指定的輸出影像寬度 | INT |
| `height` | 指定的輸出影像高度 | INT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Load3DAdvanced/zh-TW.md)

---
**Source fingerprint (SHA-256):** `fdacea8abf627621150e1196743e36f61534333837c33cc9a7416a6d11700c4d`
