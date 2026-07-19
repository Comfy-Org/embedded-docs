# 模型取樣離散

此節點旨在透過應用離散取樣策略來修改模型的取樣行為。它允許選擇不同的取樣方法，例如 epsilon、v_prediction、lcm 或 x0，並可選擇根據零樣本雜訊比（zsnr）設定來調整模型的降噪策略。

## 輸入

| 參數 | 說明 | 資料類型 | Python 資料類型 |
| --- | --- | --- | --- |
| `model` | 將套用離散取樣策略的模型。此參數至關重要，因為它定義了將進行修改的基礎模型。 | MODEL | `torch.nn.Module` |
| `取樣` | 指定要套用於模型的離散取樣方法。方法的選擇會影響模型生成樣本的方式，提供不同的取樣策略。 | COMBO[STRING] | `str` |
| `zsnr` | 一個布林標誌，啟用時會根據零樣本雜訊比調整模型的降噪策略。這可能影響生成樣本的品質和特性。 | `BOOLEAN` | `bool` |

## 輸出

| 參數 | 說明 | 資料類型 | Python 資料類型 |
| --- | --- | --- | --- |
| `model` | 已套用離散取樣策略的修改後模型。此模型現在能夠使用指定的方法和調整來生成樣本。 | MODEL | `torch.nn.Module` |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingDiscrete/zh-TW.md)
