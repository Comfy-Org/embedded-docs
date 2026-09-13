# 渲染網格

此節點透過對單一視圖進行光線投射，將 3D 網格渲染成 2D 影像。它可以輸出帶紋理的網格、頂點顏色、實心著色表面、表面法線或深度。相機與選用的模型變換可以來自 Load3D / Preview3D 檢視器；若未連接相機，會自動取景為預設正視圖。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `mesh` | 要渲染的 3D 網格。 | MESH | 是 | — |
| `mode` | 要渲染的內容。auto：若有紋理則使用紋理，否則使用頂點顏色，否則使用黏土著色。（預設："auto"） | COMBO | 是 | `"auto"`<br>`"texture"`<br>`"vertex colors"`<br>`"solid"`<br>`"normal"`<br>`"depth"` |
| `width` | 渲染影像的寬度，單位為像素。（預設：1024） | INT | 是 | 64 至 4096 （步進值：8） |
| `height` | 渲染影像的高度，單位為像素。（預設：1024） | INT | 是 | 64 至 4096 （步進值：8） |
| `background` | 用於網格未覆蓋像素的背景顏色。（預設："#000000"） | COLOR | 是 | — |
| `model_3d_info` | 來自同一個 Load3D / Preview3D 檢視器的模型變換。將其與 `camera_info` 連接，以符合檢視器的取景。 | LOAD3D_MODEL_INFO | 否 | — |
| `camera_info` | 來自 Load3D / Preview3D 檢視器或 Create Camera Info 節點的相機。若未連接任何相機，會自動取景為預設正視圖。 | LOAD3D_CAMERA | 否 | — |

注意：批次網格中僅會渲染第一個項目——若網格批次包含多個項目，節點會記錄警告並使用第一個。`texture` 模式要求網格同時具有紋理與 UV；`vertex colors` 模式要求頂點顏色；若所選模式的資料無法取得，節點會退回實心著色渲染。`normal` 模式在存在平滑頂點法線時使用它們，否則使用逐面法線。在 `depth` 模式中，較近的表面看起來較亮（近 = 白色），而未被網格覆蓋的像素保持黑色。`model_3d_info` 與 `camera_info` 應從同一個 Load3D / Preview3D 檢視器一起連接，使渲染結果符合檢視器的取景。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `image` | 網格渲染後的影像。 | IMAGE |
| `mask` | 遮罩，在網格渲染處為 1.0，其他位置為 0.0。 | MASK |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RenderMesh/zh-TW.md)

---
**Source fingerprint (SHA-256):** `d23e85a904520eb2dfed899eb3e6a9cf45c980df00c034503687ac4eccc66ac4`
