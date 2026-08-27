# RenderUVAtlas

將網格的 UV 佈局渲染為影像。每個連通的 UV 區域（chart）以不同顏色填滿，並在深灰色背景上以黑色勾勒出 chart 邊界。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `mesh` | 要渲染其 UV 佈局的 3D 網格。網格必須具有 UV 座標，否則會引發錯誤。 | MESH | 是 | - |
| `resolution` | 渲染影像的寬度和高度（以像素為單位，預設值：1024）。 | INT | 是 | 64 to 4096 (step 64) |

注意：如果網格沒有 UV 座標，節點會引發錯誤「mesh has no UVs to render. Run UnwrapMesh first.」。如果網格包含批次維度（3D UV 或面陣列），則只會渲染批次中的第一個項目。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `image` | 渲染後的 UV 圖集影像，每個 chart 以彩色呈現，且 chart 邊界邊緣以黑色勾勒。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RenderUVAtlas/zh-TW.md)

---
**Source fingerprint (SHA-256):** `b462101036418350390ffed621e583c6de14d5ea34d1e427342dc44ec3fd1922`
