## 概述

此節點使用騰訊 Hunyuan3D API 對 3D 模型執行 UV 展開。它接收一個 3D 模型檔案作為輸入，將其發送到 API 進行處理，並以 OBJ 和 FBX 格式返回處理後的模型，同時生成 UV 紋理影像。輸入模型的面數必須少於 30,000 個。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `3D 模型` | 輸入的 3D 模型（GLB、OBJ 或 FBX 格式）。模型面數必須少於 30,000 個。 | FILE3D | 是 | GLB<br>OBJ<br>FBX |
| `種子` | 種子值（預設值：1）。此參數控制節點是否應重新執行，但無論種子值為何，結果皆為非確定性。 | INT | 否 | 0 到 2147483647 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `FBX` | 以 OBJ 格式處理後的 3D 模型檔案。 | FILE3D |
| `uv_image` | 以 FBX 格式處理後的 3D 模型檔案。 | FILE3D |
| `uv_image` | 生成的 UV 紋理影像。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TencentModelTo3DUVNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `16bf094cfc3146e9d302d73862d2080b94c5aa2d575221d3c8316a3cf69fc5e1`
