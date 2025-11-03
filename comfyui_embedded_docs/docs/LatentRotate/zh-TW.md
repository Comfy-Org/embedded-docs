> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentRotate/zh-TW.md)

LatentRotate 節點專為將圖片的潛在表徵按指定角度旋轉而設計。它抽象化了操作潛在空間以實現旋轉效果的複雜性，讓使用者能夠輕鬆地在生成模型的潛在空間中轉換圖片。

## 輸入參數

| 參數名稱 | 資料類型 | 描述 |
|-----------|-------------|-------------|
| `samples` | `LATENT`    | 此參數代表待旋轉圖片的潛在表徵，對於決定旋轉操作的起始點至關重要。 |
| `rotation` | COMBO[STRING] | 此參數指定潛在圖片應旋轉的角度，直接影響最終圖片的朝向。 |

## 輸出參數

| 參數名稱 | 資料類型 | 描述 |
|-----------|-------------|-------------|
| `latent`  | `LATENT`    | 輸出為輸入潛在表徵經過指定角度旋轉後的修改版本。 |