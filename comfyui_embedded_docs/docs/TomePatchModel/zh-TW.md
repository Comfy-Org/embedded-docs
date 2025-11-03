> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TomePatchModel/zh-TW.md)

TomePatchModel 節點將 Token Merging (ToMe) 技術應用於擴散模型，以降低推理過程中的計算需求。該技術透過在注意力機制中有選擇性地合併相似 token，使模型能夠處理更少的 token 同時保持影像品質。此方法有助於在不顯著損失品質的前提下加速生成過程。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 參數說明 |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | 是 | - | 要應用 token 合併技術的擴散模型 |
| `ratio` | FLOAT | 否 | 0.0 - 1.0 | 要合併的 token 比例（預設值：0.3） |

## 輸出結果

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `model` | MODEL | 已應用 token 合併技術的修改後模型 |