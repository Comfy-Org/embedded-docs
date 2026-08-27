# 模型取樣 SD3

## 輸入
| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 要套用 SD3 取樣參數的輸入模型 | MODEL | 是 | - |
| `偏移` | 控制取樣偏移參數（預設值：3.0） | FLOAT | 是 | 0.0 - 100.0 (step: 0.01) |

注意：此節點會以固定的內部倍數 1000 套用 `shift` 值。若原始模型具有雜訊尺度設定，其將保留在修改後的模型中。

## 輸出
| 輸出名 | 描述 | 資料類型 |
| --- | --- | --- |
| `model` | 已套用 SD3 取樣參數的修改後模型 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingSD3/zh-TW.md)

---
**Source fingerprint (SHA-256):** `46d44786422c2efea78c1fe7e1183cebc9bf51d4f13861da04d5a974b5b6da7d`
