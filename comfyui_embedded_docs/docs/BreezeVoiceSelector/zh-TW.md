# Breeze Voice Selector

選擇精選的 Breeze 語音，或任意 Breeze 語音 ID，並將其傳遞給 Breeze Text to Speech。此節點僅解析 ID，不會進行 API 呼叫。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `language` | 精選語音的語言群組，或使用 `custom` 以輸入 ID。預設：`"English"`。 | DYNAMIC_COMBO | 是 | `"English"`<br>`"Chinese"`<br>`"Japanese"`<br>`"custom"` |

### 語言 "English"、"Chinese" 和 "Japanese" 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `voice` | 該語言中的精選語音。 | COMBO | 是 | 提供多個選項 |

### 語言 "custom" 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `voice_id` | 任意 Breeze 語音 ID，例如由其他 Breeze 節點建立的語音。僅允許字母、數字、`_` 和 `-`。預設：空。 | STRING | 是 | Breeze 語音 ID |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `voice` | 所選的 Breeze 語音。 | BREEZE_VOICE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BreezeVoiceSelector/zh-TW.md)

---
**Source fingerprint (SHA-256):** `0bded8f1b6ec92abaec514ed843b3c138d804e3736758f5df3a2faf52e89a8b0`
