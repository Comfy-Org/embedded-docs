`CLIP Text Encode (CLIPTextEncode)` 扮演著翻譯官的角色，將您的文字描述轉換成 AI 可以理解的格式。這有助於 AI 解讀您的輸入並生成所需的圖像。

您可以將其想像為與一位使用不同語言的藝術家溝通。CLIP 模型經過大量圖像-文字配對的訓練，透過將您的描述轉換成 AI 模型可以遵循的「指令」來彌合這一差距。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `文字` | 要進行編碼的文字。支援多行輸入和動態提示詞。 | STRING | 是 | 任何文字 |
| `CLIP` | 用於編碼文字的 CLIP 模型。 | CLIP | 是 | 已載入的 CLIP 模型 |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `CONDITIONING` | 一個包含嵌入文字的條件化數據，用於引導擴散模型。 | CONDITIONING |

## 提示詞功能

### 嵌入模型

嵌入模型允許您應用特定的藝術效果或風格。支援的格式包括 `.safetensors`、`.pt` 和 `.bin`。要使用嵌入模型：

1. 將檔案放置在 `ComfyUI/models/embeddings` 資料夾中。
2. 在您的文字中使用 `embedding:模型名稱` 來引用它。

範例：如果您在 `ComfyUI/models/embeddings` 資料夾中有一個名為 `EasyNegative.pt` 的模型，那麼您可以像這樣使用它：

```
worst quality, embedding:EasyNegative, bad quality
```

**重要提示**：使用嵌入模型時，請確認檔案名稱相符且與您的模型架構相容。例如，為 SD1.5 設計的嵌入模型將無法在 SDXL 模型上正常運作。

### 提示詞權重調整

您可以使用括號來調整描述中某些部分的重要性。例如：

- `(beautiful:1.2)` 會增加「beautiful」的權重。
- `(beautiful:0.8)` 會減少「beautiful」的權重。
- 單純的括號 `(beautiful)` 將套用預設權重 1.1。

您可以使用鍵盤快捷鍵 `ctrl + 上/下箭頭` 來快速調整權重。權重調整的步長可以在設定中修改。

如果您想在提示詞中包含字面上的括號而不改變權重，可以使用反斜線進行跳脫，例如 `\(word\)`。

### 萬用字元/動態提示詞

使用 `{}` 來建立動態提示詞。例如，`{day|night|morning}` 將在每次處理提示詞時隨機選擇一個選項。

如果您想在提示詞中包含字面上的大括號而不觸發動態行為，可以使用反斜線進行跳脫，例如 `\{word\}`。

### 提示詞中的註解

您可以透過以下方式添加不會被包含在提示詞中的註解：

- 使用 `//` 來註解掉單行。
- 使用 `/* */` 來註解掉一個區塊或多行。

範例：

```
// 此行將從提示詞中排除。
a beautiful landscape, /* 此部分將被忽略 */ high quality
```

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `e8f286cdec879c529270e110ccf5959ed6df77737cfb5a8019379afac9266118`
