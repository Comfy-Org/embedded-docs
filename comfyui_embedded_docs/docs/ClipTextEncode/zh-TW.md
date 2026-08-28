# ClipTextEncode

`CLIP Text Encode (CLIPTextEncode)` 扮演翻譯者的角色，將你的文字描述轉換成 AI 可以理解的格式。這有助於 AI 解讀你的輸入並產生所需的影像。

你可以把它想像成與一位使用不同語言的藝術家溝通。CLIP 模型經過大量圖像-文字配對的訓練，能將你的描述轉換成 AI 模型可以遵循的「指令」，從而彌合這個差距。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `文字` | 要編碼的文字。支援多行輸入與動態提示詞。 | STRING | 是 | 任意文字 |
| `CLIP` | 用於編碼文字的 CLIP 模型。 | CLIP | 是 | 已載入的 CLIP 模型 |

注意：如果 `clip` 輸入為 None（例如，來自 checkpoint 載入器，且其 checkpoint 不包含有效的 CLIP 或文字編碼器模型），則此節點會引發錯誤。

## 輸出

| 輸出名 | 說明 | 資料類型 |
| --- | --- | --- |
| `CONDITIONING` | 一種包含嵌入文字的 conditioning，用於引導擴散模型。 | CONDITIONING |

## 提示詞功能

### Embedding 模型

Embedding 模型可讓你套用特定的藝術效果或風格。支援的格式包括 `.safetensors`、`.pt` 和 `.bin`。若要使用 embedding 模型：

1. 將檔案放在 `ComfyUI/models/embeddings` 資料夾中。
2. 在文字中使用 `embedding:model_name` 來引用它。

範例：如果你的 `ComfyUI/models/embeddings` 資料夾中有一個名為 `EasyNegative.pt` 的模型，你可以這樣使用它：

```
worst quality, embedding:EasyNegative, bad quality
```

**重要**：使用 embedding 模型時，請確認檔案名稱與你的模型架構相符且相容。例如，專為 SD1.5 設計的 embedding 無法在 SDXL 模型上正常運作。

### 提示詞權重調整

你可以使用括號調整描述中某些部分的重要性。例如：

- `(beautiful:1.2)` 提高「beautiful」的權重。
- `(beautiful:0.8)` 降低「beautiful」的權重。
- 單純的括號 `(beautiful)` 會套用預設權重 1.1。

你可以使用鍵盤快捷鍵 `ctrl + up/down arrow` 快速調整權重。權重調整的步進值可以在設定中修改。

如果你想要在提示詞中包含字面上的括號而不改變權重，可以使用反斜線跳脫，例如 `\(word\)`。

### 萬用字元／動態提示詞

使用 `{}` 建立動態提示詞。例如，`{day|night|morning}` 每次處理提示詞時會隨機選擇一個選項。

如果你想要在提示詞中包含字面上的大括號而不觸發動態行為，可以使用反斜線跳脫，例如 `\{word\}`。

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ClipTextEncode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `ace7988df7aaa3ac26419b16a9bd8908a327da6e82c21c2b2704af091d2e76e7`
