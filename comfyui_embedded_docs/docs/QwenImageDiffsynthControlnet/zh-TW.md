# QwenImageDiffsynthControlnet

QwenImageDiffsynthControlnet 節點會套用擴散合成控制網路修補程式，以修改基礎模型的行為。它使用影像輸入與可選的遮罩，以可調整的強度引導模型的生成過程，建立一個包含控制網路影響的修補模型，以進行更受控制的影像合成。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 要套用控制網路修補程式的基礎模型 | MODEL | 是 | - |
| `model_patch` | 要套用至基礎模型的控制網路修補模型 | MODEL_PATCH | 是 | - |
| `vae` | 擴散過程中使用的 VAE（變分自編碼器） | VAE | 是 | - |
| `image` | 用於引導控制網路的輸入影像（僅使用 RGB 通道） | IMAGE | 是 | - |
| `strength` | 控制網路影響的強度（預設值：1.0） | FLOAT | 是 | -10.0 to 10.0 (step: 0.01) |
| `mask` | 可選遮罩，定義控制網路應套用的區域（內部會進行反向） | MASK | 否 | - |

**注意：** 當提供遮罩時，它會自動反向（1.0 - 遮罩）並重塑為控制網路處理所預期的維度。當模型修補程式為 ZImage Control 類型時，此修補會同時套用至雜訊精修器與雙重區塊；對於標準 DiffSynth 控制網路，僅套用雙重區塊修補。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `model` | 已套用擴散合成控制網路修補程式的修改後模型 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QwenImageDiffsynthControlnet/zh-TW.md)

---
**Source fingerprint (SHA-256):** `56739c098933cb70d3bcb8d6b251da33e7879b464b2e8a7296da085aefc15698`
