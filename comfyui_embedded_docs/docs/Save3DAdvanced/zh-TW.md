# 儲存 3D（進階）

將 3D 模型儲存至 ComfyUI 輸出目錄中的檔案，並產生已儲存場景的預覽。此節點也會將 3D 模型、其在場景中的放置方式、相機資訊，以及視埠尺寸傳遞至下游節點。當模型放置或相機資訊未連接時，節點會使用儲存在視埠狀態中的值。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model_3d` | 來自上游 3D 節點的 3D 模型檔案。 | FILE3D | 是 | GLB<br>GLTF<br>FBX<br>OBJ<br>STL<br>USDZ<br>Any |
| `filename_prefix` | 用於儲存檔案名稱的前綴（預設值："3d/ComfyUI"）。 | STRING | 是 | Free text |
| `viewport_state` | 包含相機與模型放置資訊的視埠狀態，通常來自 Load 3D 節點。 | LOAD3D | 是 | - |
| `model_3d_info` | 場景中各模型的放置方式：位置、旋轉與縮放（Y 軸向上的世界空間）。連接時會覆寫儲存在 `viewport_state` 中的模型放置資訊。 | LOAD3DMODELINFO | 否 | - |
| `camera_info` | 視埠相機資訊：位置、注視目標、縮放與類型。連接時會覆寫儲存在 `viewport_state` 中的相機資訊。 | LOAD3DCAMERA | 否 | - |
| `width` | 視埠的渲染寬度，以像素為單位（預設值：1024）。 | INT | 是 | 1 至 4096 |
| `height` | 視埠的渲染高度，以像素為單位（預設值：1024）。 | INT | 是 | 1 至 4096 |

注意：`model_3d_info` 與 `camera_info` 為選填。當任一輸入未連接時，節點會改用儲存在 `viewport_state` 中的對應值。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `model_3d` | 從輸入傳遞過來的 3D 模型檔案。 | FILE3D |
| `model_3d_info` | 場景中各模型的放置方式：位置、旋轉與縮放（Y 軸向上的世界空間）。 | LOAD3DMODELINFO |
| `camera_info` | 視埠相機資訊：位置、注視目標、縮放與類型。 | LOAD3DCAMERA |
| `width` | 從輸入傳遞過來的渲染寬度值。 | INT |
| `height` | 從輸入傳遞過來的渲染高度值。 | INT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Save3DAdvanced/zh-TW.md)

---
**Source fingerprint (SHA-256):** `27cb15c5cf382e6e5b8164cfd456993404222c61d59edff2d51f9f1c8e47b25f`
