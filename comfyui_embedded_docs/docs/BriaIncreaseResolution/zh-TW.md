# BriaIncreaseResolution

Bria Increase Resolution 使用 Bria 的影像放大服務，將輸入影像放大 2 倍或 4 倍，同時保留原始內容。它會上傳影像、在 Bria 服務上進行處理，並將放大後的結果作為影像回傳。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `圖像` | 要放大的輸入影像。 | IMAGE | 是 | 單張影像 |
| `desired_increase` | 解析度倍率。輸出影像的每一邊都必須在 8192 像素以內。 | COMBO | 是 | "2"<br>"4" |
| `auto_downscale` | 當輸出會超過限制時，自動降低倍率；若仍不足，則縮小輸入影像。（預設：False） | BOOLEAN | 是 | True<br>False |
| `內容審核` | 審核設定。設為 "true" 時，會啟用 `visual_input_moderation` 與 `visual_output_moderation` 子選項，兩者皆預設為 False。 | DYNAMIC_COMBO | 是 | "false"<br>"true" |

備註：
- 當 `moderation` 設為 "true" 時，子選項 `visual_input_moderation` 與 `visual_output_moderation` 會變為可用，兩者皆預設為 False。它們分別控制輸入影像與輸出影像內容的審核。
- 此節點強制限制輸出影像的最大邊長為 8192 像素。如果所選倍率會超過此限制，且 `auto_downscale` 已停用，則會產生錯誤。啟用 `auto_downscale` 後，節點會自動改用較低的倍率，或改為縮小輸入影像。
- Bria 在放大前，會先將輸入影像的短邊至少放大至 224 像素。過於狹長的影像可能觸發錯誤，要求將其裁切為較接近正方形的形狀。

## 輸出

| 輸出名 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `IMAGE` | Bria API 回傳的放大後影像。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaIncreaseResolution/zh-TW.md)

---
**Source fingerprint (SHA-256):** `6db9bf6c0d8a79903893b352658d3a8e02f67d375f3d604e9ab2a69624142885`
