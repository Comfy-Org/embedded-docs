# 渲染 UV 圖集

將網格的 UV 佈局渲染為影像。每個相連的 UV 區域（chart）會填上不同顏色，且 chart 邊界邊緣會以黑色描邊，背景為深灰色。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `mesh` | 要渲染其 UV 佈局的 3D 網格。此網格必須具有 UV 座標；否則節點會引發錯誤 "mesh has no UVs to render. Run UnwrapMesh first." | MESH | 是 | - |
| `resolution` | 渲染後正方形影像的寬度與高度（像素）（預設：1024）。 | INT | 是 | 64 至 4096 （步進值：64） |

注意：若網格包含批次維度（3D UV 或面陣列），僅會渲染批次中的第一個項目。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `image` | 渲染後的 UV 圖集影像，以單一影像批次回傳。每個 UV 區塊會上色，且區塊邊界邊緣會以黑色描邊。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RenderUVAtlas/zh-TW.md)

---
**Source fingerprint (SHA-256):** `b462101036418350390ffed621e583c6de14d5ea34d1e427342dc44ec3fd1922`
