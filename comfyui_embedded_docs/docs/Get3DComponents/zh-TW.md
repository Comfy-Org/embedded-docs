# 取得 3D 元件

Get3DComponents 會解析 3D 模型檔案（GLB、GLTF、OBJ 或 STL），將其轉換為可供網格處理節點（例如 decimate、remesh、UV unwrap 與 bake）使用的可編輯網格。所有場景節點與圖元都會套用其變換並合併為單一網格；紋理與材質設定則取自第一個材質。此節點是 MeshToFile3D 節點的對應節點。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `3D 模型` | 來自 Load 3D 或其他 3D 節點的 3D 模型檔案。不支援 FBX/USDZ——請先轉換為 GLB。 | File3DGLB<br>File3DGLTF<br>File3DOBJ<br>File3DSTL<br>File3DAny | 是 | GLB<br>GLTF<br>OBJ<br>STL |

注意：不支援 FBX 與 USDZ 檔案，使用時會導致錯誤；請先將其轉換為 GLB 或 GLTF。若 3D 檔案包含多種材質，只會保留第一個材質的紋理與材質因子（並記錄警告）。所有場景圖元都會套用其變換並合併為單一網格。此節點屬於實驗性功能。

## 輸出

| 輸出名 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `網格` | 可編輯的網格，包含從模型檔案中提取的頂點、面、UV、頂點色、法線、切線，以及材質資訊（紋理、金屬粗糙度、法線貼圖、自發光、unlit 旗標）。 | MESH |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Get3DComponents/zh-TW.md)

---
**Source fingerprint (SHA-256):** `f2cdc9767a50503988484f09d2b3d110caf086b8cd84f65034a4a1e17a94405e`
