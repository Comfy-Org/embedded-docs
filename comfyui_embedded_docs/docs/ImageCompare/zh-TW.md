# 圖像比較

Image Compare 節點提供了一個視覺化介面，可透過可拖曳的滑桿並排比較兩張圖片。它被設計為輸出節點，這表示它不會將資料傳遞給其他節點，而是直接在使用者介面中顯示圖片供檢視。

## 輸入

| 參數 | 說明 | 資料型別 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `image_a` | 要比較的第一張圖片。 | IMAGE | 否 | - |
| `image_b` | 要比較的第二張圖片。 | IMAGE | 否 | - |
| `compare_view` | 在 UI 中啟用滑桿比較檢視的控制項。 | IMAGECOMPARE | 是 | - |

**注意：** 此節點是輸出節點。雖然 `image_a` 和 `image_b` 為選填，但至少必須提供一張圖片，節點才會有可見的效果。任何未連接的圖片輸入，節點都會顯示空白區域。

## 輸出

此節點是輸出節點，不會產生任何可供其他節點使用的資料輸出。其功能是在 ComfyUI 介面中顯示所提供的圖片。

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageCompare/zh-TW.md)

---
**Source fingerprint (SHA-256):** `bc065572c5631ed80c0590aabae775c51d0f607895a87cb2cca78037ab9a6638`
