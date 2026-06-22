# 載入 LoRA

此節點會自動偵測位於 LoRA 資料夾（包含子資料夾）中的模型，對應的模型路徑為 `ComfyUI\models\loras`。如需更多資訊，請參閱安裝 LoRA 模型。

LoRA 載入器節點主要用於載入 LoRA 模型。您可以將 LoRA 模型視為濾鏡，能夠為您的圖像賦予特定的風格、內容和細節：

- 套用特定的藝術風格（例如水墨畫）
- 添加特定角色的特徵（例如遊戲角色）
- 為圖像添加特定細節
所有這些都可以透過 LoRA 實現。

如果您需要載入多個 LoRA 模型，可以直接將多個節點串聯在一起，如下所示：

## 輸入

| 參數 | 說明 | 資料類型 |
| --- | --- | --- |
| `model` | 通常用於連接基礎模型 | MODEL |
| `clip` | 通常用於連接 CLIP 模型 | CLIP |
| `lora_name` | 選擇要使用的 LoRA 模型名稱 | COMBO[STRING] |
| `strength_model` | 數值範圍從 -100.0 到 100.0，日常圖像生成通常使用 0~1 之間。數值越高，模型調整效果越明顯 | FLOAT |
| `strength_clip` | 數值範圍從 -100.0 到 100.0，日常圖像生成通常使用 0~1 之間。數值越高，模型調整效果越明顯 | FLOAT |

## 輸出

| 參數 | 說明 | 資料類型 |
| --- | --- | --- |
| `model` | 已套用 LoRA 調整的模型 | MODEL |
| `clip` | 已套用 LoRA 調整的 CLIP 實例 | CLIP |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoraLoader/zh-TW.md)
