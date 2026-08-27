# 預覽音訊

Preview Audio 節點會建立一個暫時的音訊預覽，可直接在介面中播放，不需將音訊儲存至 ComfyUI 輸出目錄。此節點接收音訊資料作為輸入，並產生預覽小工具，讓使用者無需儲存永久檔案即可聆聽音訊輸出。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 數值範圍 |
| --- | --- | --- | --- | --- |
| `音訊` | 要預覽的音訊資料。若輸入音訊為 None，此節點將引發錯誤；這可能發生在來源影片沒有音訊軌道時。 | AUDIO | 是 | - |

**注意：** 如果輸入的 `audio` 為 None，節點會拋出 ValueError。這可能發生在來源影片沒有音訊軌道時。

## 輸出

| 輸出名 | 說明 | 資料類型 |
| --- | --- | --- |
| `audio` | 從輸入傳遞過來的音訊資料，用於預覽。 | AUDIO |
| `ui` | 在介面中顯示音訊播放器小工具，用於預覽音訊。 | UI |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewAudio/zh-TW.md)

---
**Source fingerprint (SHA-256):** `ccbf9873a16bf1578fe25d178454d782f4f9b37ad5721721bef0aee3ff374f9f`
