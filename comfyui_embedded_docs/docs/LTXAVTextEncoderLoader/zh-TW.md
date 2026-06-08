此節點載入一個專門用於 LTXV 音訊模型的文字編碼器。它將特定的文字編碼器檔案與檢查點檔案結合，建立一個可用於音訊相關文字條件化任務的 CLIP 模型。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `text_encoder` | 要載入的 LTXV 文字編碼器模型檔案名稱。可用的選項從 `text_encoders` 資料夾中載入。 | STRING | 是 | 提供多個選項 |
| `ckpt_name` | 要載入的檢查點檔案名稱。可用的選項從 `checkpoints` 資料夾中載入。 | STRING | 是 | 提供多個選項 |
| `device` | 指定要載入模型的裝置。使用 `"cpu"` 強制載入到 CPU。預設行為（`"default"`）使用系統的自動裝置配置。 | STRING | 否 | `"default"`<br>`"cpu"` |

**注意：** `text_encoder` 和 `ckpt_name` 參數需搭配使用。此節點會載入兩個指定的檔案，以建立一個單一、功能完整的 CLIP 模型。這些檔案必須與 LTXV 架構相容。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `clip` | 已載入的 LTXV CLIP 模型，可用於編碼音訊生成的文字提示。 | CLIP |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXAVTextEncoderLoader/zh-TW.md)

---
**Source fingerprint (SHA-256):** `c072a0b3393aa44333bb15ae42179c50868a4e9d7ca706d6c7da5922625373e6`
