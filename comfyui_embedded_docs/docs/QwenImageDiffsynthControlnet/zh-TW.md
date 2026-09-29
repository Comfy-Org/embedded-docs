# QwenImageDiffsynthControlnet

QwenImageDiffsynthControlnet 會將擴散合成控制網路補丁套用到基礎模型。它使用輸入影像與可選遮罩，以可調整的強度引導模型的生成過程，產生一個已套用補丁的模型，該模型納入控制網路的影響，以實現更可控的影像合成。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 要套用控制網路補丁的基礎模型 | MODEL | 是 | - |
| `model_patch` | 要套用到基礎模型的控制網路補丁模型 | MODEL_PATCH | 是 | - |
| `vae` | 擴散過程中使用的 VAE（變分自編碼器） | VAE | 是 | - |
| `image` | 用於引導控制網路的輸入影像。僅使用前三個顏色通道（RGB）；任何額外通道都會被捨棄 | IMAGE | 是 | - |
| `strength` | 控制網路影響的強度（預設值：1.0） | FLOAT | 是 | -10.0 至 10.0 （步進值：0.01） |
| `mask` | 可選遮罩，用於定義應套用控制網路的區域。對於 DiffSynth 與 Z-Image 補丁，遮罩會在使用前於內部進行反轉 | MASK | 否 | - |
| `start_percent` | 去雜訊過程中，控制網路開始生效的點，以總取樣步數的比例表示（預設值：0.0） | FLOAT | 否 | 0.0 至 1.0 （步進值：0.001） |
| `end_percent` | 去雜訊過程中，控制網路停止生效的點（預設值：1.0） | FLOAT | 否 | 0.0 至 1.0 （步進值：0.001） |

**注意：** `start_percent` 與 `end_percent` 的值會將控制網路限制在去雜訊過程中的某個區間內；在該區間之外，模型會在不套用補丁的情況下進行取樣。若 `strength` 設為 0，節點會回傳未變更的基礎模型。提供遮罩時，對於 Z-Image Control 與標準 DiffSynth 路徑，遮罩會先反轉（1.0 - mask）並重新調整形狀，而 Qwen Image 2.1 Fun ControlNet 補丁則會直接使用給定的遮罩。節點會從載入的模型補丁中選擇其內部補丁實作，因此相同的輸入在 Z-Image Control、Qwen Image 2.1 Fun ControlNet 與標準 DiffSynth 檢查點上的行為會略有不同。此節點標記為實驗性。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `model` | 已套用擴散合成控制網路補丁的修改後模型 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QwenImageDiffsynthControlnet/zh-TW.md)

---
**Source fingerprint (SHA-256):** `7be42c001c2937af7ca5c2d45aa8a529574aa9117b4740c62da822910041d231`
