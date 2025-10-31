> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeHunyuanDiT/zh-TW.md)

# `CLIPTextEncodeHunyuanDiT` 節點

`CLIPTextEncodeHunyuanDiT` 節點的主要功能是將輸入文字轉換為模型能夠理解的形式。這是一個專門針對 HunyuanDiT 模型的雙文字編碼器架構設計的高階條件化節點。
其主要角色如同翻譯器，將我們的文字描述轉換成 AI 模型能夠理解的「機器語言」。`bert` 和 `mt5xl` 輸入偏好不同類型的提示詞輸入。

## 輸入參數

| 參數名稱 | 資料類型 | 描述 |
|----------|----------|------|
| `clip` | CLIP | 用於文字標記化和編碼的 CLIP 模型實例，這是生成條件化輸出的核心組件。 |
| `bert` | STRING | 用於編碼的文字輸入，偏好短語和關鍵詞，支援多行和動態提示詞。 |
| `mt5xl` | STRING | 另一個用於編碼的文字輸入，支援多行和動態提示詞（多語言），可使用完整句子和複雜描述。 |

## 輸出參數

| 參數名稱 | 資料類型 | 描述 |
|----------|----------|------|
| `CONDITIONING` | CONDITIONING | 經過編碼的條件化輸出，用於生成任務中的後續處理。 |