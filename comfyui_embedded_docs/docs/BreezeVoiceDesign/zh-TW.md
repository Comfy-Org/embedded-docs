# Breeze Voice Design

從文字描述建立新的 Breeze 聲音。提供聲音的描述，以及讓它朗讀的一段句子；聲音會根據該預覽建立，並儲存到你的帳戶。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `description` | 以 3 至 500 個字元描述聲音：年齡、性別、口音、語調、語速。預設：空白。 | STRING | 是 | 3 至 500 個字元 |
| `preview_text` | 新聲音在預覽中朗讀的句子，最多 500 個字元。請以所選語言撰寫，因為聲音是根據此預覽建立的。預設：空白。 | STRING | 是 | 1 至 500 個字元 |
| `language` | 預覽文字的語言。英文與中文可使用任一模型；其他語言則使用 Breeze TTS 2 Multilingual。 | DYNAMIC_COMBO | 是 | 提供多個選項 |
| `strength` | 聲音與描述契合的程度。預設：4.0。 | FLOAT | 否 | 1.0 至 10.0（步進值：0.1） |
| `seed` | 控制節點是否重新執行；無論種子值為何，結果皆不具決定性。預設：42。 | INT | 否 | 0 至 2147483647 |

### Language "English" and "Chinese" 輸入

僅當 `language` 為 English 或 Chinese 時才會顯示。

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | `Breeze TTS 2` 或 `Breeze TTS 2 Multilingual`。預設：`"Breeze TTS 2"`。 | COMBO | 是 | `"Breeze TTS 2"`<br>`"Breeze TTS 2 Multilingual"` |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `voice` | 新的 Breeze 聲音，以描述內容命名。 | BREEZE_VOICE |
| `preview` | 所設計聲音的音訊預覽。 | AUDIO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BreezeVoiceDesign/zh-TW.md)

---
**Source fingerprint (SHA-256):** `5b0ea4ccd03e442972a71ec839be7b755f569686400e472967a09a956de0982f`
