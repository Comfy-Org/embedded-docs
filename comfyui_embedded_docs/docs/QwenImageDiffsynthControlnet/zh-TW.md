> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QwenImageDiffsynthControlnet/zh-TW.md)

# QwenImageDiffsynthControlnet 節點

QwenImageDiffsynthControlnet 節點應用擴散合成控制網路修補程式來修改基礎模型的行為。它使用影像輸入和可選遮罩，以可調整的強度引導模型的生成過程，建立一個整合控制網路影響的修補模型，以實現更受控制的影像合成。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | 是 | - | 要套用控制網路修補的基礎模型 |
| `model_patch` | MODEL_PATCH | 是 | - | 要套用到基礎模型的控制網路修補模型 |
| `vae` | VAE | 是 | - | 擴散過程中使用的 VAE（變分自編碼器） |
| `image` | IMAGE | 是 | - | 用於引導控制網路的輸入影像（僅使用 RGB 通道） |
| `strength` | FLOAT | 是 | -10.0 至 10.0 | 控制網路影響的強度（預設值：1.0） |
| `mask` | MASK | 否 | - | 可選遮罩，定義控制網路應套用的區域（內部會反轉處理） |

**注意：** 當提供遮罩時，它會自動反轉（1.0 - 遮罩）並重新調整形狀，以符合控制網路處理所需的預期維度。此節點會根據模型修補是 ZImage Control 類型還是標準 DiffSynth 控制網路，使用不同的內部處理方法。

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `model` | MODEL | 已套用擴散合成控制網路修補的修改後模型 |

---
**Source fingerprint (SHA-256):** `61833984d0b92be65fae72a894806572c0588dea74a295e8289d1194dee611bb`
