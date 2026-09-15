# 取得 3D 元件

Get3DComponents 會將 3D 模型檔案（GLB、GLTF、OBJ 或 STL）解析為可供網格處理節點（例如 decimate、remesh、UV unwrap 和 bake）使用的可編輯網格。所有場景節點與圖元都會套用其變換後合併成單一網格，而紋理與材質設定則取自第一個材質。它是 MeshToFile3D 節點的對應節點。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `3D 模型` | 來自 Load 3D 或其他 3D 節點的 3D 模型檔案。不支援 FBX/USDZ——請先轉換為 GLB。 | File3DGLB<br>File3DGLTF<br>File3DOBJ<br>File3DSTL<br>File3DAny | 是 | GLB<br>GLTF<br>OBJ<br>STL |

注意：不支援 FBX 與 USDZ 檔案，會導致錯誤；請先將它們轉換為 GLB 或 GLTF。若檔案格式無法辨識為 GLB、GLTF、OBJ 或 STL，節點會拋出錯誤並列出支援的格式。若 glTF 場景不含三角形幾何，或檔案包含指向頂點清單之外的面的索引（檔案損毀的徵兆），節點會拋出錯誤。若 3D 檔案包含多個材質，只會保留第一個材質的紋理與材質因子（並記錄一則警告）。所有場景圖元都會套用其變換後合併為單一網格。此節點為實驗性功能。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `mesh` | 可編輯網格，包含頂點、面、UV、頂點顏色、法線與切線，以及取自檔案的材質資訊（紋理、金屬度-粗糙度、法線貼圖、自發光顏色、unlit 旗標、occlusion-in-metallic-roughness 旗標與材質資料）。 | MESH |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Get3DComponents/zh-TW.md)

---
**Source fingerprint (SHA-256):** `f2cdc9767a50503988484f09d2b3d110caf086b8cd84f65034a4a1e17a94405e`
