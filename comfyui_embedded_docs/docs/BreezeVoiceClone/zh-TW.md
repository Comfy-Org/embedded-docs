# Breeze Voice Clone

從單一講者的錄音建立 Breeze 語音。該語音會儲存到你的帳戶，並以語音控制代碼的形式回傳，同時附上其聲音效果的音訊預覽。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `audio` | 單一講者的錄音，長度至少 3 秒。僅使用前 60 秒。 | AUDIO | 是 | - |
| `remove_background_noise` | 在複製前先清理錄音。預設：false。 | BOOLEAN | 否 | true<br>false |
| `seed` | 控制節點是否重新執行；無論種子值為何，結果皆不具確定性。預設：42。 | INT | 否 | 0 至 2147483647 |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `voice` | 新的 Breeze 語音，供 Breeze Text to Speech 使用。 | BREEZE_VOICE |
| `preview` | 複製語音的音訊預覽。 | AUDIO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BreezeVoiceClone/zh-TW.md)

---
**Source fingerprint (SHA-256):** `3c2e461a8e1a38bfa494a687f5b77a375e9e81c77964493181d7c622a682c56f`
