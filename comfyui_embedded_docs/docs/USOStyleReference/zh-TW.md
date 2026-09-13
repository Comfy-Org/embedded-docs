# USO風格參考

USOStyleReference 節點會將 CLIP 視覺特徵與模型補丁結合，以將風格參考套用至模型，並回傳輸入模型套用補丁後的副本。視覺風格資訊會與模型的文字條件結合，因此能影響生成。此節點適用於 Flux 模型，並標記為實驗性功能。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `模型` | 要套用風格參考補丁的基礎模型。 | MODEL | 是 | - |
| `模型修補` | 包含投影模型的模型補丁，該投影模型用於編碼參考影像特徵。 | MODEL_PATCH | 是 | - |
| `CLIP視覺輸出` | 由參考影像的 CLIP 視覺處理所擷取出的編碼視覺特徵。 | CLIP_VISION_OUTPUT | 是 | - |

注意：`clip_vision_output` 必須來自能提供完整隱藏狀態與倒數第二個隱藏狀態的 CLIP 視覺模型。此節點會將倒數第 20 個、倒數第 11 個與倒數第二個隱藏狀態合併為風格嵌入。`model_patch` 必須透過其 `model` 屬性公開一個投影模型，該模型會將這些影像特徵轉換為風格嵌入。取樣期間，風格嵌入會前置到文字條件，使其能影響生成；而相符的零位置文字 ID 也會前置到文字 ID，讓識別碼序列與擴展後的條件保持一致。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `model` | 已套用風格參考補丁的修改後模型。 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/USOStyleReference/zh-TW.md)

---
**Source fingerprint (SHA-256):** `9033dddb76fafb388c67dcd09d96102a7ab3e5bc416cec61bf18d088da37a0f0`
