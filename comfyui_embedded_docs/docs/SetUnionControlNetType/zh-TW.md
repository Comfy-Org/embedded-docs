## 概述

SetUnionControlNetType 節點允許您指定要用於條件控制的網路類型。它會接收現有的控制網路，並根據您的選擇設定其控制類型，從而建立一個具有指定類型配置的修改版控制網路副本。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `control_net` | 要修改並套用新類型設定的控制網路 | CONTROL_NET | 是 | - |
| `type` | 要套用的控制網路類型。使用 "auto" 進行自動類型偵測，或從可用選項中選擇特定的控制網路類型 | STRING | 是 | `"auto"`<br>所有可用的 UNION_CONTROLNET_TYPES 鍵 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `control_net` | 已套用指定類型設定的修改版控制網路 | CONTROL_NET |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SetUnionControlNetType/zh-TW.md)

---
**Source fingerprint (SHA-256):** `a64308aec96784f08b6f3f8e96e85f532bd1c536301739e7252b2c7978921b5a`
