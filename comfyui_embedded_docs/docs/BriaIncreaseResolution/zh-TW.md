# BriaIncreaseResolution

Bria Increase Resolution 使用 Bria 的圖像放大 API，將輸入圖像放大 2 倍或 4 倍，同時保留原始內容。此節點會上傳圖像，在 Bria 服務上進行處理，並將放大後的結果以圖像形式傳回。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `image` | 要放大的輸入圖像。 | IMAGE | 是 | 單張圖像 |
| `desired_increase` | 解析度倍率。輸出每邊必須在 8192 像素以內。 | COMBO | 是 | "2"<br>"4" |
| `auto_downscale` | 當輸出會超過限制時，自動降低倍率；若仍不足，則縮小輸入圖像。（預設值：False） | BOOLEAN | 是 | True<br>False |
| `moderation` | 審核設定。設為 "true" 時，會啟用 `visual_input_moderation` 和 `visual_output_moderation` 子選項，兩者預設皆為 False。 | DYNAMIC_COMBO | 是 | "false"<br>"true" |

注意事項：
- 此節點會強制限制輸出最大邊長為 8192 像素。若選擇的倍率會超過此限制，且 `auto_downscale` 停用，則會引發錯誤。啟用 `auto_downscale` 可讓節點自動使用較低的倍率，或改為縮小輸入圖像。
- Bria 在放大前，會先將輸入圖像的短邊至少放大到 224 像素。圖像過於細長時，可能會觸發錯誤，要求裁剪成更接近正方形的形狀。

## 輸出

| 輸出名 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `IMAGE` | Bria API 傳回的放大圖像。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaIncreaseResolution/zh-TW.md)

---
**Source fingerprint (SHA-256):** `6db9bf6c0d8a79903893b352658d3a8e02f67d375f3d604e9ab2a69624142885`
