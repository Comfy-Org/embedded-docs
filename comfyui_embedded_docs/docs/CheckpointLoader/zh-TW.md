# 載入檢查點與設定檔（已淘汰）

CheckpointLoader 節點會載入預先訓練的模型檢查點及其設定檔。它接受設定檔與檢查點檔案作為輸入，並傳回已載入的模型元件，包括主模型、CLIP 模型與 VAE 模型，供工作流程使用。

## 輸入

| 參數 | 描述 | 資料型別 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `config_name` | 定義模型架構與設定的設定檔 | STRING | 是 | 可用設定檔 |
| `ckpt_name` | 包含已訓練模型權重與參數的檢查點檔案 | STRING | 是 | 可用檢查點檔案 |

**注意：** 此節點需要同時選取設定檔與檢查點檔案。設定檔必須與所載入檢查點檔案的架構相符。

## 輸出

| 輸出名 | 描述 | 資料型別 |
| --- | --- | --- |
| `MODEL` | 已載入、可立即用於推論的主模型元件 | MODEL |
| `CLIP` | 已載入、用於文字編碼的 CLIP 模型元件 | CLIP |
| `VAE` | 已載入、用於影像編碼與解碼的 VAE 模型元件 | VAE |

**重要注意：** 此節點已標記為已棄用，並可能在未來版本中移除。針對新的工作流程，請考慮使用其他載入節點。

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CheckpointLoader/zh-TW.md)

---
**Source fingerprint (SHA-256):** `820cd9f7a5ccd5a70d2b29906c8deca3632d2ccba84ca51022717e061afb72b3`
