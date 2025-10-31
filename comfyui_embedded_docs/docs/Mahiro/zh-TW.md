> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Mahiro/zh-TW.md)

{heading_overview}

Mahiro 節點修改了引導函數，使其更專注於正向提示詞的方向，而非正向與負向提示詞之間的差異。它建立了一個修補後的模型，該模型使用標準化條件與非條件去噪輸出之間的餘弦相似度來應用自定義引導縮放方法。這個實驗性節點有助於更強烈地將生成結果導向正向提示詞的預期方向。

{heading_inputs}

| 參數 | 資料類型 | 必填 | 範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | 是 | | 要使用修改後引導函數進行修補的模型 |

{heading_outputs}

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `patched_model` | MODEL | 應用了 Mahiro 引導函數的修改後模型 |