# Create Camera Orbit

圍繞第一個相機的目標建立一組相機裝置：預設為轉台，設定 `pitch` 時為傾斜掃掠，並可選擇正下方與正上方的視角。Render Mesh 會為每台相機渲染一張影像，Bake Texture From Views 則會將這些影像投影回網格上。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `camera_info` | 軌道的第一台相機。相機清單會繞行清單中的每一台相機。 | LOAD3D_CAMERA | 是 | - |
| `count` | 沿著掃掠均勻間隔排列的相機數量。預設：4。 | INT | 是 | 1 至 64 |
| `yaw` | 繞目標的總轉角，以 Create Camera Info 的 yaw 方向為準。整圈旋轉會停在第一台相機前一步；其他掃掠則結束於最後一台相機。預設：360.0。 | FLOAT | 是 | -720.0 至 720.0（步進值：1.0） |
| `pitch` | 相對於目標的總傾斜角度，正值上升方向與 Create Camera Info 的 pitch 相同；超過 90 時，相機會越過頂部。整圈旋轉會像 `yaw` 一樣循環。預設：0.0。 | FLOAT | 是 | -720.0 至 720.0（步進值：1.0） |
| `poles` | 從目標正下方及／或正上方觀看的視角，會加在軌道之後。其影像頂端會背離第一台相機。預設：`"none"`。 | COMBO | 是 | `"none"`<br>`"top"`<br>`"bottom"`<br>`"top and bottom"` |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `camera_info` | 此相機裝置的相機清單，順序為軌道順序，之後接續極點視角。 | LOAD3D_CAMERA |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateCameraOrbit/zh-TW.md)

---
**Source fingerprint (SHA-256):** `b251efc969f8db7cf03527594be3bbd2af037f1ebb56bdf508bf264ddd9f8c08`
