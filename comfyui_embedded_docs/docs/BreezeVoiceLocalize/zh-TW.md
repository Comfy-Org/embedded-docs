# Breeze Voice Localize

建立一個能以另一種語言母語發音的語音複本，而非以原本的口音朗讀外語。該複本會儲存至您的帳戶，並回傳一段音訊預覽。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `voice` | 要複製的 Breeze 語音。 | BREEZE_VOICE | 是 | - |
| `language` | 新語音所說的語言。預設：`"English"`。 | COMBO | 是 | 有多個選項可用 |
| `seed` | 控制此節點是否重新執行；無論種子值為何，結果皆非確定性。預設：42。 | INT | 否 | 0 至 2147483647 |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `voice` | 該語音的本地化複本，以原始語音與語言命名。 | BREEZE_VOICE |
| `preview` | 本地化語音的音訊預覽。 | AUDIO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BreezeVoiceLocalize/zh-TW.md)

---
**Source fingerprint (SHA-256):** `a997fbc3426669f6e5725c455f49f3e16d5e14806ea3fac26657459f63e99db1`
