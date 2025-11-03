> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VoxelToMesh/zh-TW.md)

VoxelToMesh 節點使用不同的演算法將 3D 體素資料轉換為網格幾何體。它處理體素網格並生成構成 3D 網格表示的頂點和面。該節點支援多種轉換演算法，並允許調整閾值以控制表面提取。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 參數說明 |
|-----------|-----------|----------|-------|-------------|
| `voxel` | VOXEL | 是 | - | 要轉換為網格幾何體的輸入體素資料 |
| `algorithm` | COMBO | 是 | "surface net"<br>"basic" | 用於從體素資料進行網格轉換的演算法 |
| `threshold` | FLOAT | 是 | -1.0 至 1.0 | 用於表面提取的閾值（預設值：0.6） |

## 輸出結果

| 輸出名稱 | 資料類型 | 輸出說明 |
|-------------|-----------|-------------|
| `MESH` | MESH | 生成的包含頂點和面的 3D 網格 |