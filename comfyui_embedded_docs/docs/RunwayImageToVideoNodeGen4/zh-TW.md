> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RunwayImageToVideoNodeGen4/zh-TW.md)

Runway Image to Video (Gen4 Turbo) 節點使用 Runway 的 Gen4 Turbo 模型，從單一起始畫面生成影片。它接收文字提示和初始影像畫面，然後根據提供的持續時間和長寬比設定建立影片序列。此節點會處理將起始畫面上傳至 Runway API 並回傳生成的影片。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | 是 | - | 用於生成影片的文字提示（預設：空字串） |
| `start_frame` | IMAGE | 是 | - | 用於影片生成的起始畫面 |
| `duration` | COMBO | 是 | 提供多個選項 | 從可用的持續時間選項中選擇影片長度 |
| `ratio` | COMBO | 是 | 提供多個選項 | 從可用的 Gen4 Turbo 長寬比選項中選擇畫面比例 |
| `seed` | INT | 否 | 0 到 4294967295 | 用於生成過程的隨機種子（預設：0） |

**參數限制：**

- `start_frame` 影像的尺寸不得超過 7999x7999 像素
- `start_frame` 影像的長寬比必須在 0.5 到 2.0 之間
- `prompt` 必須至少包含一個字元

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `output` | VIDEO | 基於輸入畫面和提示所生成的影片 |