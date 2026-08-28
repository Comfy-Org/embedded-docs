# RenderUVAtlas

渲染 mesh 的 UV 佈局為一張影像。每個連通的 UV 區域（chart）會以不同顏色填滿，chart 邊界則在深灰色背景上以黑色描邊。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `mesh` | 要渲染其 UV 佈局的 3D 網格。網格必須具備 UV 座標，否則會拋出錯誤。 | MESH | 是 | - |
| `resolution` | 渲染影像的寬度和高度（以像素為單位，預設值：1024）。 | INT | 是 | 64 至 4096 (step 64) |

注意：如果網格沒有 UV 座標，節點會拋出錯誤："mesh has no UVs to render. Run UnwrapMesh first." 如果網格包含批次維度（3D UV 或面陣列），則只會渲染批次中的第一個項目。

## 輸出

| 輸出名 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `image` | 渲染後的 UV 圖集影像，每個 chart 已著色，且 chart 邊界邊緣以黑色描邊。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RenderUVAtlas/zh-TW.md)

---
**Source fingerprint (SHA-256):** `b462101036418350390ffed621e583c6de14d5ea34d1e427342dc44ec3fd1922`
