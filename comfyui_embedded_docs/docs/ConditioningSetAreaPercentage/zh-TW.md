## 概述
ConditioningSetAreaPercentage 節點專門用於根據百分比值調整條件元素的影響區域。它允許將區域的尺寸和位置指定為總影像大小的百分比，並透過強度參數來調節條件效果的程度。

## 輸入

| 參數 | 說明 | 資料類型 |
| --- | --- | --- |
| `CONDITIONING` | 代表要修改的條件元素，作為應用區域和強度調整的基礎。 | CONDITIONING |
| `寬度` | 指定區域寬度佔總影像寬度的百分比，影響條件在水平方向上對影像的影響範圍。 | `FLOAT` |
| `高度` | 決定區域高度佔總影像高度的百分比，影響條件在垂直方向上的影響範圍。 | `FLOAT` |
| `X 座標` | 指示區域的水平起始點佔總影像寬度的百分比，用於定位條件效果。 | `FLOAT` |
| `Y 座標` | 指定區域的垂直起始點佔總影像高度的百分比，用於定位條件效果。 | `FLOAT` |
| `強度` | 控制指定區域內條件效果的強度，允許微調其影響程度。 | `FLOAT` |

## 輸出

| 參數 | 說明 | 資料類型 |
| --- | --- | --- |
| `CONDITIONING` | 返回已更新區域和強度參數的修改後條件元素，可供進一步處理或應用。 | CONDITIONING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetAreaPercentage/zh-TW.md)
