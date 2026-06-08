## 概述
VideoLinearCFGGuidance 節點對影片模型應用線性條件引導比例，在指定範圍內調整條件與非條件成分的影響力。這能對生成過程進行動態控制，根據所需的條件程度微調模型輸出。

## 輸入

| 參數 | 說明 | 資料類型 |
| --- | --- | --- |
| `model` | model 參數代表將套用線性 CFG 引導的影片模型。此參數對於定義將透過引導比例進行修改的基礎模型至關重要。 | MODEL |
| `最小 cfg` | min_cfg 參數指定要套用的最小條件引導比例，作為線性比例調整的起點。它在決定引導比例下限方面扮演關鍵角色，進而影響模型的輸出。 | `FLOAT` |

## 輸出

| 參數 | 說明 | 資料類型 |
| --- | --- | --- |
| `model` | 輸出為輸入模型的修改版本，已套用線性 CFG 引導比例。此調整後的模型能夠根據指定的引導比例，生成具有不同程度條件影響的輸出。 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VideoLinearCFGGuidance/zh-TW.md)
