# 預覽音訊

Preview Audio 節點可讓您直接在 ComfyUI 中試聽音訊，而無需將其儲存到輸出目錄。它會接收音訊輸入，檢查是否確實存在音訊資料，然後透過介面中的預覽播放器播放，同時將相同音訊作為輸出傳遞。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `音訊` | 要預覽的音訊資料。若此輸入為 None，節點會引發 ValueError；當來源影片沒有音軌時，就可能發生此情況。 | AUDIO | 是 | - |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `audio` | 從輸入原樣傳遞的音訊資料，因此此節點可置於工作流程中間。 | AUDIO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewAudio/zh-TW.md)

---
**Source fingerprint (SHA-256):** `02dbc5cb7d6924aae63c59e926a8ea265eb0889dbc2e6b47ff60f666a55d1adf`
