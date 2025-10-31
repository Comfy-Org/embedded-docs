> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ViduImageToVideoNode/zh-TW.md)

Vidu Image To Video Generation 節點可從起始圖像和可選的文字描述創建影片。它使用 AI 模型生成從提供的圖像幀延伸的影片內容。該節點將圖像和參數發送到外部服務，並返回生成的影片。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | 是 | `vidu_q1`<br>*其他 VideoModelName 選項* | 模型名稱（預設值：vidu_q1） |
| `image` | IMAGE | 是 | - | 用作生成影片起始畫面的圖像 |
| `prompt` | STRING | 否 | - | 用於影片生成的文字描述（預設值：空） |
| `duration` | INT | 否 | 5-5 | 輸出影片的持續時間（單位：秒）（預設值：5，固定為 5 秒） |
| `seed` | INT | 否 | 0-2147483647 | 影片生成的隨機種子（0 表示隨機）（預設值：0） |
| `resolution` | COMBO | 否 | `r_1080p`<br>*其他 Resolution 選項* | 支援的數值可能因模型和持續時間而異（預設值：r_1080p） |
| `movement_amplitude` | COMBO | 否 | `auto`<br>*其他 MovementAmplitude 選項* | 畫面中物體的運動幅度（預設值：auto） |

**限制條件：**

- 僅允許輸入一張圖像（無法處理多張圖像）
- 輸入圖像的長寬比必須在 1:4 到 4:1 之間

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `output` | VIDEO | 生成的影片輸出 |