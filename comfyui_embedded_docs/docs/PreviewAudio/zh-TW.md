# 預覽音訊

PreviewAudio 節點可讓您直接在介面中預覽音訊，而無需將其儲存到 ComfyUI 輸出目錄。它接收音訊資料作為輸入，並顯示一個音訊播放器小工具，供您用來聽取結果。如果輸入音訊為 None，節點會引發錯誤；當來源影片沒有音訊軌時，就可能發生這種情況。

## 輸入

| 參數 | 描述 | 資料型別 | 必須 | 範圍 |
| --- | --- | --- | --- | --- |
| `audio` | 要預覽的音訊資料。如果音訊為 None，節點會引發錯誤；當來源影片沒有音訊軌時，就可能發生這種情況。 | AUDIO | 是 | - |

## 輸出

| 輸出名稱 | 描述 | 資料型別 |
| --- | --- | --- |
| `audio` | 傳遞通過節點的音訊資料。介面中會顯示音訊播放器小工具，用於預覽音訊。 | AUDIO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewAudio/zh-TW.md)

---
**Source fingerprint (SHA-256):** `ccbf9873a16bf1578fe25d178454d782f4f9b37ad5721721bef0aee3ff374f9f`
