> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeSDXL/zh-TW.md)

此節點專為使用 SDXL 架構客製化的 CLIP 模型來編碼文字輸入而設計。它採用雙編碼器系統（CLIP-L 和 CLIP-G）來處理文字描述，從而實現更精確的圖像生成。

## 輸入

| 參數 | 資料類型 | 描述 |
|-----------|-----------|-------------|
| `clip` | CLIP | 用於文字編碼的 CLIP 模型實例。 |
| `width` | INT | 指定圖像寬度（像素），預設值為 1024。 |
| `height` | INT | 指定圖像高度（像素），預設值為 1024。 |
| `crop_w` | INT | 裁剪區域的寬度（像素），預設值為 0。 |
| `crop_h` | INT | 裁剪區域的高度（像素），預設值為 0。 |
| `target_width` | INT | 輸出圖像的目標寬度，預設值為 1024。 |
| `target_height` | INT | 輸出圖像的目標高度，預設值為 1024。 |
| `text_g` | STRING | 用於整體場景描述的全局文字描述。 |
| `text_l` | STRING | 用於細節描述的局部文字描述。 |

## 輸出

| 參數 | 資料類型 | 描述 |
|-----------|-----------|-------------|
| `CONDITIONING` | CONDITIONING | 包含圖像生成所需的編碼文字和條件資訊。 |