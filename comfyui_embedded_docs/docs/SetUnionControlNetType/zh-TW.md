# SetUnionControlNetType

SetUnionControlNetType 節點可讓您選擇控制網路所使用的控制類型。它會取得現有的控制網路，並以所選的控制類型建立修改後的副本，原始控制網路則保持不變。當選取「auto」時，儲存的控制類型會被清除，以便自動偵測類型。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `control_net` | 要使用新類型設定修改的控制網路 | CONTROL_NET | 是 | - |
| `type` | 要套用的控制網路類型。使用「auto」進行自動類型偵測，或從可用選項中選取特定控制網路類型（預設值：「auto」） | COMBO | 是 | `"auto"`<br>`"openpose"`<br>`"depth"`<br>`"hed/pidi/softedge"`<br>`"canny"`<br>`"scribble"`<br>`"seg"`<br>`"tile"`<br>`"inpaint"`<br>`"lineart"`<br>`"blur"`<br>`"mlsd"`<br>`"normalbae"`<br>`"mask"` |

當 `type` 設定為 `"auto"` 時，節點會清除儲存的控制類型，以便自動偵測類型。當選取特定類型時，節點會將相符的控制類型儲存在複製的控制網路中。

## 輸出

| 輸出名 | 描述 | 資料類型 |
| --- | --- | --- |
| `control_net` | 已套用指定類型設定的修改後控制網路 | CONTROL_NET |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SetUnionControlNetType/zh-TW.md)

---
**Source fingerprint (SHA-256):** `db4b1a3cebafcff2be3172faa09cecbd5e19331376491c491cbe359013ed3da3`
