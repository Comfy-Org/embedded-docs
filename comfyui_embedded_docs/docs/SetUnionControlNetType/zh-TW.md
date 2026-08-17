# SetUnionControlNetType

SetUnionControlNetType 節點可讓您設定用於條件化（conditioning）的控制網路控制類型。它會取得現有的控制網路，建立一個修改後的副本，並將所選的控制類型儲存在該副本中，使原始控制網路保持不變。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `control_net` | 要複製並以所選控制類型修改的控制網路 | CONTROL_NET | 是 | - |
| `type` | 要套用於複製後控制網路的控制類型。選擇 "auto" 以不設定控制類型，或從可用的聯合控制網路類型中選擇特定類型（預設值為 "auto"） | COMBO | 是 | `"auto"`<br>`"openpose"`<br>`"depth"`<br>`"hed/pidi/scribble/ted"`<br>`"canny/softedge"`<br>`"normal/bms"`<br>`"seg"`<br>`"inpaint"`<br>`"lineart"`<br>`"s4"`<br>`"tile/color"`<br>`"blur"`<br>`"identity"` |

注意：當 `type` 為 "auto" 時，複製後控制網路上的控制類型清單會被清除。當選擇特定類型時，複製後的控制網路會儲存對應的類型編號。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `control_net` | 已套用所選控制類型的控制網路修改副本 | CONTROL_NET |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SetUnionControlNetType/zh-TW.md)

---
**Source fingerprint (SHA-256):** `db4b1a3cebafcff2be3172faa09cecbd5e19331376491c491cbe359013ed3da3`
