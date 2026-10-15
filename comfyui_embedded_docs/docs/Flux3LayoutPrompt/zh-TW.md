# FLUX 3 Image Layout Prompt

建立 FLUX 3 Image 所讀取的版面配置表，該表由提示詞產生。此節點會取得在 Create Bounding Boxes 節點中繪製的元素，並將它們以方框清單的形式附加到你的提示詞中，每個方框都包含一個 id、其座標與其描述。在提示詞中以 `<obj_N>` 引用某個方框，即可將文字與該區域綁定，接著將輸出連接到 FLUX 3 Image 節點的 `prompt` 輸入。若未連接任何元素，則提示詞會原樣返回。

## 輸入

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `prompt` | 提示詞文字。以 `<obj_N>` 引用第 N 個方框，即可將文字與其綁定。 | STRING | 是 | - |
| `element` | 要放置在版面配置中的元素，取自 Create Bounding Boxes 節點。由於不會使用調色盤，請改在描述中說明顏色。 | ARRAY | 是 | - |

## 輸出

| Output Name | Description | Data Type |
| --- | --- | --- |
| `prompt` | 已附加方框版面配置表的提示詞，可直接饋入 FLUX 3 Image 節點。 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux3LayoutPrompt/zh-TW.md)

---
**Source fingerprint (SHA-256):** `ac8f61701c8da0a6fc8361aeebf7fc5e7aa338ce6ad8689718904caa9c53e3b8`
