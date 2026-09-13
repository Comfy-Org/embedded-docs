# ClipTextEncode

使用 CLIP 模型將文字提示詞編碼為嵌入，可用於引導擴散模型生成特定圖像。

`CLIP Text Encode (CLIPTextEncode)` 扮演翻譯器的角色，將你的文字描述轉換為 AI 能理解的格式。這能協助 AI 解讀你的輸入並生成想要的圖像。

可以把它想像成與一位說不同語言的藝術家溝通。CLIP 模型在大量圖像-文字配對上訓練，能將你的描述轉換成 AI 模型可遵循的「指令」，藉此彌合這個差距。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `文字` | 要編碼的文字。支援多行輸入與動態提示詞。 | STRING | 是 | 任意文字 |
| `CLIP` | 用於編碼文字的 CLIP 模型。 | CLIP | 是 | 已載入的 CLIP 模型 |

注意：如果 `clip` 輸入為 None（例如來自 checkpoint 載入器，而該 checkpoint 不包含有效的 CLIP 或文字編碼器模型），則此節點會引發錯誤。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `CONDITIONING` | 包含嵌入文字的條件，用於引導擴散模型。 | CONDITIONING |

## 提示詞功能

### 嵌入模型

嵌入模型可讓你套用特定的藝術效果或風格。支援的格式包括 `.safetensors`、`.pt` 和 `.bin`。若要使用嵌入模型：

1. 將檔案放到 `ComfyUI/models/embeddings` 資料夾中。
2. 在文字中使用 `embedding:model_name` 來引用它。

範例：如果你的 `ComfyUI/models/embeddings` 資料夾中有一個名為 `EasyNegative.pt` 的模型，則可以這樣使用：

```
worst quality, embedding:EasyNegative, bad quality
```

**重要**：使用嵌入模型時，請確認檔案名稱正確，且與你的模型架構相容。例如，為 SD1.5 設計的嵌入模型無法在 SDXL 模型上正確運作。

### 提示詞權重調整

你可以使用括號調整描述中特定部分的重要性。例如：

- `(beautiful:1.2)` 會增加「beautiful」的權重。
- `(beautiful:0.8)` 會降低「beautiful」的權重。
- 單純的括號 `(beautiful)` 會套用預設權重 1.1。

你可以使用鍵盤快速鍵 `ctrl + up/down arrow` 快速調整權重。權重調整的間隔大小可在設定中修改。

如果你想在提示詞中加入字面上的括號，而不改變權重，可以使用反斜線來跳脫，例如 `\(word\)`。

### 萬用字元/動態提示詞

使用 `{}` 建立動態提示詞。例如，`{day|night|morning}` 會在每次處理提示詞時隨機選取一個選項。

如果你想在提示詞中加入字面的大括號，而不觸發動態行為，可以使用反斜線來跳脫，例如 `\{word\}`。

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ClipTextEncode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `ace7988df7aaa3ac26419b16a9bd8908a327da6e82c21c2b2704af091d2e76e7`
