> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeSDXL/zh-TW.md)

{heading_overview}

此節點專為使用針對 SDXL 架構特別定制的 CLIP 模型來編碼文字輸入而設計。它採用雙編碼器系統（CLIP-L 和 CLIP-G）來處理文字描述，從而實現更準確的影像生成。

{heading_inputs}

| 參數 | 資料類型 | 描述 |
|-----------|-----------|-------------|
| `clip` | CLIP | 用於文字編碼的 CLIP 模型實例。 |
| `width` | INT | 指定影像寬度（像素），預設值為 1024。 |
| `height` | INT | 指定影像高度（像素），預設值為 1024。 |
| `crop_w` | INT | 裁切區域的寬度（像素），預設值為 0。 |
| `crop_h` | INT | 裁切區域的高度（像素），預設值為 0。 |
| `target_width` | INT | 輸出影像的目標寬度，預設值為 1024。 |
| `target_height` | INT | 輸出影像的目標高度，預設值為 1024。 |
| `text_g` | STRING | 全域文字描述，用於整體場景描述。 |
| `text_l` | STRING | 局部文字描述，用於細節描述。 |

{heading_outputs}

| 參數 | 資料類型 | 描述 |
|-----------|-----------|-------------|
| `CONDITIONING` | CONDITIONING | 包含影像生成所需的編碼文字和條件資訊。 |