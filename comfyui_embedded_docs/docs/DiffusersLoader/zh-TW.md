# Diffusers 載入器

DiffusersLoader 節點會載入以 diffusers 格式儲存的預訓練模型。它會搜尋已設定的 `diffusers` 資料夾，尋找包含 `model_index.json` 檔案的目錄，讓您選取其中一個，並將其載入為管線中使用的 MODEL、CLIP 和 VAE 元件。此節點已棄用，但仍保留以相容於 Hugging Face diffusers 模型。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model_path` | 要載入的 diffusers 模型目錄路徑。節點會自動掃描已設定的 diffusers 資料夾，尋找有效的模型並列出可用的選項。 | COMBO | 是 | 多個選項可用<br>（從 diffusers 資料夾自動填入） |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-----------|-------------|-----------|
| `MODEL` | 從 diffusers 格式載入的模型元件。 | MODEL |
| `CLIP` | 從 diffusers 格式載入的 CLIP 模型元件。 | CLIP |
| `VAE` | 從 diffusers 格式載入的 VAE（變分自編碼器）元件。 | VAE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DiffusersLoader/zh-TW.md)

---
**Source fingerprint (SHA-256):** `75238342d05eac7528f981a2d4544accb6053891cd078a77751cc838054225d4`
