> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoraSave/zh-TW.md)

LoraSave 節點從模型差異中提取並儲存 LoRA（低秩適應）檔案。它可以處理擴散模型差異、文字編碼器差異或兩者，並將其轉換為具有指定秩和類型的 LoRA 格式。生成的 LoRA 檔案將儲存到輸出目錄中以供後續使用。

## 輸入參數

| 參數名稱 | 資料類型 | 是否必填 | 數值範圍 | 參數說明 |
|-----------|-----------|----------|-------|-------------|
| `filename_prefix` | STRING | 是 | - | 輸出檔案名稱的前綴（預設值："loras/ComfyUI_extracted_lora"） |
| `rank` | INT | 是 | 1-4096 | LoRA 的秩值，控制大小和複雜度（預設值：8） |
| `lora_type` | COMBO | 是 | 提供多種選項 | 要建立的 LoRA 類型，提供多種可用選項 |
| `bias_diff` | BOOLEAN | 是 | - | 是否在 LoRA 計算中包含偏差差異（預設值：True） |
| `model_diff` | MODEL | 否 | - | 要轉換為 LoRA 的 ModelSubtract 輸出 |
| `text_encoder_diff` | CLIP | 否 | - | 要轉換為 LoRA 的 CLIPSubtract 輸出 |

**注意：** 必須提供 `model_diff` 或 `text_encoder_diff` 中的至少一個參數，節點才能正常運作。如果兩者都未提供，節點將不會產生任何輸出。

## 輸出結果

| 輸出名稱 | 資料類型 | 輸出說明 |
|-------------|-----------|-------------|
| - | - | 此節點會將 LoRA 檔案儲存到輸出目錄，但不會透過工作流程返回任何資料 |