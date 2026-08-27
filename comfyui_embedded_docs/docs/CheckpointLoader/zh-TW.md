# 載入檢查點與設定檔（已淘汰）

CheckpointLoader 節點會載入預訓練的模型檢查點及其配置文件。它以配置文件和檢查點文件作為輸入，並傳回已載入的模型組件 — 主模型、CLIP 模型和 VAE 模型 — 供工作流程使用。此節點已棄用。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `config_name` | 定義模型架構和設定的配置文件 | COMBO | 是 | 可用的配置文件 |
| `ckpt_name` | 包含已訓練模型權重和參數的檢查點文件 | COMBO | 是 | 可用的檢查點文件 |

**注意：** 此節點需要同時選取配置文件和檢查點文件。配置文件必須與要載入的檢查點文件的架構相符。

## 輸出

| 輸出名 | 描述 | 資料類型 |
| --- | --- | --- |
| `MODEL` | 已載入的主模型組件，可用於推論 | MODEL |
| `CLIP` | 已載入的 CLIP 模型組件，用於文字編碼 | CLIP |
| `VAE` | 已載入的 VAE 模型組件，用於影像編碼和解碼 | VAE |

**重要注意事項：** 此節點已被標記為棄用，並可能在未來版本中移除。對於新的工作流程，請考慮使用其他載入節點。

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CheckpointLoader/zh-TW.md)

---
**Source fingerprint (SHA-256):** `820cd9f7a5ccd5a70d2b29906c8deca3632d2ccba84ca51022717e061afb72b3`
