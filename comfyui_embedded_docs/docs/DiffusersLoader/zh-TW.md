# Diffusers 載入器

## 概述

DiffusersLoader 節點用於從 diffusers 格式載入預訓練模型。它會搜尋包含 `model_index.json` 檔案的有效 diffusers 模型目錄，並將其載入為 MODEL、CLIP 和 VAE 元件，以供後續流程使用。此節點屬於已棄用的載入器類別，提供與 Hugging Face diffusers 模型的相容性。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `model_path` | 要載入的 diffusers 模型目錄路徑。此節點會自動掃描已設定的 diffusers 資料夾中的有效 diffusers 模型，並列出可用的選項。 | STRING | 是 | 提供多個選項<br>(從 diffusers 資料夾自動填入) |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `MODEL` | 從 diffusers 格式載入的模型元件 | MODEL |
| `CLIP` | 從 diffusers 格式載入的 CLIP 模型元件 | CLIP |
| `VAE` | 從 diffusers 格式載入的 VAE（變分自編碼器）元件 | VAE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DiffusersLoader/zh-TW.md)

---
**Source fingerprint (SHA-256):** `59be9923ed76d4859d5f7217a802c43297cb5af3d895eb6713edea97a32c3db2`
