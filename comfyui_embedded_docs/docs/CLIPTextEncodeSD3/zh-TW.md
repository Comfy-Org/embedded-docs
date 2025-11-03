> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeSD3/zh-TW.md)

CLIPTextEncodeSD3 節點透過使用不同的 CLIP 模型編碼多個文字提示，為 Stable Diffusion 3 模型處理文字輸入。它處理三個獨立的文字輸入（clip_g、clip_l 和 t5xxl），並提供管理空白文字填充的選項。該節點確保不同文字輸入之間的標記正確對齊，並返回適用於 SD3 生成流程的調節資料。

## 輸入參數

| 參數名稱 | 資料類型 | 輸入類型 | 預設值 | 數值範圍 | 描述 |
|-----------|-----------|------------|---------|-------|-------------|
| `clip` | CLIP | 必填 | - | - | 用於文字編碼的 CLIP 模型 |
| `clip_l` | STRING | 多行文字，動態提示 | - | - | 用於本地 CLIP 模型的文字輸入 |
| `clip_g` | STRING | 多行文字，動態提示 | - | - | 用於全域 CLIP 模型的文字輸入 |
| `t5xxl` | STRING | 多行文字，動態提示 | - | - | 用於 T5-XXL 模型的文字輸入 |
| `空白填充` | COMBO | 選擇 | - | ["none", "empty_prompt"] | 控制如何處理空白文字輸入 |

**參數限制：**

- 當 `empty_padding` 設為 "none" 時，`clip_g`、`clip_l` 或 `t5xxl` 的空白文字輸入將產生空白標記列表，而非填充內容
- 當長度不同時，該節點會透過用空白標記填充較短的輸入，自動平衡 `clip_l` 和 `clip_g` 輸入之間的標記長度
- 所有文字輸入均支援動態提示和多行文字輸入

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `CONDITIONING` | CONDITIONING | 已編碼的文字調節資料，準備好用於 SD3 生成流程 |