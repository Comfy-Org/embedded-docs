> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TomePatchModel/zh-TW.md)

此節點將 Token Merging (ToMe) 技術應用於擴散模型，以降低推理過程中的計算需求。它透過在注意力機制中有選擇性地合併相似 token 來實現，使模型能夠處理更少的 token 同時保持影像品質。此技術有助於在不顯著損失品質的情況下加速生成過程。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 參數說明 |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | 是 | - | 要應用 token 合併技術的擴散模型 |
| `比例` | FLOAT | 否 | 0.0 - 1.0 | 要合併的 token 比例（預設值：0.3） |

## 輸出結果

| 輸出名稱 | 資料類型 | 輸出說明 |
|-------------|-----------|-------------|
| `model` | MODEL | 已應用 token 合併技術的修改後模型 |