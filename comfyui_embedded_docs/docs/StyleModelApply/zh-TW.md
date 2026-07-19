# 套用風格模型

此節點將風格模型應用於給定的條件化資料，根據 CLIP 視覺模型的輸出增強或改變其風格。它將風格模型的條件化整合到現有條件化中，從而在生成過程中實現風格的無縫融合。

## 輸入

### {heading_required}

| 參數 | 描述 | Comfy dtype |
| --- | --- | --- |
| `條件設定` | 原始的條件化資料，風格模型的條件化將應用於此。它對於定義將被增強或改變的基礎上下文或風格至關重要。 | `CONDITIONING` |
| `style_model` | 用於根據 CLIP 視覺模型的輸出生成新條件化的風格模型。它在定義要應用的新風格方面扮演關鍵角色。 | `STYLE_MODEL` |
| `clip_vision_output` | 來自 CLIP 視覺模型的輸出，風格模型使用它來生成新的條件化。它提供了風格應用所需的視覺上下文。 | `CLIP_VISION_OUTPUT` |

## 輸出

| 參數 | 描述 | Comfy dtype |
| --- | --- | --- |
| `條件設定` | 增強或改變後的條件化資料，包含了風格模型的輸出。它代表最終、已套用風格的條件化，可供進一步處理或生成使用。 | `CONDITIONING` |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StyleModelApply/zh-TW.md)
