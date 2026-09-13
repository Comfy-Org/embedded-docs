# FreeU

The FreeU 節點會對模型的輸出塊套用頻域修改，以提升圖像生成品質。它透過縮放不同的通道組，並對特定特徵圖套用傅立葉濾波來運作，讓您能在生成過程中對模型行為進行精細控制。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 要套用 FreeU 修改的模型 | MODEL | 是 | - |
| `b1` | 套用於具有 model_channels × 4 通道之特徵圖的主幹縮放因子（預設：1.1）。標記為進階設定。 | FLOAT | 是 | 0.0 - 10.0 |
| `b2` | 套用於具有 model_channels × 2 通道之特徵圖的主幹縮放因子（預設：1.2）。標記為進階設定。 | FLOAT | 是 | 0.0 - 10.0 |
| `s1` | 套用於具有 model_channels × 4 通道之特徵圖的跳躍連接縮放因子（預設：0.9）。標記為進階設定。 | FLOAT | 是 | 0.0 - 10.0 |
| `s2` | 套用於具有 model_channels × 2 通道之特徵圖的跳躍連接縮放因子（預設：0.2）。標記為進階設定。 | FLOAT | 是 | 0.0 - 10.0 |

注意：FreeU 調整僅會套用於通道數等於 model_channels × 4（使用 `b1` 和 `s1`）或 model_channels × 2（使用 `b2` 和 `s2`）的特徵圖。傅立葉濾波器僅會縮放跳躍連接特徵圖的中央低頻區域（閾值為 1）；所有其他頻率成分保持不變。全部四個縮放參數都接受 0.0 到 10.0 之間、步長為 0.01 的值。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `model` | 已套用 FreeU 補丁的修改後模型 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FreeU/zh-TW.md)

---
**Source fingerprint (SHA-256):** `7f7bd34964218ed16c9e58caa446d0c1e69f116607334df4a114cdc4adaf047f`
