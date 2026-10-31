# VAE Compute Dtype

此節點會設定 VAE 進行編碼或解碼時使用的計算 dtype，而不會變更模型圖的其餘部分。它會回傳一份套用了所要求精度的輸入 VAE 副本，因此工作流程可以讓其中一個分支以較高精度執行，而其他分支保持不變。"default" 會保留輸入 VAE 目前已使用的計算 dtype。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `vae` | 要調整的 VAE。此節點會作用於副本，因此已連線的 VAE 不會被修改。 | VAE | 是 | - |
| `dtype` | 用於 VAE 編碼與解碼的計算 dtype。"default" 會保留輸入 VAE 的計算 dtype（預設："default"）。 | COMBO | 是 | "default"<br>"fp32"<br>"fp16"<br>"bf16" |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `vae` | 已套用所選計算 dtype 的 VAE 副本。 | VAE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEComputeDtype/zh-TW.md)

---
**Source fingerprint (SHA-256):** `239e5829d76b4bd43ec300fc2b7c8c408b5bd4a93918da417ecf43817aee3e12`
