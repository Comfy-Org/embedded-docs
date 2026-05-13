> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/NormalizeVideoLatentStart/zh-TW.md)

此節點會調整影片潛在空間的前幾幀，使其看起來更像後續的幀。它從影片後方的一組參考幀計算平均值和變異數，並將這些相同的特徵套用至起始幀。這有助於在影片開頭創造更平滑且一致的視覺過渡。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `latent` | LATENT | 是 | - | 要處理的影片潛在空間表示。 |
| `start_frame_count` | INT | 是 | 1 至 16384 | 要標準化的潛在幀數，從開頭算起（預設值：4）。 |
| `reference_frame_count` | INT | 是 | 1 至 16384 | 起始幀之後用作參考的潛在幀數（預設值：5）。 |

**注意：** `reference_frame_count` 會自動限制為起始幀之後可用的幀數。如果影片潛在空間只有 1 幀長，則不會執行標準化，並直接回傳原始潛在空間。

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `latent` | LATENT | 已處理的影片潛在空間，其起始幀已標準化。 |

---
**Source fingerprint (SHA-256):** `64844f3bf1735952334dcca3a829e8f666fd89e817ab66cf3c2dc04ecbbdff56`
