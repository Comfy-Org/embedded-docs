# Rodin 3D Gen-2.5 - 圖像轉 3D

## 概述

此節點使用 Rodin Gen-2.5 API，從一到五張參考圖像生成 3D 模型。您可以選擇快速、一般或極高品質模式，以平衡生成速度與成本。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `images` | 一到五張輸入圖像。當提供多張圖像時，第一張圖像將用於材質生成。 | IMAGE | 是 | 1 至 5 張圖像 |
| `mode` | 生成品質模式。較高品質模式可產生更佳結果，但成本也更高。 | COMBO | 是 | `"Fast"`<br>`"Regular"`<br>`"Extreme-High"` |
| `material` | 生成 3D 模型的材質類型。 | COMBO | 是 | `"PBR"`<br>`"Matte"` |
| `geometry_file_format` | 3D 模型幾何的輸出檔案格式。 | COMBO | 是 | `"glb"`<br>`"obj"`<br>`"stl"`<br>`"usdz"` |
| `texture_mode` | 紋理生成模式。「Original」保留輸入紋理，「Clean」移除紋理，「Style」則套用風格化紋理。 | COMBO | 是 | `"Original"`<br>`"Clean"`<br>`"Style"` |
| `seed` | 用於可重現結果的隨機種子。使用相同種子可獲得相同輸出。 | INT | 是 | 0 至 2147483647 |
| `TAPose` | 是否對生成的模型套用 T 姿勢。 | BOOLEAN | 是 | True / False |
| `hd_texture` | 是否生成高解析度紋理貼圖。 | BOOLEAN | 是 | True / False |
| `texture_delight` | 是否在紋理生成前移除輸入圖像中的光照。 | BOOLEAN | 是 | True / False |
| `use_original_alpha` | 是否使用輸入圖像的原始 Alpha 通道。 | BOOLEAN | 是 | True / False |
| `addon_highpack` | 是否在標準模型之外，額外生成高多邊形版本的模型。 | BOOLEAN | 是 | True / False |
| `bbox_width` | 生成模型邊界框的寬度（單位：公分）。 | INT | 是 | 1 至 1000 |
| `bbox_height` | 生成模型邊界框的高度（單位：公分）。 | INT | 是 | 1 至 1000 |
| `bbox_length` | 生成模型邊界框的長度（單位：公分）。 | INT | 是 | 1 至 1000 |
| `height_cm` | 生成模型的高度（單位：公分）。 | INT | 是 | 1 至 300 |

**關於圖像數量的說明：** 此節點接受 1 到 5 張圖像。如果您提供一批圖像（例如 4 張圖像的批次），批次中的每張圖像都會被視為單獨的輸入圖像。提供超過 5 張圖像將會導致錯誤。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `model_file` | 以所選幾何格式生成的 3D 模型檔案。 | FILE3D |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Rodin3D_Gen25_Image/zh-TW.md)

---
**Source fingerprint (SHA-256):** `65f755a2c3bd2317eb61c4681a406b51b06f960e36864d3602c3d03a44aa4878`
