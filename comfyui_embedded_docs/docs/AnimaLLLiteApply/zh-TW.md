# AnimaLLLiteApply

此節點對擴散模型應用輕量級動畫修補程式，實現具有可調整強度與時序控制的受控影像生成。它將預先配置的模型修補程式與輸入影像及可選遮罩整合，修改模型的注意力層與 MLP 層以影響生成過程。

## 輸入
| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | 要套用修補程式的基础擴散模型 | MODEL | 是 | |
| `model_patch` | 預先配置的動畫修補程式 | MODEL_PATCH | 是 | |
| `image` | 用於引導生成的參考影像 | IMAGE | 是 | |
| `strength` | 修補程式的效果強度（預設值：1.0） | FLOAT | 是 | -10.0 至 10.0 |
| `start_percent` | 修補程式開始生效的降噪過程百分比（預設值：0.0） | FLOAT | 是 | 0.0 至 1.0 |
| `end_percent` | 修補程式停止生效的降噪過程百分比（預設值：1.0） | FLOAT | 是 | 0.0 至 1.0 |
| `mask` | 可選遮罩，用於將修補程式效果限制在影像的特定區域 | MASK | 否 | |

**參數限制說明：** 若 `model_patch` 具有 4 個輸入通道且未提供 `mask`，系統會自動建立與影像尺寸相符的零遮罩。若 `model_patch` 不具有 4 個輸入通道，則 `mask` 參數會被忽略並設為 `None`。

## 輸出
| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `MODEL` | 已套用動畫修補程式的修補後擴散模型 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AnimaLLLiteApply/zh-TW.md)

---
**Source fingerprint (SHA-256):** `291dc6a6619faab1c1100110c71c47381addcd80dbaf933dd8025a376bc2bee7`
