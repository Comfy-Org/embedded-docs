# Bria 解析度提升

Bria Increase Resolution 會使用 Bria 的影像放大服務，將輸入影像放大 2 倍或 4 倍，同時保留原始內容。此節點會上傳影像、將其提交至 Bria 服務進行處理、等待結果，並傳回放大後的影像。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `圖像` | 要放大的輸入影像。 | IMAGE | 是 | 單張影像 |
| `desired_increase` | 解析度倍率。輸出在每一邊都必須不超過 8192 像素。 | COMBO | 是 | "2"<br>"4" |
| `auto_downscale` | 當輸出會超過限制時，自動降低倍率；若這樣仍不足，則縮小輸入影像。（預設：False） | BOOLEAN | 是 | True<br>False |
| `內容審核` | 審核設定。當設為 "true" 時，會啟用 `visual_input_moderation` 和 `visual_output_moderation` 子選項，兩者預設皆為 False。 | DYNAMIC_COMBO | 是 | "false"<br>"true" |

注意：
- 當 `moderation` 設為 "true" 時，子選項 `visual_input_moderation` 和 `visual_output_moderation` 會變為可用，兩者預設皆為 False。它們控制輸入影像與輸出影像內容的審核。
- 此節點強制輸出每一邊最大為 8192 像素。若所選倍率會超過此限制，且未啟用 `auto_downscale`，則會引發錯誤。啟用 `auto_downscale` 可讓節點自動使用較低倍率，或改為縮小輸入影像。
- Bria 會先將輸入影像的短邊放大到至少 224 像素，再進行放大。過於狹長的影像可能會觸發錯誤，要求將其裁切為較接近正方形的形狀。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `IMAGE` | Bria 服務傳回的放大後影像。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaIncreaseResolution/zh-TW.md)

---
**Source fingerprint (SHA-256):** `6db9bf6c0d8a79903893b352658d3a8e02f67d375f3d604e9ab2a69624142885`
