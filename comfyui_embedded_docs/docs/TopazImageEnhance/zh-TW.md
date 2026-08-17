# Topaz 影像增強

Topaz Image Enhance 節點提供業界標準的影像放大與增強功能。它使用雲端 AI 模型處理單一輸入影像，以改善品質、細節與解析度。此節點提供對增強過程的精細控制，包括創意引導、主體對焦與臉部保留等選項。

## 輸入

| 參數 | 描述 | 資料型態 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | 用於影像增強的 AI 模型。 | COMBO | 是 | `"Reimagine"` |
| `image` | 要增強的輸入影像。僅支援單一影像。 | IMAGE | 是 | - |
| `prompt` | 用於創意放大引導的選用文字提示（預設為空）。 | STRING | 否 | - |
| `subject_detection` | 控制增強過程專注於影像的哪個部分（預設為 "All"）。 | COMBO | 否 | `"All"`<br>`"Foreground"`<br>`"Background"` |
| `face_enhancement` | 在處理過程中增強臉部（若存在）（預設為 True）。 | BOOLEAN | 否 | - |
| `face_enhancement_creativity` | 設定臉部增強的創意等級（預設為 0.0）。 | FLOAT | 否 | 0.0 - 1.0 |
| `face_enhancement_strength` | 控制增強後的臉部相對於背景的銳利程度（預設為 1.0）。 | FLOAT | 否 | 0.0 - 1.0 |
| `crop_to_fill` | 預設情況下，當輸出長寬比不同時，影像會以信箱模式顯示。啟用此選項可裁切影像以填滿輸出尺寸（預設為 False）。 | BOOLEAN | 否 | - |
| `output_width` | 零值表示自動計算（通常會是原始尺寸，或若指定了 `output_height` 則使用該值）（預設為 0）。 | INT | 否 | 0 - 32000 |
| `output_height` | 零值表示以與原始或 `output_width` 相同的高度輸出（預設為 0）。 | INT | 否 | 0 - 32000 |
| `creativity` | 控制增強的整體創意等級（預設為 3）。 | INT | 否 | 1 - 9 |
| `face_preservation` | 保留主體的面部特徵（預設為 True）。 | BOOLEAN | 否 | - |
| `color_preservation` | 保留原始色彩（預設為 True）。 | BOOLEAN | 否 | - |

**注意：** 此節點僅能處理單一輸入影像。提供多張影像的批次將導致錯誤。

## 輸出

| 輸出名稱 | 描述 | 資料型態 |
|-------------|-------------|-----------|
| `image` | 增強後的輸出影像。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TopazImageEnhance/zh-TW.md)

---
**Source fingerprint (SHA-256):** `a4b622ced661dd1dd1c57d4536359874d2203c8d4064c76fa684b9935e265085`
