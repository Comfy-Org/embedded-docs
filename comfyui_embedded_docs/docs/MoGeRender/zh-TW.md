# MoGe 渲染

此節點接收由 MoGe 深度/法線估計節點產生的 MOGE_GEOMETRY 封包，並將其渲染為標準影像格式。你可以選擇輸出深度圖、彩色深度圖、法線圖或遮罩。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `moge_geometry` | 來自 MoGe 估計節點的幾何資料封包。 | MOGE_GEOMETRY | 是 | N/A |
| `output` | 要從幾何資料渲染出的影像類型。`depth` 輸出灰階深度圖，`depth_colored` 輸出彩色深度圖，`normal_opengl` 和 `normal_directx` 輸出法線圖，`mask` 輸出遮罩。DirectX 與 OpenGL 控制法線圖的綠色通道慣例。DirectX：green = -Y down（Unreal）。OpenGL：green = +Y up（Blender、Substance、Unity、glTF）。（預設值："depth"） | COMBO | 是 | `"depth"`<br>`"depth_colored"`<br>`"normal_opengl"`<br>`"normal_directx"`<br>`"mask"` |

**注意：** 幾何封包必須包含與所選 `output` 模式相符的資料。`depth` 和 `depth_colored` 模式需要封包中的深度資料。`normal_opengl` 和 `normal_directx` 模式需要法線資料，或可從中推導法線的點資料。`mask` 模式需要遮罩資料。如果缺少必要資料，節點會引發錯誤。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `IMAGE` | 渲染後的影像，以一批 RGB 張量表示。內容取決於 `output` 模式：灰階深度圖、彩色深度圖、法線圖，或轉換為 RGB 的遮罩。輸出批次大小與輸入幾何批次大小相符。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGeRender/zh-TW.md)

---
**Source fingerprint (SHA-256):** `ca602f7a7d6eb1b1d00986459621d94ecf9331266ff1d3ce7bb759d24448a346`
