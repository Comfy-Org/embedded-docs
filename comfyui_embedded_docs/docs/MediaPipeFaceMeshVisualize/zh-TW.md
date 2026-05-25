> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MediaPipeFaceMeshVisualize/zh-TW.md)

## 概述

在輸入影像上繪製臉部特徵點和連接線（臉部網格）。此節點使用臉部偵測節點產生的特徵點資料，將偵測到的臉部特徵（如眼睛、鼻子、嘴巴和臉部輪廓）視覺化。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `face_landmarks` | FACE_LANDMARKS | 是 | | 來自偵測節點的臉部特徵點資料。 |
| `image` | IMAGE | 否 | | 要在其上繪製網格的影像。若未連接，將使用與偵測結果相同尺寸的黑色畫布。 |
| `connections` | COMBO | 是 | `"all"`<br>`"fill"`<br>`"custom"` | 決定要繪製臉部網格的哪些部分。`"all"` 繪製完整網格（橢圓、眼睛、眉毛、嘴唇、虹膜、鼻子）。`"fill"` 繪製臉部橢圓的實心多邊形（剪影遮罩）。`"custom"` 可讓您個別切換每個特徵。（預設值：`"all"`） |
| `color` | COLOR | 是 | | 網格線條和點的顏色。（預設值：`#00ff00`） |
| `thickness` | INT | 是 | 0 至 8 | 網格線條的像素粗細。設為 0 可停用線條繪製。（預設值：1） |
| `point_size` | INT | 是 | 0 至 16 | 特徵點圓點的像素半徑。設為 0 可停用圓點繪製。（預設值：2） |

**關於 `connections` 參數的說明：** 當選擇 `"custom"` 時，每個臉部特徵會出現額外的布林輸入（例如 `face_oval`、`lips`、`left_eye`、`right_eye`、`left_eyebrow`、`right_eyebrow`、`left_iris`、`right_iris`、`nose`、`tesselation`）。僅會繪製您啟用的特徵。

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `IMAGE` | IMAGE | 已繪製臉部特徵點網格的輸入影像。 |

---
**Source fingerprint (SHA-256):** `fb5437d73378b0c8daa68669c2e19058ccb7133ed68fc51c8d4c5bab8662f243`
