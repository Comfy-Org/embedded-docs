> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PikaImageToVideoNode2_2/zh-TW.md)

Pika Image to Video 節點將圖像和文字提示發送至 Pika API 2.2 版本以生成影片。它會根據提供的描述和設定，將輸入圖像轉換為影片格式。此節點負責處理 API 通訊，並返回生成的影片作為輸出。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 參數說明 |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | 是 | - | 要轉換為影片的圖像 |
| `prompt_text` | STRING | 是 | - | 指導影片生成的文字描述 |
| `negative_prompt` | STRING | 是 | - | 描述影片中應避免內容的文字 |
| `seed` | INT | 是 | - | 用於可重現結果的隨機種子值 |
| `resolution` | STRING | 是 | - | 輸出影片解析度設定 |
| `duration` | INT | 是 | - | 生成影片的長度（單位：秒） |

## 輸出結果

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `output` | VIDEO | 生成的影片檔案 |