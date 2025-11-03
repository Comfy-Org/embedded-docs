> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RunwayImageToVideoNodeGen3a/zh-TW.md)

Runway Image to Video (Gen3a Turbo) 節點使用 Runway 的 Gen3a Turbo 模型，從單一起始畫面生成影片。它接收文字提示和初始影像畫面，然後根據指定的持續時間和長寬比創建影片序列。此節點會連接到 Runway 的 API 以進行遠端生成處理。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | 是 | N/A | 用於生成影片的文字提示 (預設值: "") |
| `start_frame` | IMAGE | 是 | N/A | 用於影片生成的起始畫面 |
| `duration` | COMBO | 是 | 多個選項可用 | 從可用選項中選擇影片持續時間 |
| `ratio` | COMBO | 是 | 多個選項可用 | 從可用選項中選擇長寬比 |
| `seed` | INT | 否 | 0-4294967295 | 用於生成過程的隨機種子 (預設值: 0) |

**參數限制條件：**

- `start_frame` 的尺寸不得超過 7999x7999 像素
- `start_frame` 的長寬比必須在 0.5 到 2.0 之間
- `prompt` 必須至少包含一個字元 (不能為空)

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `output` | VIDEO | 生成的影片序列 |