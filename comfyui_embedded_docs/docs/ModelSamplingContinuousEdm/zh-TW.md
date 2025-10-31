> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingContinuousEDM/zh-TW.md)

此節點旨在透過整合連續 EDM（基於能量的擴散模型）取樣技術來增強模型的取樣能力。它允許在模型取樣過程中動態調整雜訊水平，從而對生成品質和多樣性提供更精細的控制。

## 輸入參數

| 參數名稱       | 資料類型       | Python 資料類型      | 描述 |
|----------------|----------------|----------------------|------|
| `model`        | `MODEL`        | `torch.nn.Module`    | 要透過連續 EDM 取樣功能增強的基础模型。它作為應用進階取樣技術的基礎。 |
| `取樣`     | COMBO[STRING]  | `str`                | 指定要應用的取樣類型，可以是 'eps'（用於 epsilon 取樣）或 'v_prediction'（用於速度預測），這會影響模型在取樣過程中的行為。 |
| `最大 sigma`    | `FLOAT`        | `float`              | 雜訊水平的最大 sigma 值，用於控制在取樣過程中雜訊注入的上限。 |
| `最小 sigma`    | `FLOAT`        | `float`              | 雜訊水平的最小 sigma 值，設定了雜訊注入的下限，從而影響模型的取樣精度。 |

## 輸出參數

| 參數名稱 | 資料類型    | Python 資料類型      | 描述 |
|----------|-------------|----------------------|------|
| `model`  | MODEL       | `torch.nn.Module`    | 具有整合式連續 EDM 取樣功能的增強型模型，已準備好用於後續的生成任務。 |