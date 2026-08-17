# Diffusers 載入器

DiffusersLoader 節點已棄用。此節點用於載入以 Hugging Face diffusers 格式儲存的預訓練模型，並回傳管線所需的三個標準元件：MODEL、CLIP 和 VAE。節點會自動掃描設定的 diffusers 資料夾，找出有效的模型目錄（包含 `model_index.json` 檔案的資料夾），並讓您選擇要載入的模型。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model_path` | 要載入的 diffusers 模型目錄路徑。節點會掃描設定的 diffusers 資料夾，並列出所有包含 `model_index.json` 檔案的目錄。 | COMBO | 是 | 自動從設定的 diffusers 資料夾中填入（每個包含 `model_index.json` 檔案的子目錄） |

注意：選取的路徑會與探索到的模型清單進行比對驗證。如果路徑已不在清單中，或找不到模型目錄，載入會失敗並顯示錯誤。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `MODEL` | 從 diffusers 格式載入的模型元件 | MODEL |
| `CLIP` | 從 diffusers 格式載入的 CLIP 文字編碼模型元件 | CLIP |
| `VAE` | 從 diffusers 格式載入的 VAE（變分自編碼器）元件 | VAE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DiffusersLoader/zh-TW.md)

---
**Source fingerprint (SHA-256):** `75238342d05eac7528f981a2d4544accb6053891cd078a77751cc838054225d4`
