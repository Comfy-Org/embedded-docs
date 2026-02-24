> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXAVTextEncoderLoader/zh-TW.md)

此節點載入 LTXV 音訊模型的專用文字編碼器。它將特定的文字編碼器檔案與檢查點檔案結合，建立一個可用於音訊相關文字條件任務的 CLIP 模型。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `text_encoder` | STRING | 是 | 提供多個選項 | 要載入的 LTXV 文字編碼器模型檔案名稱。可用選項從 `text_encoders` 資料夾載入。 |
| `ckpt_name` | STRING | 是 | 提供多個選項 | 要載入的檢查點檔案名稱。可用選項從 `checkpoints` 資料夾載入。 |
| `device` | STRING | 否 | `"default"`<br>`"cpu"` | 指定載入模型的裝置。使用 `"cpu"` 可強制載入到 CPU。預設行為 (`"default"`) 使用系統的自動裝置配置。 |

**注意：** `text_encoder` 和 `ckpt_name` 參數需配合使用。此節點會載入兩個指定的檔案以建立一個單一、可運作的 CLIP 模型。這些檔案必須與 LTXV 架構相容。

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `clip` | CLIP | 已載入的 LTXV CLIP 模型，準備好用於為音訊生成編碼文字提示。 |
