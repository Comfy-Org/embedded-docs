# Pixal3DConditioning

此節點為 Trellis2 3D 生成流程準備影像條件。它使用 DINOv3 視覺模型以兩種解析度從輸入影像中提取視覺特徵，將它們組織成每個階段的特徵圖（可選地用 NAF 模型增強），並將它們與從水平視野推導出的相機資料結合。它輸出一對正向與負向的條件，其中負向使用零化特徵進行無分類器引導。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `clip_vision_model` | DINOv3 ViT-L/16 ClipVision 模型。 | CLIP_VISION | 是 | — |
| `image` | 來自 ImageCropToMask 的預處理影像（Pixal3D 的 pad_factor=1.1）。 | IMAGE | 是 | — |
| `camera_angle_x` | 水平視野（以度為單位）（顯示名稱：fov）。連接 MoGeGeometryToFOV（axis='horizontal'，unit='degrees'）以獲得每個影像的 FoV（與上游預設值一致）。預設值：49.13。 | FLOAT | 是 | 1.0 – 170.0 |

注意：`camera_angle_x` 值在內部會轉換為弧度，並用於計算投影變換矩陣的相機距離。當提供的視覺模型包含 NAF 元件時，節點會額外為形狀與紋理階段產生高解析度特徵圖。

## 輸出

| 輸出名 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `positive` | 包含影像衍生特徵圖與投影資料的正向條件，用於 Trellis2 生成。 | CONDITIONING |
| `negative` | 具有零化特徵張量的負向條件，用於無分類器引導。 | CONDITIONING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Pixal3DConditioning/zh-TW.md)

---
**Source fingerprint (SHA-256):** `3eba711620f6c56a21bbf7df89f8d406ce6f90908298b1a295a1dbbddd042472`
