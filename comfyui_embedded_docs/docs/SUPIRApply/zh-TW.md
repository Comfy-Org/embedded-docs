> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SUPIRApply/zh-TW.md)

# SUPIRApply 節點

SUPIRApply 節點將 SUPIR 模型修補程式應用於擴散模型。它使用修補程式來修改模型的行為，使其能夠在取樣過程中納入輸入圖像的引導。該節點還提供用於調整此引導隨時間變化的強度的控制項，並包含一個可選功能，有助於保持對原始輸入的保真度。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | 是 | - | 將應用 SUPIR 修補程式的基本擴散模型。 |
| `model_patch` | MODELPATCH | 是 | - | 包含用於修改模型的權重和配置的 SUPIR 模型修補程式。 |
| `vae` | VAE | 是 | - | 用於將輸入圖像編碼為潛在表示的 VAE（變分自編碼器）。 |
| `image` | IMAGE | 是 | - | 用於引導生成過程的輸入圖像。僅使用前三個顏色通道（RGB）。 |
| `strength_start` | FLOAT | 否 | 0.0 - 10.0 | 取樣開始時（高 sigma）的控制強度。圖像引導的影響從此值開始。（預設值：1.0） |
| `strength_end` | FLOAT | 否 | 0.0 - 10.0 | 取樣結束時（低 sigma）的控制強度。從起始值線性插值。圖像引導的影響在此值結束。（預設值：1.0） |
| `restore_cfg` | FLOAT | 否 | 0.0 - 20.0 | 將去噪輸出拉向輸入潛在表示。數值越高 = 對輸入的保真度越強。設為 0 以停用。（預設值：4.0） |
| `restore_cfg_s_tmin` | FLOAT | 否 | 0.0 - 1.0 | 低於此 sigma 閾值時，`restore_cfg` 將被停用。（預設值：0.05） |

*注意：* `image` 輸入會經過處理以僅提取 RGB 通道。如果提供了帶有 Alpha 通道的圖像，則 Alpha 通道將被忽略。

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `model` | MODEL | 已應用 SUPIR 修補程式並配置了任何額外的後 CFG 功能的擴散模型。 |

---
**Source fingerprint (SHA-256):** `32ba7a337060b52d4c9085a6a2bc209c737e374dee4291d431d2caf768fc2817`
