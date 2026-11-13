# Bake Texture From Views

將渲染後的影像投影回網格的 UV 佈局。使用 Render Mesh 渲染網格，編輯或重新生成影像，然後使用相同的網格和相機將其烘焙。沒有任何視圖覆蓋的紋素會保留網格自身的紋理或頂點顏色。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `mesh` | 已渲染的 UV 展開網格。 | MESH | 是 | - |
| `images` | 每台相機一張影像，依相機順序（Batch Images）。任何符合渲染長寬比的解析度；較高解析度會產生更銳利的烘焙結果。 | IMAGE | 是 | - |
| `camera_info` | 用於渲染這些影像的相機，需與連接至 Render Mesh 的相機相同。使用 Batch Cameras 合併多個相機組。無：Render Mesh 自動取景的前視圖。 | LOAD3D_CAMERA | 否 | - |
| `resolution` | 方形紋理解析度。0 會保留網格目前的紋理尺寸；若網格沒有紋理則為 2048；否則會將目前的紋理重新取樣至此解析度。預設：0。 | INT | 否 | 0 至 8192（步進值：64） |
| `blend_exponent` | 視圖會以 cos(視角)^指數 加權。較高值偏好最正對的視圖（更銳利、接縫更明顯）；較低值會平均更多視圖（更柔和）。預設：4.0。 | FLOAT | 否 | 0.0 至 32.0（步進值：0.5） |
| `fill_unseen` | 沒有任何視圖看到的紋素會採用從可見表面延伸生成的顏色，而不是網格自身的紋理或頂點顏色。當視圖要取代整張紋理時使用。預設：false。 | BOOLEAN | 否 | true<br>false |
| `mask` | 每個視圖中已編輯的區域；僅投影被遮罩的像素。單一遮罩會套用到每個視圖。 | MASK | 否 | - |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `base_color` | 烘焙後的紋理，用於 Apply Texture to Mesh。 | IMAGE |
| `confidence` | 對每個紋素而言，最佳視圖正對看到它的程度；0 表示未被看到。 | MASK |

注意：使用檢視器模型變換進行的渲染不會與烘焙結果對齊，且僅使用批次中的第一個網格。

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BakeTextureFromViews/zh-TW.md)

---
**Source fingerprint (SHA-256):** `e5f2456977693dc09e69ce4d846f2ab775f2520115623d9f63a76807d6c9f797`
