# Rodin 3D Gen-2.5 - 文字轉3D

## 概述

使用 Rodin Gen-2.5 API 從文字提示生成 3D 模型。您可以選擇不同的品質模式（Fast、Regular 或 Extreme-High），以平衡生成速度與輸出品質。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `提示詞` | 用於 3D 模型的文字提示。 | STRING | 是 | 1 至 1024 個字元 |
| `模式` | 生成品質與速度模式。「Fast」最快，「Extreme-High」可產生最高品質，但耗時較長。 | COMBO | 是 | `"Fast"`<br>`"Regular"`<br>`"Extreme-High"` |
| `材質` | 所生成 3D 模型的材質風格。 | COMBO | 是 | `"PBR"`<br>`"Matte"`<br>`"Shiny"` |
| `幾何檔案格式` | 輸出 3D 模型的檔案格式。 | COMBO | 是 | `"glb"`<br>`"obj"`<br>`"stl"`<br>`"usdz"` |
| `材質品質` | 紋理生成模式。「None」不產生紋理，「Generated」建立標準紋理，「Generated+HD」建立高解析度紋理。 | COMBO | 是 | `"None"`<br>`"Generated"`<br>`"Generated+HD"` |
| `隨機種子` | 用於可重現結果的隨機種子。搭配相同輸入使用相同種子時，會產生相同輸出。 | INT | 是 | 0 至 2147483647 |
| `T/A 姿勢` | 是否對生成的模型套用 T-pose（手臂伸展）。 | BOOLEAN | 是 | True 或 False |
| `高畫質材質` | 是否為模型生成高解析度紋理。 | BOOLEAN | 是 | True 或 False |
| `材質去光照` | 是否對模型套用 texture delight（增強紋理品質）。 | BOOLEAN | 是 | True 或 False |
| `HighPack 附加包` | 是否除了標準版本外，另生成模型的高多邊形版本。 | BOOLEAN | 是 | True 或 False |
| `包圍盒寬度` | 邊界框的寬度，以世界單位為單位。 | INT | 是 | 1 至 1000 |
| `包圍盒高度` | 邊界框的高度，以世界單位為單位。 | INT | 是 | 1 至 1000 |
| `包圍盒長度` | 邊界框的長度，以世界單位為單位。 | INT | 是 | 1 至 1000 |
| `模型高度（公分）` | 所生成模型的高度，以公分為單位。 | INT | 是 | 1 至 300 |

**注意：** `prompt` 參數長度必須介於 1 到 1024 個字元之間。若未指定，`seed` 參數預設為 0（隨機）。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `模型檔案` | 以指定格式生成的 3D 模型檔案。 | FILE3DANY |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Rodin3D_Gen25_Text/zh-TW.md)

---
**Source fingerprint (SHA-256):** `95d5faa36298f09f0ae4dcda95dfd8913ebb393bb5934ae2c4622acfe79c85d6`
