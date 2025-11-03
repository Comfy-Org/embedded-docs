> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DiffusersLoader/zh-TW.md)

DiffusersLoader 節點從 diffusers 格式載入預訓練模型。它會搜尋包含 model_index.json 檔案的有效 diffusers 模型目錄，並將其載入為 MODEL、CLIP 和 VAE 元件，以便在流程中使用。此節點屬於已棄用的載入器類別，並提供與 Hugging Face diffusers 模型的相容性。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 參數說明 |
|-----------|-----------|----------|-------|-------------|
| `model_path` | STRING | 是 | 提供多個選項<br>（自動從 diffusers 資料夾填入） | 要載入的 diffusers 模型目錄路徑。節點會自動掃描已設定的 diffusers 資料夾中的有效 diffusers 模型，並列出可用選項。 |

## 輸出參數

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `MODEL` | MODEL | 從 diffusers 格式載入的模型元件 |
| `CLIP` | CLIP | 從 diffusers 格式載入的 CLIP 模型元件 |
| `VAE` | VAE | 從 diffusers 格式載入的 VAE（變分自編碼器）元件 |