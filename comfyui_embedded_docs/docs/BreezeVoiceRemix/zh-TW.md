# Breeze Voice Remix

建立同一語言中語音的變更副本，可依文字描述進行變更，或從具名預設中選擇。副本會儲存到你的帳戶，並附上音訊預覽一併回傳。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `voice` | 要變更的 Breeze 語音。 | BREEZE_VOICE | 是 | - |
| `change` | `custom` 以文字描述變更內容，`preset` 選擇具名的變更。預設：`"custom"`。 | DYNAMIC_COMBO | 是 | `"custom"`<br>`"preset"` |
| `strength` | 數值越高，語音變更程度越大。預設：4.0。 | FLOAT | 否 | 1.0 至 10.0（步進值：0.1） |
| `seed` | 控制節點是否重新執行；無論 `seed` 為何，結果都不具確定性。預設：42。 | INT | 否 | 0 至 2147483647 |

### Change "custom" 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `prompt` | 語音應如何變更，例如更年長、更沙啞。預設：空。 | STRING | 是 | 多行文字 |

### Change "preset" 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `preset` | 具名的變更，依年齡、性別、音高、語速、能量與情緒分組。 | COMBO | 是 | 有多個可用選項 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `voice` | 變更後的語音副本。 | BREEZE_VOICE |
| `preview` | 重新混音後語音的音訊預覽。 | AUDIO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BreezeVoiceRemix/zh-TW.md)

---
**Source fingerprint (SHA-256):** `1bb135706fa760c6a6e8f4b9cb12a3f1506db375ee09cbd511b62d2bb24a9d2c`
