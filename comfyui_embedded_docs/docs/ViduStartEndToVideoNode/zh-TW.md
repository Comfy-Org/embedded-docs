> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ViduStartEndToVideoNode/zh-TW.md)

Vidu Start End To Video Generation 節點透過在起始影格和結束影格之間生成影格來建立影片。它使用文字提示來引導影片生成過程，並支援具有不同解析度和運動設定的各種影片模型。該節點在處理前會驗證起始和結束影格是否具有相容的長寬比。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 參數說明 |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | 是 | `"vidu_q1"`<br>[VideoModelName 枚舉中的其他模型值] | 模型名稱（預設值："vidu_q1"） |
| `first_frame` | IMAGE | 是 | - | 起始影格 |
| `end_frame` | IMAGE | 是 | - | 結束影格 |
| `prompt` | STRING | 否 | - | 用於影片生成的文字描述 |
| `duration` | INT | 否 | 5-5 | 輸出影片的持續時間（單位：秒）（預設值：5，固定為5秒） |
| `seed` | INT | 否 | 0-2147483647 | 影片生成的種子值（0表示隨機）（預設值：0） |
| `resolution` | COMBO | 否 | `"1080p"`<br>[Resolution 枚舉中的其他解析度值] | 支援的數值可能因模型和持續時間而異（預設值："1080p"） |
| `movement_amplitude` | COMBO | 否 | `"auto"`<br>[MovementAmplitude 枚舉中的其他運動幅度值] | 畫面中物體的運動幅度（預設值："auto"） |

**注意：** 起始和結束影格必須具有相容的長寬比（使用 min_rel=0.8、max_rel=1.25 的長寬比容差進行驗證）。

## 輸出結果

| 輸出名稱 | 資料類型 | 輸出說明 |
|-------------|-----------|-------------|
| `output` | VIDEO | 生成的影片檔案 |