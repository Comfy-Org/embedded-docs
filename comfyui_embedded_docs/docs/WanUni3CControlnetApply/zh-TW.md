# 套用 Wan Uni3C ControlNet

## 概述

此節點將 Uni3C ControlNet 應用於 Wan 影片擴散模型，利用渲染的引導影片（例如扭曲點雲渲染）來影響模型的輸出。它將控制訊號注入特定區塊層，從而在影片生成過程中實現基於相機軌跡的引導。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|------|------|----------|------|------|
| `模型` | 要修補的 Wan 擴散模型。 | MODEL | 是 | – |
| `模型補丁` | Uni3C ControlNet 修補（必須為 `comfy.ldm.wan.uni3c.WanUni3CControlnet` 的實例）。 | MODEL_PATCH | 是 | – |
| `vae` | 用於將引導影片編碼為潛在向量的 VAE。 | VAE | 是 | – |
| `渲染影片` | 從相機軌跡渲染的引導影片，最常見的是輸入影像的扭曲點雲渲染。 | IMAGE | 是 | – |
| `強度` | 所施加控制訊號的強度。 | FLOAT | 是 | -10.0 至 10.0（預設：1.0） |
| `起始百分比` | 控制開始時的去噪過程百分比。 | FLOAT | 是 | 0.0 至 1.0（預設：0.0） |
| `結束百分比` | 控制結束時的去噪過程百分比。 | FLOAT | 是 | 0.0 至 1.0（預設：1.0） |

**注意事項：**
- `model_patch` 必須是 Uni3C ControlNet，否則節點將引發錯誤。
- controlnet 的內部維度必須與 Wan 模型的維度相匹配——若兩者不同，則會引發錯誤。
- `render_video` 輸入影像應為 RGB 格式（僅使用前 3 個通道）。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|----------|------|----------|
| `MODEL` | 已套用 Uni3C ControlNet 的修補後 Wan 模型。 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanUni3CControlnetApply/zh-TW.md)

---
**Source fingerprint (SHA-256):** `f69253f06aba9208778f713ad36e9995f53a15d2e61243b853b9ac9131637371`
