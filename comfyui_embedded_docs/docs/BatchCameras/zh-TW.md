# Batch Cameras

將相機與相機軌道依輸入順序合併為一個相機清單。Render Mesh 與 Render Splat 會為清單中的每台相機各渲染一張影像，多視圖渲染即以此方式建構。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `cameras` | 可增長的相機插槽，來源為 Create Camera Info、Create Camera Orbit 或檢視器。一個相機清單會計入其中的每一台相機。 | AUTOGROW | 是 | 1 至 50 台相機 |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `camera_info` | 一個相機清單，依輸入順序包含所有輸入相機。 | LOAD3D_CAMERA |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BatchCameras/zh-TW.md)

---
**Source fingerprint (SHA-256):** `a5ddae7f539a2d70efc1b156f7b4ec4b219d7cf78544b882f7b8f9538ae9a88d`
