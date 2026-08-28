# CFGGuider

CFG 引導器節點建立一個引導系統，用於控制影像生成過程中的取樣。它接收一個模型以及正向與負向條件輸入，然後套用無分類器引導尺度，將生成導向所需的內容，同時避開不需要的元素。此節點輸出一個引導器物件，可供取樣節點用來控制影像生成方向。

## 輸入
| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 用於引導的模型 | MODEL | 是 | - |
| `正向` | 正向條件，引導生成朝向所需的內容 | CONDITIONING | 是 | - |
| `負向` | 負向條件，使生成遠離不需要的內容 | CONDITIONING | 是 | - |
| `cfg` | 無分類器引導尺度，控制條件對生成的影響強度（預設值：8.0） | FLOAT | 是 | 0.0 至 100.0 |

## 輸出
| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `GUIDER` | 引導器物件，可傳遞給取樣節點以控制生成過程 | GUIDER |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CFGGuider/zh-TW.md)

---
**Source fingerprint (SHA-256):** `73b57bfbb6d4fc083a8089bc0f786f82d03e0d7b2faeeb7a42b3d87e38047b9e`
