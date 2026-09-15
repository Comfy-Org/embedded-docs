# EasyCache

EasyCache 節點會為擴散模型加入原生快取系統，透過重複使用先前已計算步驟的結果，而非每一步都重新計算，來加速取樣。它僅會在取樣流程中可設定的起點與終點之間啟用，並在預估的輸出變化低於使用者定義的閾值時略過步驟。這是實驗性節點，適用於進階除錯用途。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `模型` | 要加入 EasyCache 的模型。 | MODEL | 是 | - |
| `重用閾值` | 重複使用快取步驟的閾值（預設值：0.2）。 | FLOAT | 是 | 0.0 - 3.0 |
| `起始百分比` | 開始使用 EasyCache 的相對取樣步驟（預設值：0.15）。 | FLOAT | 是 | 0.0 - 1.0 |
| `結束百分比` | 結束使用 EasyCache 的相對取樣步驟（預設值：0.95）。 | FLOAT | 是 | 0.0 - 1.0 |
| `詳細模式` | 是否記錄詳細資訊（預設值：False）。 | BOOLEAN | 是 | - |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `model` | 已加入 EasyCache 功能的模型。 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EasyCache/zh-TW.md)

---
**Source fingerprint (SHA-256):** `3e10ac65f8df58ce8649fdf599e62bfb86f2d4166840bed5622c0aa2c419cd38`
