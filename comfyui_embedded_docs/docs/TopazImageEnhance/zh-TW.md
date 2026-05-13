> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TopazImageEnhance/zh-TW.md)

Topaz 影像增強節點提供業界標準的放大與影像增強功能。它使用雲端 AI 模型處理單一輸入影像，以改善品質、細節與解析度。此節點提供對增強過程的精細控制，包括創意引導、主體對焦與臉部保留等選項。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | 是 | `"Reimagine"` | 用於影像增強的 AI 模型。 |
| `image` | IMAGE | 是 | - | 要增強的輸入影像。僅支援單一影像。 |
| `prompt` | STRING | 否 | - | 用於創意放大引導的選用文字提示（預設為空）。 |
| `subject_detection` | COMBO | 否 | `"All"`<br>`"Foreground"`<br>`"Background"` | 控制增強過程聚焦於影像的哪個部分（預設為 "All"）。 |
| `face_enhancement` | BOOLEAN | 否 | - | 啟用以增強影像中存在的臉部（預設為 True）。 |
| `face_enhancement_creativity` | FLOAT | 否 | 0.0 - 1.0 | 設定臉部增強的創意程度（預設為 0.0）。 |
| `face_enhancement_strength` | FLOAT | 否 | 0.0 - 1.0 | 控制增強後臉部相對於背景的銳利程度（預設為 1.0）。 |
| `crop_to_fill` | BOOLEAN | 否 | - | 預設情況下，當輸出寬高比不同時，影像會以信箱模式顯示。啟用此選項則會裁切影像以填滿輸出尺寸（預設為 False）。 |
| `output_width` | INT | 否 | 0 - 32000 | 輸出影像的期望寬度。值為 0 表示將自動計算，通常基於原始尺寸或指定的 `output_height`（預設為 0）。 |
| `output_height` | INT | 否 | 0 - 32000 | 輸出影像的期望高度。值為 0 表示將自動計算，通常基於原始尺寸或指定的 `output_width`（預設為 0）。 |
| `creativity` | INT | 否 | 1 - 9 | 控制增強的整體創意程度（預設為 3）。 |
| `face_preservation` | BOOLEAN | 否 | - | 保留影像中主體的面部特徵（預設為 True）。 |
| `color_preservation` | BOOLEAN | 否 | - | 保留輸入影像的原始色彩（預設為 True）。 |

**注意：** 此節點僅能處理單一輸入影像。提供多張影像的批次將導致錯誤。

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `image` | IMAGE | 增強後的輸出影像。 |

---
**Source fingerprint (SHA-256):** `69f2c929f2cd11f13557e064e30a4514e3862e127a2bdb3a3f40ec92023f255d`
