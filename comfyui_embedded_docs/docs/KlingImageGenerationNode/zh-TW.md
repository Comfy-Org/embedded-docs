> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingImageGenerationNode/zh-TW.md)

Kling 圖像生成節點能根據文字提示生成圖像，並可選擇使用參考圖像作為引導。它會根據您的文字描述和參考設定創建一張或多張圖像，然後將生成的圖像作為輸出返回。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 參數說明 |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | 是 | - | 正向文字提示 |
| `negative_prompt` | STRING | 是 | - | 負向文字提示 |
| `image_type` | COMBO | 是 | 選項來自 KlingImageGenImageReferenceType<br>(從原始碼提取) | 圖像參考類型選擇 |
| `image_fidelity` | FLOAT | 是 | 0.0 - 1.0 | 用戶上傳圖像的參考強度 (預設值: 0.5) |
| `human_fidelity` | FLOAT | 是 | 0.0 - 1.0 | 主體參考相似度 (預設值: 0.45) |
| `model_name` | COMBO | 是 | "kling-v1"<br>(以及 KlingImageGenModelName 的其他選項) | 圖像生成的模型選擇 (預設值: "kling-v1") |
| `aspect_ratio` | COMBO | 是 | "16:9"<br>(以及 KlingImageGenAspectRatio 的其他選項) | 生成圖像的長寬比 (預設值: "16:9") |
| `n` | INT | 是 | 1 - 9 | 生成圖像的數量 (預設值: 1) |
| `image` | IMAGE | 否 | - | 可選的參考圖像 |

**參數限制：**

- `image` 參數為可選，但當提供圖像時，kling-v1 模型不支援參考圖像
- 正向提示和負向提示有最大長度限制 (MAX_PROMPT_LENGTH_IMAGE_GEN)
- 當未提供參考圖像時，`image_type` 參數會自動設為 None

## 輸出結果

| 輸出名稱 | 資料類型 | 輸出說明 |
|-------------|-----------|-------------|
| `output` | IMAGE | 根據輸入參數生成的圖像 |