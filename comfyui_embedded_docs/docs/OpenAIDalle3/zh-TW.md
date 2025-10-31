> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIDalle3/zh-TW.md)

透過 OpenAI 的 DALL·E 3 端點同步生成圖像。此節點接收文字提示，並使用 OpenAI 的 DALL·E 3 模型創建相應的圖像，允許您指定圖像品質、風格和尺寸。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `提示詞` | STRING | 是 | - | 用於 DALL·E 的文字提示 (預設值: "") |
| `種子` | INT | 否 | 0 到 2147483647 | 後端尚未實現此功能 (預設值: 0) |
| `畫質` | COMBO | 否 | "standard"<br>"hd" | 圖像品質 (預設值: "standard") |
| `風格` | COMBO | 否 | "natural"<br>"vivid" | Vivid 會使模型傾向於生成超現實且戲劇化的圖像。Natural 會使模型產生更自然、較不超現實的圖像。(預設值: "natural") |
| `尺寸` | COMBO | 否 | "1024x1024"<br>"1024x1792"<br>"1792x1024" | 圖像尺寸 (預設值: "1024x1024") |

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `IMAGE` | IMAGE | 由 DALL·E 3 生成的圖像 |