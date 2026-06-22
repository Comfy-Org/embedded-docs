# MultiGPU_Options

## 概述

此節點可讓您在同時使用多張速度不同的顯示卡時，指定每張 GPU 的相對效能。它會建立一組 GPU 選項，可用於跨裝置分配工作負載，不過在目前版本中，基於速度的工作負載分配功能尚未實作。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `device_index` | 要設定的 GPU 裝置索引編號（預設值：0） | INT | 是 | 0 至 64 |
| `relative_speed` | 此 GPU 相對於其他 GPU 的相對速度，用於工作負載分配（預設值：1.0，步進值：0.01） | FLOAT | 是 | 0.0 至無上限 |
| `gpu_options` | 要加入此裝置選項的現有 GPU 選項群組。若未提供，則會建立新的群組 | GPU_OPTIONS | 否 | - |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `GPU_OPTIONS` | 包含已設定裝置設定的 GPU 選項群組，可傳遞給其他節點進行多 GPU 操作 | GPU_OPTIONS |

**注意：** `relative_speed` 參數已定義，但內部排程器尚未使用它來跨 GPU 分配工作負載。在目前的實作中，無論各裝置的相對速度為何，工作負載都會均勻分配給所有裝置。

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MultiGPU_Options/zh-TW.md)

---
**Source fingerprint (SHA-256):** `8010460560a69c57d4ee0d8c3728a7a5d999e56ef5316b557fba0c660c9f38b0`
