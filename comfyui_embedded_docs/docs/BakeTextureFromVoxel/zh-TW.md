# 從體素烘焙紋理

此節點會使用網格既有的 UV 佈局，將 PBR 貼圖烘焙到 3D 網格上。它會在 UV 空間中將網格光柵化，並在每個 texel 上從稀疏體素體積取樣顏色與材質屬性，輸出基礎顏色影像以及 metallic 與 roughness 貼圖。它不會展開網格，因此必須在上游連接 UV 展開節點；產生的影像應搭配同一個網格在 ApplyTextureToMesh 中使用，以儲存為 GLB。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `mesh` | 要將貼圖烘焙到的 3D 網格。必須已經有 UV 佈局；必須在上游連接 UV 展開節點。 | MESH | 是 | |
| `voxel_colors` | 包含每個體素顏色與可選 PBR 屬性（metallic 與 roughness 通道）的稀疏體素體積。 | VOXEL | 是 | |
| `texture_size` | 正方形 UV 圖集解析度（顯示名稱："resolution"，預設：2048）。 | INT | 是 | 64 至 8192 |
| `參考網格` | 可選的稠密簡化前網格；在取樣前將每個 texel 反向投影到其真實表面，避免在低面數網格上產生面片化烘焙。 | MESH | 否 | |

注意事項：

- 輸入網格必須有 UV。若不存在 UV，節點會引發錯誤。UV 必須與頂點一一對應（每個頂點一個 UV）。
- 當網格與體素座標包含批次維度時，每個批次項目會分別烘焙。若某個批次項目沒有體素或沒有面，則會略過該項目，並為其輸出黑色貼圖。
- 當為某個批次提供 `reference_mesh` 時，它會依批次索引配對；除非它只包含單一網格，此時該網格會用於所有項目。
- 未被任何 UV 三角形覆蓋的 texel 會由最近的已覆蓋 texel 填補，以避免貼圖接縫吸入黑色。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `base_color` | RGB 基礎顏色貼圖。數值為 0–1 範圍的 FLOAT 值。 | IMAGE |
| `metallic` | 灰階金屬度貼圖（FLOAT，0–1）。當體素顏色不包含 metallic 通道時為黑色。 | IMAGE |
| `roughness` | 灰階粗糙度貼圖（FLOAT，0–1）。當體素顏色不包含 roughness 通道時為黑色。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BakeTextureFromVoxel/zh-TW.md)

---
**Source fingerprint (SHA-256):** `080dcb670620f1cb97523d04fc45293e03d139e513845d0fa7b1c4d2f8bdf32d`
