# FreeU

FreeU 節點對模型的輸出區塊套用頻域修改，以提升影像生成品質。其運作方式是對不同的通道群組進行縮放，並對特定特徵圖套用傅立葉濾波，從而在生成過程中對模型行為進行精細控制。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 要套用 FreeU 修改的模型 | MODEL | 是 | - |
| `b1` | 適用於 model_channels × 4 特徵的骨幹縮放因子（預設值：1.1） | FLOAT | 是 | 0.0 - 10.0 |
| `b2` | 適用於 model_channels × 2 特徵的骨幹縮放因子（預設值：1.2） | FLOAT | 是 | 0.0 - 10.0 |
| `s1` | 適用於 model_channels × 4 特徵的跳躍連接縮放因子（預設值：0.9） | FLOAT | 是 | 0.0 - 10.0 |
| `s2` | 適用於 model_channels × 2 特徵的跳躍連接縮放因子（預設值：0.2） | FLOAT | 是 | 0.0 - 10.0 |

注意：修改僅套用於具有 model_channels × 4 和 model_channels × 2 通道的特徵圖；`b1`/`s1` 影響前者，`b2`/`s2` 影響後者。其他特徵圖保持不變。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `model` | 已套用 FreeU 補丁的修改後模型 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FreeU/zh-TW.md)

---
**Source fingerprint (SHA-256):** `7f7bd34964218ed16c9e58caa446d0c1e69f116607334df4a114cdc4adaf047f`
