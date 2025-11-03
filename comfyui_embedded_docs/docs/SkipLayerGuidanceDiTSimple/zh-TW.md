> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SkipLayerGuidanceDiTSimple/zh-TW.md)

此節點是 SkipLayerGuidanceDiT 節點的簡化版本，僅在去噪過程中修改無條件傳遞。該節點透過根據指定的時機和層級參數，在無條件傳遞期間選擇性地跳過特定層級，將跳層引導應用於 DiT（擴散轉換器）模型中的特定轉換器層級。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | 是 | - | 要應用跳層引導的模型 |
| `double_layers` | STRING | 是 | - | 要跳過的雙區塊層級索引的逗號分隔列表（預設："7, 8, 9"） |
| `single_layers` | STRING | 是 | - | 要跳過的單區塊層級索引的逗號分隔列表（預設："7, 8, 9"） |
| `start_percent` | FLOAT | 是 | 0.0 - 1.0 | 跳層引導開始的去噪過程起始百分比（預設：0.0） |
| `end_percent` | FLOAT | 是 | 0.0 - 1.0 | 跳層引導停止的去噪過程結束百分比（預設：1.0） |

**注意：** 僅當 `double_layers` 和 `single_layers` 都包含有效的層級索引時，才會應用跳層引導。如果兩者皆為空，節點將返回未修改的原始模型。

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `model` | MODEL | 已對指定層級應用跳層引導的修改後模型 |