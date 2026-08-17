# LTXV 音訊文字編碼器載入器

此節點載入 LTXV 音訊模型的專用文字編碼器。它會將文字編碼器檔案與檢查點檔案結合，建立一個可用於音訊相關文字條件化任務的 CLIP 模型。根據此節點的配方描述，LTXV 音訊文字編碼器應為 Gemma 3 12B 模型或相符的 Gemma 4 模型。

## 輸入

| 參數 | 描述 | 資料型別 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `text_encoder` | 要載入的 LTXV 文字編碼器模型檔案名稱。可用選項從 `text_encoders` 資料夾載入。 | COMBO | 是 | 多個可用選項 |
| `ckpt_name` | 要載入的檢查點檔案名稱。可用選項從 `checkpoints` 資料夾載入。 | COMBO | 是 | 多個可用選項 |
| `device` | 指定要將模型載入到的裝置。使用 `"cpu"` 強制載入到 CPU。預設行為（`"default"`）使用系統的自動裝置放置（預設值：`"default"`）。 | COMBO | 否 | `"default"`<br>`"cpu"` |

**注意：** `text_encoder` 和 `ckpt_name` 參數需搭配使用。此節點會載入兩個指定的檔案，以建立單一且可用的 CLIP 模型。這些檔案必須與 LTXV 架構相容。

## 輸出

| 輸出名稱 | 描述 | 資料型別 |
| --- | --- | --- |
| `clip` | 已載入的 LTXV CLIP 模型，可用於編碼音訊生成的文字提示。 | CLIP |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXAVTextEncoderLoader/zh-TW.md)

---
**Source fingerprint (SHA-256):** `1f3df2c1791203ba849a87897de14052e0cb8370100dbca19df4cf30169a0a2a`
