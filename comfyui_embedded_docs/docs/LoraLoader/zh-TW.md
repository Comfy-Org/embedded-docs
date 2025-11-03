> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoraLoader/zh-TW.md)

此節點會自動偵測位於 LoRA 資料夾（包含子資料夾）中的模型，對應的模型路徑為 `ComfyUI\models\loras`。更多資訊請參考安裝 LoRA 模型。

LoRA 載入器節點主要用於載入 LoRA 模型。您可以將 LoRA 模型視為濾鏡，能為您的影像賦予特定風格、內容和細節：

- 套用特定藝術風格（如水墨畫）
- 添加特定角色特徵（如遊戲角色）
- 為影像添加特定細節
這些都可以透過 LoRA 來實現。

如果您需要載入多個 LoRA 模型，可以直接將多個節點串聯在一起，如下所示：

## 輸入參數

| 參數名稱 | 資料類型 | 描述 |
| --- | --- | --- |
| `model` | MODEL | 通常用於連接基礎模型 |
| `clip` | CLIP | 通常用於連接 CLIP 模型 |
| `lora_name` | COMBO[STRING] | 選擇要使用的 LoRA 模型名稱 |
| `strength_model` | FLOAT | 數值範圍從 -100.0 到 100.0，日常影像生成通常使用 0~1 之間的值。數值越高，模型調整效果越明顯 |
| `strength_clip` | FLOAT | 數值範圍從 -100.0 到 100.0，日常影像生成通常使用 0~1 之間的值。數值越高，模型調整效果越明顯 |

## 輸出參數

| 參數名稱 | 資料類型 | 描述 |
| --- | --- | --- |
| `model` | MODEL | 已套用 LoRA 調整的模型 |
| `clip` | CLIP | 已套用 LoRA 調整的 CLIP 實例 |