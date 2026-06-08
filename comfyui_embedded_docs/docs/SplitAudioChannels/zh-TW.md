SplitAudioChannels 節點可將立體聲音訊分離為獨立的左聲道和右聲道。它接收具有兩個聲道的立體聲音訊輸入，並輸出兩個獨立的音訊串流，一個用於左聲道，另一個用於右聲道。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `音訊` | 要分離為聲道的立體聲音訊輸入 | AUDIO | 是 | - |

**注意：** 輸入音訊必須恰好有兩個聲道（立體聲）。如果輸入音訊只有一個聲道，此節點將會引發錯誤。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `右聲道` | 分離後的左聲道音訊 | AUDIO |
| `right` | 分離後的右聲道音訊 | AUDIO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SplitAudioChannels/zh-TW.md)

---
**Source fingerprint (SHA-256):** `48f329f3eb9749e75eda1038c43caf42ee63d8a1fa66ab29ad3d34b5d136e323`
