# Tome 修補模型

TomePatchModel 節點對擴散模型套用 Token 合併（ToMe），以降低推論期間的計算需求。其運作方式是選擇性地合併注意力機制中相似的 token，使模型能處理較少的 token，同時維持圖像品質。這項技術有助於加快生成速度，且不會造成顯著的品質損失。

## 輸入
| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 要套用 token 合併的擴散模型 | MODEL | 是 | - |
| `ratio` | 要合併的 token 比例（預設值：0.3，步長：0.01）。數值越高會合併越多 token，進而大幅加速，但可能降低品質。 | FLOAT | 是 | 0.0 - 1.0 |

## 輸出
| 輸出名 | 描述 | 資料類型 |
| --- | --- | --- |
| `model` | 已套用 token 合併的修改後模型 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TomePatchModel/zh-TW.md)

---
**Source fingerprint (SHA-256):** `1202c0df17f357440cd156fa0920f70c18a318e32c41dc04cecff11613f0072f`
