# MoGe 渲染

此節點接收一個 MOGE_GEOMETRY 資料包（由 MoGe 深度/法線估計節點產生），並將其渲染為標準影像格式。您可以選擇輸出深度圖、彩色深度圖、法線圖或遮罩。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `moge_geometry` | 來自 MoGe 估計節點的幾何資料包。 | MOGE_GEOMETRY | 是 | N/A |
| `output` | 要從幾何資料渲染的影像類型。DirectX 與 OpenGL 控制法線圖的綠色通道慣例。DirectX：綠色 = -Y 向下（Unreal）。OpenGL：綠色 = +Y 向上（Blender、Substance、Unity、glTF）。（預設值："depth"） | COMBO | 是 | `"depth"`<br>`"depth_colored"`<br>`"normal_opengl"`<br>`"normal_directx"`<br>`"mask"` |

**注意：** 選取的 `output` 模式決定 `moge_geometry` 中必須存在的資料：
- `depth` 和 `depth_colored` 需要深度資料。深度會使用 0.1/99.9 百分位裁剪轉換為歸一化的視差（1/depth）圖。
- `normal_opengl` 和 `normal_directx` 需要法線資料，或可從中推導出法線的點資料。若兩者皆不存在，節點會引發錯誤。
- `mask` 需要遮罩資料。

## 輸出

| 輸出名 | 描述 | 資料類型 |
| --- | --- | --- |
| `IMAGE` | 渲染後的影像，作為一批 RGB 張量。內容取決於 `output` 模式：灰階深度圖、彩色深度圖、法線圖或遮罩。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGeRender/zh-TW.md)

---
**Source fingerprint (SHA-256):** `ca602f7a7d6eb1b1d00986459621d94ecf9331266ff1d3ce7bb759d24448a346`
