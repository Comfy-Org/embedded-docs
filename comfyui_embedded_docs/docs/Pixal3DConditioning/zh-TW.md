# Pixal3DConditioning

Pixal3DConditioning 節點會為 Trellis2 3D 生成流程準備影像條件。它使用 DINOv3 視覺模型，從輸入影像中以兩種解析度（512 和 1024）擷取視覺特徵，然後將其組織成逐階段特徵圖，這些特徵圖可選擇性地由 NAF 模型增強。相機資訊會從水平視野推導而來，以建立投影變換矩陣，而節點會輸出正向條件對（影像衍生特徵加上投影資料）與負向條件對（歸零的特徵張量），用於無分類器引導。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `clip_vision_model` | DINOv3 ViT-L/16 ClipVision。 | CLIP_VISION | 是 | — |
| `圖像` | 來自 ImageCropToMask 的預處理影像（Pixal3D 的 pad_factor=1.1）。 | IMAGE | 是 | — |
| `camera_angle_x` | 水平 FOV，單位為度（顯示為 `fov`）。連接 MoGeGeometryToFOV（axis='horizontal', unit='degrees'）以取得每張影像的 FoV（符合上游預設）。預設值：49.13。 | FLOAT | 是 | 1.0 – 170.0 （步進值：0.01） |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `positive` | 正向條件輸出，包含用於 Trellis2 生成的影像衍生特徵圖與投影資料。 | CONDITIONING |
| `negative` | 負向條件輸出，具有歸零的特徵張量，用於無分類器引導。 | CONDITIONING |

注意：`camera_angle_x` 值會在內部從度轉換為弧度，並根據它計算相機距離，以建立投影變換矩陣。當提供的視覺模型包含 NAF 元件時，節點也會為形狀與紋理階段產生高解析度特徵圖。

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Pixal3DConditioning/zh-TW.md)

---
**Source fingerprint (SHA-256):** `88e82b48fbe297c8e32ddd1b6659f196bda6f77fd53480bc021e85170d1923c7`
