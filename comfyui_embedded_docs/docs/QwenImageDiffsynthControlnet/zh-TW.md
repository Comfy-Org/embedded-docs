# QwenImageDiffsynthControlnet

QwenImageDiffsynthControlnet 節點將擴散合成控制網路補丁套用至基礎模型。它使用輸入影像以及可選的遮罩，以可調整的強度引導模型的生成過程，產生整合控制網路影響力的修補後模型，以實現更受控制的影像合成。

## 輸入

| 參數 | 描述 | 資料型別 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 要套用控制網路補丁的基礎模型 | MODEL | 是 | - |
| `model_patch` | 要套用至基礎模型的控制網路補丁模型 | MODEL_PATCH | 是 | - |
| `vae` | 擴散過程中使用的 VAE（變分自編碼器） | VAE | 是 | - |
| `image` | 用於引導控制網路的輸入影像。僅使用前三個色彩通道（RGB）；任何額外的通道都會被丟棄 | IMAGE | 是 | - |
| `strength` | 控制網路影響的強度（預設值：1.0） | FLOAT | 是 | -10.0 到 10.0 |
| `mask` | 可選遮罩，定義應套用控制網路的區域。此遮罩在內部使用前會被反轉 | MASK | 否 | - |

**注意：** 當提供遮罩時，它會自動反轉（1.0 - 遮罩）並調整形狀以符合控制網路處理所需的預期維度。此節點會根據模型補丁是 ZImage Control 類型還是標準 DiffSynth 控制網路，使用不同的內部處理方法。此節點被標記為實驗性。

## 輸出

| 輸出名稱 | 描述 | 資料型別 |
| --- | --- | --- |
| `model` | 已套用擴散合成控制網路補丁的修改後模型 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QwenImageDiffsynthControlnet/zh-TW.md)

---
**Source fingerprint (SHA-256):** `56739c098933cb70d3bcb8d6b251da33e7879b464b2e8a7296da085aefc15698`
