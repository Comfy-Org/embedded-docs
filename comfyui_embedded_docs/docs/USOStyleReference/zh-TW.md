# USO風格參考

USOStyleReference 節點透過將 CLIP 視覺特徵與模型補丁結合，將風格參考應用於模型，並返回輸入模型的補丁副本。此節點主要用於 Flux 模型，並標記為實驗性。視覺風格資訊會與模型的文字條件結合，使其能夠影響生成過程。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `模型` | 套用風格參考補丁的基礎模型。 | MODEL | 是 | - |
| `模型修補` | 包含投影模型的模型補丁，用於編碼參考影像特徵。 | MODEL_PATCH | 是 | - |
| `CLIP視覺輸出` | 從參考影像的 CLIP 視覺處理中提取的編碼視覺特徵。 | CLIP_VISION_OUTPUT | 是 | - |

注意：`clip_vision_output` 必須來自提供完整隱藏狀態和倒數第二個隱藏狀態的 CLIP 視覺模型。此節點會將倒數第 20 個、倒數第 11 個和倒數第二個隱藏狀態組合成風格嵌入。`model_patch` 必須透過其 `model` 屬性暴露一個投影模型，用於將這些影像特徵轉換為風格嵌入。在取樣期間，風格嵌入會被前置到文字條件之前，以便影響生成。

## 輸出

| 輸出名 | 描述 | 資料類型 |
| --- | --- | --- |
| `model` | 套用了風格參考補丁的修改後模型。 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/USOStyleReference/zh-TW.md)

---
**Source fingerprint (SHA-256):** `9033dddb76fafb388c67dcd09d96102a7ab3e5bc416cec61bf18d088da37a0f0`
