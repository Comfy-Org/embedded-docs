# SUPIRApply

SUPIRApply 節點會將 SUPIR 模型修補程式套用到擴散模型。它使用該修補程式來修改模型的行為，使其能在取樣過程中納入輸入影像的引導。此節點也提供控制選項，可調整此引導隨時間變化的強度，並包含一項選用功能，有助於維持對原始輸入的忠實度。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 要套用 SUPIR 修補程式的基本擴散模型。 | MODEL | 是 | - |
| `model_patch` | 包含用於修改模型之權重與設定的 SUPIR 模型修補程式。 | MODELPATCH | 是 | - |
| `vae` | 用於將輸入影像編碼為潛在表示的 VAE（變分自編碼器）。 | VAE | 是 | - |
| `image` | 用於引導生成過程的輸入影像。僅使用前三個色彩通道（RGB）。 | IMAGE | 是 | - |
| `strength_start` | 取樣開始時（高 sigma）的控制強度。影像引導的影響由此值開始。預設值：1.0 | FLOAT | 是 | 0.0 - 10.0 |
| `strength_end` | 取樣結束時（低 sigma）的控制強度。從起始值線性內插。影像引導的影響在此值結束。預設值：1.0 | FLOAT | 是 | 0.0 - 10.0 |
| `restore_cfg` | 將去噪後的輸出拉向輸入潛在表示。數值越高，對輸入的保真度越強。設為 0 可停用。預設值：4.0 | FLOAT | 是 | 0.0 - 20.0 |
| `restore_cfg_s_tmin` | 低於此 sigma 閾值時，`restore_cfg` 會被停用。預設值：0.05 | FLOAT | 是 | 0.0 - 1.0 |

*注意：* `image` 輸入在處理時只會擷取 RGB 通道。如果提供含有 alpha 通道的影像，alpha 通道將被忽略。

*注意：* `restore_cfg` 僅在設定為大於 0 的值時才會生效。設為 0 會完全停用還原後處理。啟用時，只有在目前的 sigma 值高於 `restore_cfg_s_tmin` 時才會套用此校正。

*注意：* 此節點在 ComfyUI 中被標記為實驗性功能。

## 輸出

| 輸出名 | 說明 | 資料類型 |
| --- | --- | --- |
| `model` | 已套用 SUPIR 修補程式，並設定了任何額外 CFG 後置函式的擴散模型。 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SUPIRApply/zh-TW.md)

---
**Source fingerprint (SHA-256):** `fa9f67f63777160863c44c620d8de11e92f79245c3f5b60e138975dfd0cc65c7`
