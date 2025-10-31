> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateVideo/zh-TW.md)

{heading_overview}

Create Video 節點可從一系列影像生成視訊檔案。您可以透過設定每秒幀數來指定播放速度，並可選擇性地為視訊添加音訊。此節點會將您的影像組合為可按照指定幀率播放的視訊格式。

{heading_inputs}

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `影像` | IMAGE | 是 | - | 用於建立視訊的影像序列。 |
| `每秒影格數` | FLOAT | 是 | 1.0 - 120.0 | 視訊播放的每秒幀數（預設值：30.0）。 |
| `音訊` | AUDIO | 否 | - | 要添加到視訊中的音訊。 |

{heading_outputs}

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `output` | VIDEO | 生成的視訊檔案，包含輸入影像和可選的音訊。 |