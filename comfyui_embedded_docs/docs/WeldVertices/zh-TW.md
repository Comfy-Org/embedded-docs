# 焊接頂點

Weld Vertices 會合併 3D 網格中位置重合的頂點，使得原本各自擁有獨立角點的面最終會共用相同的頂點。它會使用以網格邊界框為基礎的容差，透過網格量化將鄰近頂點分組，並對每個合併後的群組平均頂點顏色。當網格匯入時尚未焊接，也就是每個面都有自己的頂點且沒有共用邊時，這個節點很有用，也可作為 FillHoles 或 DecimateMesh 等拓撲感知操作之前的前置處理。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `mesh` | 要合併位置重合頂點的輸入 3D 網格。 | MESH | 是 | - |
| `epsilon_rel` | 焊接容差（bbox 對角線的比例）。1e-5 用於浮點去重；1e-3 用於視覺上接近但實際不同的頂點。預設：1e-5。 | FLOAT | 是 | 0.0 to unlimited (step 1e-6) |
| `epsilon_abs` | 絕對焊接容差（當大於 0 時會覆寫 `epsilon_rel`）。預設：0.0。 | FLOAT | 是 | 0.0 to unlimited (step 1e-6) |

注意：當 `epsilon_abs` 大於 0 時，它的優先順序高於 `epsilon_rel`，且會忽略相對容差。當 `epsilon_abs` 為 0 時，會使用相對容差 `epsilon_rel`，並將其乘以網格邊界框對角線，轉換為絕對距離。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `mesh` | 焊接後的網格，具有合併後的頂點、更新後的面索引，以及平均後的頂點顏色（如果輸入網格有顏色）。 | MESH |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WeldVertices/zh-TW.md)

---
**Source fingerprint (SHA-256):** `f8779e764b344de651b8459f6e4c28773509d9596a98fd164dc7044278856435`
