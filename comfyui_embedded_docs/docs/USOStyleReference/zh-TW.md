# USO風格參考

USOStyleReference 節點會將參考影像的樣式資訊套用至 Flux 模型。它會從 CLIP 視覺輸出建立樣式嵌入，然後修補模型的複本，使產生期間能將樣式嵌入插入至文字提示條件化之前。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | Range |
| --- | --- | --- | --- | --- |
| `model` | 要套用樣式參考修補的基礎模型 | MODEL | 是 | - |
| `model_patch` | 包含樣式參考資訊的模型修補 | MODEL_PATCH | 是 | - |
| `clip_vision_output` | 從 CLIP 視覺處理中提取的編碼視覺特徵。此節點會結合第 -20 層和第 -11 層的隱藏狀態，以及倒數第二層的隱藏狀態，來建立樣式嵌入 | CLIP_VISION_OUTPUT | 是 | - |

注意：所有三個輸入皆為必填。此節點標記為實驗性功能。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `model` | 已套用樣式參考修補的修改後模型 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/USOStyleReference/zh-TW.md)

---
**Source fingerprint (SHA-256):** `9033dddb76fafb388c67dcd09d96102a7ab3e5bc416cec61bf18d088da37a0f0`
