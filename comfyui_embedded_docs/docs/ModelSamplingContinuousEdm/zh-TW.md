此節點旨在透過整合連續 EDM（基於能量的擴散模型）取樣技術，來增強模型的取樣能力。它允許在模型的取樣過程中動態調整雜訊等級，從而對生成品質與多樣性提供更精細的控制。

## 輸入

| 參數 | 說明 | 資料類型 | Python dtype |
| --- | --- | --- | --- |
| `model` | 要增強連續 EDM 取樣能力的模型，作為應用進階取樣技術的基礎。 | `MODEL` | `torch.nn.Module` |
| `取樣` | 指定要套用的取樣類型，可選 'eps'（epsilon 取樣）或 'v_prediction'（速度預測），影響模型在取樣過程中的行為。 | COMBO[STRING] | `str` |
| `最大 sigma` | 雜訊等級的最大 sigma 值，用於控制取樣過程中雜訊注入的上限。 | `FLOAT` | `float` |
| `最小 sigma` | 雜訊等級的最小 sigma 值，設定雜訊注入的下限，從而影響模型的取樣精確度。 | `FLOAT` | `float` |

## 輸出

| 參數 | 說明 | 資料類型 | Python dtype |
| --- | --- | --- | --- |
| `model` | 已整合連續 EDM 取樣能力的增強模型，可直接用於後續的生成任務。 | MODEL | `torch.nn.Module` |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingContinuousEDM/zh-TW.md)
