> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveGLB/zh-TW.md)

SaveGLB 節點將 3D 網格資料或 3D 檔案儲存至輸出目錄。此節點可接受網格資料或各種 3D 檔案格式（GLB、GLTF、OBJ、FBX、STL、USDZ），並以指定的檔案名稱前綴進行匯出。在儲存網格資料時，可處理多個網格，並在啟用元資料時自動將工作流程元資料加入檔案中。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `mesh` | MESH 或 FILE3D | 是 | - | 要儲存的網格或 3D 檔案。接受網格資料或包含 GLB、GLTF、OBJ、FBX、STL 和 USDZ 在內的 3D 檔案格式 |
| `檔名前綴` | STRING | 否 | - | 輸出檔案名稱的前綴（預設值："3d/ComfyUI"） |

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `ui` | UI | 在使用者介面中顯示已儲存的 3D 檔案，包含檔案名稱、子資料夾和類型資訊 |

---
**Source fingerprint (SHA-256):** `bd36600185aeb793cd4e9f37f3b4464267cb36f451fdcf71aff83077bb8c3f53`
