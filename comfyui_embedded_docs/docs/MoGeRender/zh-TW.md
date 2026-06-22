# MoGe 渲染

## 概述

此節點接收一個 MOGE_GEOMETRY 資料包（由 MoGe 深度/法線估算節點產生），並將其渲染為標準影像格式。您可以選擇輸出深度圖、彩色深度圖、法線圖或遮罩。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `moge_geometry` | 來自 MoGe 估算節點的幾何資料包。 | MOGE_GEOMETRY | 是 | 不適用 |
| `output` | 要從幾何資料渲染的影像類型。DirectX 與 OpenGL 控制法線貼圖的綠色通道慣例。DirectX：綠色 = -Y 向下（Unreal）。OpenGL：綠色 = +Y 向上（Blender、Substance、Unity、glTF）。（預設值："depth"） | COMBO | 是 | `"depth"`<br>`"depth_colored"`<br>`"normal_opengl"`<br>`"normal_directx"`<br>`"mask"` |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `IMAGE` | 渲染後的影像，以 RGB 張量批次形式呈現。內容取決於 `output` 模式：灰階深度圖、彩色深度圖、法線圖或遮罩。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGeRender/zh-TW.md)

---
**Source fingerprint (SHA-256):** `45ba499e746ce46f9b6f7773e3218bcf80ad2e8d65940b38e248cc2f20c8b2fe`
