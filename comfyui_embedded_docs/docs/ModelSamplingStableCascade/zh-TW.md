> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingStableCascade/zh-TW.md)

{heading_overview}

ModelSamplingStableCascade 節點透過使用偏移值調整採樣參數，對模型應用穩定級聯採樣。它會建立輸入模型的修改版本，具有用於穩定級聯生成的自定義採樣配置。

{heading_inputs}

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | 是 | - | 要應用穩定級聯採樣的輸入模型 |
| `shift` | FLOAT | 是 | 0.0 - 100.0 | 應用於採樣參數的偏移值（預設值：2.0） |

{heading_outputs}

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `model` | MODEL | 已應用穩定級聯採樣的修改後模型 |