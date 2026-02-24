> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TencentModelTo3DUVNode/zh-TW.md)

此節點使用騰訊混元3D API 對 3D 模型進行 UV 展開。它接收一個 3D 模型檔案作為輸入，將其發送至 API 進行處理，並以 OBJ 和 FBX 格式返回處理後的模型以及生成的 UV 紋理圖像。

## 輸入參數

| 參數 | 資料類型 | 必填 | 範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `model_3d` | FILE3D | 是 | GLB<br>OBJ<br>FBX | 輸入的 3D 模型 (GLB、OBJ 或 FBX)。模型的面數必須少於 30000。 |
| `seed` | INT | 否 | 0 至 2147483647 | 種子值 (預設值：1)。此值控制節點是否應重新執行，但無論種子值為何，結果都是非確定性的。 |

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `OBJ` | FILE3D | 處理後的 3D 模型檔案，格式為 OBJ。 |
| `FBX` | FILE3D | 處理後的 3D 模型檔案，格式為 FBX。 |
| `Image` | IMAGE | 生成的 UV 紋理圖像。 |