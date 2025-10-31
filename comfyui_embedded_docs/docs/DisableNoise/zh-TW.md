> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DisableNoise/zh-TW.md)

{heading_overview}

DisableNoise 節點提供了一個空的噪聲配置，可用於在採樣過程中停用噪聲生成。它返回一個不包含任何噪聲數據的特殊噪聲物件，當其他節點連接到此輸出時，可以跳過與噪聲相關的操作。

{heading_inputs}

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| *無輸入參數* | - | - | - | 此節點不需要任何輸入參數。 |

{heading_outputs}

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `NOISE` | NOISE | 返回一個空的噪聲配置，可用於在採樣過程中停用噪聲生成。 |