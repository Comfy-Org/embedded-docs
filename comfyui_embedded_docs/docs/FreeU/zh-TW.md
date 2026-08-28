# FreeU

FreeU 節點會對模型的輸出區塊套用頻域修改，以提升影像生成品質。其運作方式是縮放不同的通道群組，並對特定的特徵圖套用傅立葉濾波，讓您在生成過程中能夠精細控制模型的行為。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 要套用 FreeU 修改的模型 | MODEL | 是 | - |
| `b1` | model_channels × 4 特徵的主幹縮放因子（預設值：1.1） | FLOAT | 是 | 0.0 - 10.0 |
| `b2` | model_channels × 2 特徵的主幹縮放因子（預設值：1.2） | FLOAT | 是 | 0.0 - 10.0 |
| `s1` | model_channels × 4 特徵的跳躍連接縮放因子（預設值：0.9） | FLOAT | 是 | 0.0 - 10.0 |
| `s2` | model_channels × 2 特徵的跳躍連接縮放因子（預設值：0.2） | FLOAT | 是 | 0.0 - 10.0 |

注意：FreeU 調整僅套用於通道數等於 model_channels × 4（使用 `b1` 和 `s1`）或 model_channels × 2（使用 `b2` 和 `s2`）的特徵圖。傅立葉濾波僅縮放跳躍連接特徵圖的中央低頻區域；所有其他頻率分量保持不變。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `model` | 已套用 FreeU 修補程式的修改後模型 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FreeU/zh-TW.md)

---
**Source fingerprint (SHA-256):** `7f7bd34964218ed16c9e58caa446d0c1e69f116607334df4a114cdc4adaf047f`
