# SUPIRApply

SUPIRApply 節點將 SUPIR 模型修補程式套用至擴散模型。它使用該修補程式來修改模型的行為，使其能夠在取樣過程中納入輸入影像的引導。此節點也提供控制項，用於隨時間調整此引導的強度，並包含一個選用功能，有助於維持對原始輸入的忠實度。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 基礎擴散模型，SUPIR 修補程式將套用至此模型。 | MODEL | 是 | - |
| `model_patch` | 包含用於修改模型的權重與配置的 SUPIR 模型修補程式。 | MODELPATCH | 是 | - |
| `vae` | 用於將輸入影像編碼為潛在表示的 VAE（變分自編碼器）。 | VAE | 是 | - |
| `image` | 用於引導生成過程的輸入影像。僅使用前三個色彩通道（RGB）。 | IMAGE | 是 | - |
| `strength_start` | 取樣開始時（高 sigma）的控制強度。影像引導的影響從此值開始。（預設值：1.0） | FLOAT | 否 | 0.0 - 10.0 |
| `strength_end` | 取樣結束時（低 sigma）的控制強度。從起始值線性內插。影像引導的影響在此值結束。（預設值：1.0） | FLOAT | 否 | 0.0 - 10.0 |
| `restore_cfg` | 將去噪後的輸出拉向輸入潛在表示。數值越高，對輸入的忠實度越強。設為 0 以停用。（預設值：4.0） | FLOAT | 否 | 0.0 - 20.0 |
| `restore_cfg_s_tmin` | 低於此 sigma 閾值時，restore_cfg 會被停用。（預設值：0.05） | FLOAT | 否 | 0.0 - 1.0 |

*注意：* `image` 輸入會經處理以僅擷取 RGB 通道。若提供包含 alpha 通道的影像，則 alpha 通道將被忽略。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `model` | 已套用 SUPIR 修補程式，並配置了任何額外的後置 CFG 功能的擴散模型。 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SUPIRApply/zh-TW.md)

---
**Source fingerprint (SHA-256):** `fa9f67f63777160863c44c620d8de11e92f79245c3f5b60e138975dfd0cc65c7`
