> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TopazImageEnhance/zh-TW.md)

Topaz Image Enhance 節點提供業界標準的影像放大與增強功能。它使用基於雲端的 AI 模型處理單一輸入影像，以提升品質、細節和解析度。該節點提供對增強過程的細粒度控制，包括創意引導、主體聚焦和臉部保留等選項。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | 是 | `"Reimagine"` | 用於影像增強的 AI 模型。 |
| `image` | IMAGE | 是 | - | 待增強的輸入影像。僅支援單一影像。 |
| `prompt` | STRING | 否 | - | 用於創意放大引導的選用文字提示（預設：空）。 |
| `subject_detection` | COMBO | 否 | `"All"`<br>`"Foreground"`<br>`"Background"` | 控制增強功能聚焦於影像的哪個部分（預設："All"）。 |
| `face_enhancement` | BOOLEAN | 否 | - | 啟用後，若影像中存在臉部則對其進行增強（預設：True）。 |
| `face_enhancement_creativity` | FLOAT | 否 | 0.0 - 1.0 | 設定臉部增強的創意等級（預設：0.0）。 |
| `face_enhancement_strength` | FLOAT | 否 | 0.0 - 1.0 | 控制增強後的臉部相對於背景的銳利程度（預設：1.0）。 |
| `crop_to_fill` | BOOLEAN | 否 | - | 預設情況下，當輸出長寬比不同時，影像會加上黑邊。啟用此選項將改為裁切影像以填滿輸出尺寸（預設：False）。 |
| `output_width` | INT | 否 | 0 - 32000 | 輸出影像的期望寬度。值為 0 表示將自動計算，通常基於原始尺寸或指定的 `output_height`（預設：0）。 |
| `output_height` | INT | 否 | 0 - 32000 | 輸出影像的期望高度。值為 0 表示將自動計算，通常基於原始尺寸或指定的 `output_width`（預設：0）。 |
| `creativity` | INT | 否 | 1 - 9 | 控制增強的整體創意等級（預設：3）。 |
| `face_preservation` | BOOLEAN | 否 | - | 保留影像中主體的臉部特徵（預設：True）。 |
| `color_preservation` | BOOLEAN | 否 | - | 保留輸入影像的原始色彩（預設：True）。 |

**注意：** 此節點僅能處理單一輸入影像。提供包含多張影像的批次將會導致錯誤。

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `image` | IMAGE | 增強後的輸出影像。 |
