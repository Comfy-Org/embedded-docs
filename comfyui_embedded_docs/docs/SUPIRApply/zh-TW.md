# SUPIRApply

SUPIRApply 節點會將 SUPIR 模型補丁套用到擴散模型。它使用該補丁來修改模型的行為，使其能夠在取樣過程中納入來自輸入影像的引導。此節點也提供控制項，可隨時間調整此引導的強度，並包含一項選用功能，用於協助維持對原始輸入的保真度。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 將套用 SUPIR 補丁的基礎擴散模型。 | MODEL | 是 | - |
| `model_patch` | 包含用於修改模型之權重與設定的 SUPIR 模型補丁。 | MODEL_PATCH | 是 | - |
| `vae` | 用於將輸入影像編碼為潛在表徵的 VAE（變分自編碼器）。 | VAE | 是 | - |
| `image` | 用於引導生成過程的輸入影像。僅使用前三個色彩通道（RGB）。 | IMAGE | 是 | - |
| `strength_start` | 取樣開始時（高 sigma）的控制強度。影像引導的影響會從此值開始。（預設：1.0） | FLOAT | 是 | 0.0 - 10.0 |
| `strength_end` | 取樣結束時（低 sigma）的控制強度。會從起始值線性插值。影像引導的影響會在此值結束。（預設：1.0） | FLOAT | 是 | 0.0 - 10.0 |
| `restore_cfg` | 將去噪輸出拉向輸入潛在表徵。數值越高 = 對輸入的保真度越高。設為 0 可停用。（預設：4.0，進階設定） | FLOAT | 是 | 0.0 - 20.0 |
| `restore_cfg_s_tmin` | sigma 閾值，低於此值時會停用 `restore_cfg`。（預設：0.05，進階設定） | FLOAT | 是 | 0.0 - 1.0 |

*注意：* `image` 輸入會被處理為僅擷取 RGB 通道。若提供的影像帶有 alpha 通道，則會忽略 alpha 通道。

*注意：* 若 SUPIR 模型補丁提供去噪編碼器權重，則輸入影像會使用這些權重進行編碼，而非使用一般 VAE 編碼器。

*注意：* `restore_cfg` 僅在設為大於 0 的值時才會生效。設為 0 會完全停用還原後處理。啟用時，僅會在當前 sigma 值高於 `restore_cfg_s_tmin` 時套用校正。

*注意：* 此節點在 ComfyUI 中標記為實驗性。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `model` | 已套用 SUPIR 補丁並配置任何額外 post-CFG 函式的輸入模型複製副本。 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SUPIRApply/zh-TW.md)

---
**Source fingerprint (SHA-256):** `fa9f67f63777160863c44c620d8de11e92f79245c3f5b60e138975dfd0cc65c7`
