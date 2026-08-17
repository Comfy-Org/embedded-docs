# CLIP 文字編碼（提示詞）

`CLIP Text Encode (CLIPTextEncode)` 扮演翻譯者的角色，將你的文字描述轉換為 AI 可以理解的格式。這有助於 AI 解讀你的輸入並產生所需的影像。

你可以把它想成是與一位說不同語言的藝術家溝通。CLIP 模型透過大量影像-文字配對資料進行訓練，能將你的描述轉換成 AI 模型可以遵循的「指令」，從而彌補這之間的差距。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `text` | 要編碼的文字。支援多行輸入和動態提示詞。 | STRING | 是 | 任何文字 |
| `clip` | 用於編碼文字的 CLIP 模型。 | CLIP | 是 | 已載入的 CLIP 模型 |

**注意**：`clip` 輸入必須是有效的 CLIP 模型。如果它是 `None`，節點會產生錯誤。這通常發生在 checkpoint 載入節點所載入的 checkpoint 不包含有效的 CLIP 或文字編碼器模型時。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `CONDITIONING` | 包含嵌入文字的 conditioning，用於引導擴散模型。 | CONDITIONING |

## 提示詞功能

### 嵌入模型

嵌入模型可讓你套用特定的藝術效果或風格。支援的格式包括 `.safetensors`、`.pt` 和 `.bin`。若要使用嵌入模型：

1. 將檔案放入 `ComfyUI/models/embeddings` 資料夾中。
2. 在文字中使用 `embedding:model_name` 來引用它。

範例：如果你有一個名為 `EasyNegative.pt` 的模型放在 `ComfyUI/models/embeddings` 資料夾中，則可以這樣使用：

```
worst quality, embedding:EasyNegative, bad quality
```

**重要**：使用嵌入模型時，請確認檔案名稱與你的模型架構相符且相容。例如，專為 SD1.5 設計的嵌入模型無法在 SDXL 模型上正確運作。

### 提示詞權重調整

你可以使用括號來調整描述中某些部分的重要性。例如：

- `(beautiful:1.2)` 會增加「beautiful」的權重。
- `(beautiful:0.8)` 會降低「beautiful」的權重。
- 單純的括號 `(beautiful)` 會套用預設權重 1.1。

你可以使用鍵盤快捷鍵 `ctrl + 上/下箭頭` 快速調整權重。權重調整的步進值可以在設定中修改。

如果你希望在提示詞中包含字面上的括號而不改變權重，可以使用反斜線進行跳脫，例如 `\(word\)`。

### 萬用字元/動態提示詞

使用 `{}` 來建立動態提示詞。例如，`{day|night|morning}` 會在每次處理提示詞時隨機選擇其中一個選項。

如果你希望在提示詞中包含字面上的大括號而不觸發動態行為，可以使用反斜線進行跳脫，例如 `\{word\}`。

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `ace7988df7aaa3ac26419b16a9bd8908a327da6e82c21c2b2704af091d2e76e7`
