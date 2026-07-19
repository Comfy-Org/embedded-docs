# LTXV 預處理

LTXVPreprocess 節點對影像套用壓縮預處理。它接收輸入影像，並以指定的壓縮等級進行處理，輸出已套用壓縮設定的處理後影像。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `影像` | 要處理的輸入影像 | IMAGE | 是 | - |
| `img_compression` | 套用於影像的壓縮量（預設值：35） | INT | 否 | 0-100 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `output_image` | 已套用壓縮的處理後輸出影像 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVPreprocess/zh-TW.md)

---
**Source fingerprint (SHA-256):** `2c5fbde5d011bdf3313ca05508f58a13eaae0bdff12f3659fef281c0045e480d`
