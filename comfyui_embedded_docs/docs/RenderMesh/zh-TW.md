# RenderMesh

此節點透過光線投射單一視圖，將 3D 網格渲染為 2D 影像。它可以輸出帶紋理的網格、頂點顏色、實體著色表面、表面法線或深度。相機與可選的模型變換可來自 Load3D / Preview3D 檢視器；若未連接相機，則會自動取景預設的前視圖。

## 輸入

| 參數 | 說明 | 資料型別 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `mesh` | 要渲染的 3D 網格。 | MESH | 是 | — |
| `mode` | 要渲染的內容。auto：若存在紋理則使用紋理，否則使用頂點顏色，否則使用著色黏土。（預設值："auto"） | COMBO | 是 | `"auto"`<br>`"texture"`<br>`"vertex colors"`<br>`"solid"`<br>`"normal"`<br>`"depth"` |
| `width` | 渲染影像的寬度（像素）。（預設值：1024） | INT | 是 | 64 to 4096 (step 8) |
| `height` | 渲染影像的高度（像素）。（預設值：1024） | INT | 是 | 64 to 4096 (step 8) |
| `background` | 用於網格未覆蓋像素的背景顏色。（預設值："#000000"） | COLOR | 是 | — |
| `model_3d_info` | 來自同一個 Load3D / Preview3D 檢視器的模型變換。將其與 `camera_info` 連接，以符合檢視器的取景。 | LOAD3D_MODEL_INFO | 否 | — |
| `camera_info` | 來自 Load3D / Preview3D 檢視器或 Create Camera Info 節點的相機。若未連接任何相機，則會自動取景預設的前視圖。 | LOAD3D_CAMERA | 否 | — |

注意：批量網格僅會渲染第一個項目——若網格批次包含多個項目，節點會記錄警告並使用第一個項目。`texture` 模式要求網格同時具備紋理與 UV；`vertex colors` 模式則需要頂點顏色。若所選模式所需的資料不存在，節點會改以實體著色方式渲染。`model_3d_info` 與 `camera_info` 應同時連接自同一個 Load3D / Preview3D 檢視器，以使渲染結果符合檢視器的取景。

## 輸出

| 輸出名稱 | 說明 | 資料型別 |
|-------------|-------------|-----------|
| `image` | 網格渲染後的影像。 | IMAGE |
| `mask` | 一個遮罩，在網格被渲染處為 1.0，其餘位置為 0.0。 | MASK |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RenderMesh/zh-TW.md)

---
**Source fingerprint (SHA-256):** `d23e85a904520eb2dfed899eb3e6a9cf45c980df00c034503687ac4eccc66ac4`
