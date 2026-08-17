# HiDream-O1 參考圖像

## 概述

將參考圖像附加到正向與負向條件上。此節點允許您提供一張或多張參考圖像，這些圖像將用於引導圖像生成過程，無論是基於指令進行編輯，還是進行主體驅動的個人化。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `positive` | 要附加參考圖像的正向條件。 | CONDITIONING | 是 | - |
| `negative` | 要附加參考圖像的負向條件。 | CONDITIONING | 是 | - |
| `images` | 參考圖像。1 張圖像 = 指令編輯；2-10 張圖像 = 多參考。 | IMAGE | 是 | 1 to 10 images |

**關於 `images` 參數的說明：** 這是一個自動擴充輸入，接受 1 到 10 張圖像。圖像會標記為 `image_1` 到 `image_10`。您必須至少提供 1 張圖像。圖像數量決定操作模式：單張圖像用於編輯指令，而多張圖像（2-10）則用於主體驅動的個人化。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `positive` | 已附加參考圖像的正向條件。 | CONDITIONING |
| `negative` | 已附加參考圖像的負向條件。 | CONDITIONING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HiDreamO1ReferenceImages/zh-TW.md)

---
**Source fingerprint (SHA-256):** `f05f6be19df8b8697a98507163e8f60fd0cf2048c81f92597d2ae0a3395b8c6d`
