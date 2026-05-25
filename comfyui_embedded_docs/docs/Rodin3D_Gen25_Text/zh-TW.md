> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Rodin3D_Gen25_Text/zh-TW.md)

## 概述

使用 Rodin Gen-2.5 API 從文字提示生成 3D 模型。您可以選擇不同的品質模式（快速、一般或極高），以平衡生成速度和輸出品質。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | 是 | 最多 2500 個字元 | 描述您想要生成的 3D 模型的文字提示。 |
| `mode` | COMBO | 是 | `"Fast"`<br>`"Regular"`<br>`"Extreme-High"` | 生成品質與速度模式。「Fast」最快，「Extreme-High」品質最高但耗時較長。 |
| `material` | COMBO | 是 | `"PBR"`<br>`"Matte"`<br>`"Shiny"` | 生成的 3D 模型的材質風格。 |
| `geometry_file_format` | COMBO | 是 | `"glb"`<br>`"obj"`<br>`"stl"`<br>`"usdz"` | 輸出 3D 模型的檔案格式。 |
| `texture_mode` | COMBO | 是 | `"None"`<br>`"Generated"`<br>`"Generated+HD"` | 紋理生成模式。「None」不產生紋理，「Generated」建立標準紋理，「Generated+HD」建立高畫質紋理。 |
| `seed` | INT | 是 | 0 到 2147483647 | 用於可重現結果的隨機種子。使用相同的種子和輸入將產生相同的輸出。 |
| `TAPose` | BOOLEAN | 是 | True / False | 是否對生成的模型套用 T 姿勢（雙臂伸展）。 |
| `hd_texture` | BOOLEAN | 是 | True / False | 是否為模型生成高畫質紋理。 |
| `texture_delight` | BOOLEAN | 是 | True / False | 是否對模型套用紋理增強（提升紋理品質）。 |
| `addon_highpack` | BOOLEAN | 是 | True / False | 是否在標準模型之外，額外生成高多邊形版本的模型。 |
| `bbox_width` | INT | 是 | 1 到 1000 | 邊界框的寬度（以世界單位計）。 |
| `bbox_height` | INT | 是 | 1 到 1000 | 邊界框的高度（以世界單位計）。 |
| `bbox_length` | INT | 是 | 1 到 1000 | 邊界框的長度（以世界單位計）。 |
| `height_cm` | INT | 是 | 1 到 300 | 生成的模型高度（以公分計）。 |

**注意：** `prompt` 參數長度必須介於 1 到 2500 個字元之間。若未指定，`seed` 參數預設為 0（隨機）。

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `model_file` | FILE3DANY | 以指定格式生成的 3D 模型檔案。 |

---
**Source fingerprint (SHA-256):** `79fbaf466e9af88cdfdac0f9136a2df17ba4bc2e5bb65a35b9ad2b1181da94db`
