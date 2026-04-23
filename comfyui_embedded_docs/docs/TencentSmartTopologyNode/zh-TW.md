> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TencentSmartTopologyNode/zh-TW.md)

此節點對 3D 模型執行智慧拓撲重構，這是一個自動創建具有更低多邊形數量的全新、更乾淨網格的過程。它連接至騰訊混元 3D API 來處理模型，支援 GLB 和 OBJ 檔案格式。節點會將處理後的模型以 OBJ 檔案格式返回。

## 輸入參數

| 參數 | 資料類型 | 必填 | 範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `model_3d` | FILE3D | 是 | - | 輸入的 3D 模型 (GLB 或 OBJ)。檔案必須為 GLB 或 OBJ 格式，且大小不能超過 200MB。 |
| `polygon_type` | STRING | 是 | `"triangle"`<br>`"quadrilateral"` | 表面組成類型。 |
| `face_level` | STRING | 是 | `"medium"`<br>`"high"`<br>`"low"` | 多邊形減面等級。 |
| `seed` | INT | 否 | 0 到 2147483647 | 種子值控制節點是否應重新執行；無論種子值為何，結果都是非確定性的。(預設值: 0) |

**注意：** `seed` 參數用於觸發節點重新執行，但無法保證相同種子值會產生完全相同的輸出結果。

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `OBJ` | FILE3D | 經過拓撲優化處理的 3D 模型，以 OBJ 格式返回。 |