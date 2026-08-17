# FreeU_V2

FreeU_V2 節點透過對擴散模型的 U-Net 架構應用基於頻率的修改來增強圖像生成品質。它使用可配置的縮放因子來調整不同區塊中的特徵通道，無需額外訓練即可改善輸出。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 要應用 FreeU 增強的擴散模型 | MODEL | 是 | - |
| `b1` | 第一個區塊的骨幹特徵縮放因子（預設值：1.3） | FLOAT | 是 | 0.0 - 10.0 |
| `b2` | 第二個區塊的骨幹特徵縮放因子（預設值：1.4） | FLOAT | 是 | 0.0 - 10.0 |
| `s1` | 第一個區塊的跳躍特徵縮放因子（預設值：0.9） | FLOAT | 是 | 0.0 - 10.0 |
| `s2` | 第二個區塊的跳躍特徵縮放因子（預設值：0.2） | FLOAT | 是 | 0.0 - 10.0 |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `model` | 已應用 FreeU 修改的增強擴散模型 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FreeU_V2/zh-TW.md)

---
**Source fingerprint (SHA-256):** `4cef2af9b04164a8ead25bea9c9bb3311be9224f2539a5cc6edbe97ad8465d65`
