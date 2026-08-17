# 模型取樣 SD3

The ModelSamplingSD3 node applies Stable Diffusion 3 sampling parameters to a model. It modifies the model's sampling behavior by adjusting the shift parameter, which controls the sampling distribution characteristics. The node creates a modified copy of the input model with the specified sampling configuration applied.

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 要套用 SD3 取樣參數的輸入模型 | MODEL | 是 | - |
| `shift` | 控制取樣位移參數（預設值：3.0） | FLOAT | 是 | 0.0 - 100.0 |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `model` | 已套用 SD3 取樣參數的修改後模型 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingSD3/zh-TW.md)

---
**Source fingerprint (SHA-256):** `46d44786422c2efea78c1fe7e1183cebc9bf51d4f13861da04d5a974b5b6da7d`
