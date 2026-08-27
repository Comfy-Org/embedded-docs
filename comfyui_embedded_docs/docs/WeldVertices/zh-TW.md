# WeldVertices

Weld Vertices 會合併 3D 網格中重合的頂點，使原本具有分開角點的面最終共享相同的頂點。它使用基於網格邊界盒容差的網格量化來對附近的頂點進行分組，並對每個合併的組平均頂點顏色。當網格以未焊接狀態到達時（即每個面都有自己的頂點且沒有共享邊緣），此功能非常有用。

## 輸入
| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `mesh` | 輸入的 3D 網格，其重合的頂點將被合併。 | MESH | 是 | - |
| `epsilon_rel` | 焊接容差（邊界盒對角線的分數）。1e-5 用於浮點數去重；1e-3 用於明顯接近但不同的頂點。預設值：1e-5。 | FLOAT | 是 | 0.0 to unlimited |
| `epsilon_abs` | 絕對焊接容差（當大於 0 時覆寫 `epsilon_rel`）。預設值：0.0。 | FLOAT | 是 | 0.0 to unlimited |

注意：當 `epsilon_abs` 大於 0 時，它優先於 `epsilon_rel`，且相對容差會被忽略。當 `epsilon_abs` 為 0 時，使用相對容差 `epsilon_rel`。

## 輸出
| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `mesh` | 已焊接的網格，包含合併後的頂點、更新的面索引，以及平均後的頂點顏色（如果輸入網格具有顏色的話）。 | MESH |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WeldVertices/zh-TW.md)

---
**Source fingerprint (SHA-256):** `f8779e764b344de651b8459f6e4c28773509d9596a98fd164dc7044278856435`
