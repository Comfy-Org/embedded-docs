# CFGGuider

CFGGuider 節點建立一個引導系統，用於控制影像生成中的取樣過程。它接收模型以及正向和負向條件輸入，然後套用無分類器引導尺度，將生成過程導向所需內容，同時避免不需要的元素。此節點輸出一個 guider 物件，可供取樣節點用來控制影像生成方向。

## 輸入
| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `model` | 用於引導的模型 | MODEL | Yes | - |
| `positive` | 正向條件，引導生成朝向所需內容 | CONDITIONING | Yes | - |
| `negative` | 負向條件，使生成遠離不需要的內容 | CONDITIONING | Yes | - |
| `cfg` | 無分類器引導尺度，控制條件影響生成的強度（預設值：8.0） | FLOAT | Yes | 0.0 to 100.0 |

## 輸出
| Output Name | Description | Data Type |
| --- | --- | --- |
| `GUIDER` | 一個 guider 物件，可傳遞給取樣節點以控制生成過程 | GUIDER |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CFGGuider/zh-TW.md)

---
**Source fingerprint (SHA-256):** `73b57bfbb6d4fc083a8089bc0f786f82d03e0d7b2faeeb7a42b3d87e38047b9e`
