# ElevenLabs 文字轉對話

ElevenLabs Text to Dialogue 節點可從文字生成多說話者音訊對話。它允許您透過指定不同的文字行和每個參與者的不同語音來建立對話。節點會將對話請求傳送至 ElevenLabs API，並回傳生成的音訊。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `穩定性` | 語音穩定性。較低的值提供更廣泛的情緒範圍，較高的值則產生更一致但可能單調的語音。（預設值：0.5） | FLOAT | 否 | 0.0 - 1.0 |
| `套用文字正規化` | 文字標準化模式。'auto' 讓系統自行決定，'on' 一律套用標準化，'off' 則跳過。 | COMBO | 否 | `"auto"`<br>`"on"`<br>`"off"` |
| `模型` | 用於對話生成的模型。 | COMBO | 否 | `"eleven_v3"` |
| `對話項目數` | 對話條目數量。選擇一個數字將生成相應數量的文字和語音輸入欄位。 | DYNAMIC_COMBO | 是 | `"1"`<br>`"2"`<br>`"3"`<br>`"4"`<br>`"5"`<br>`"6"`<br>`"7"`<br>`"8"`<br>`"9"`<br>`"10"` |
| `語言代碼` | ISO-639-1 或 ISO-639-3 語言代碼（例如 'en'、'es'、'fra'）。留空以自動偵測。（預設值：空） | STRING | 否 | - |
| `隨機種子` | 用於再現的隨機種子。（預設值：1） | INT | 否 | 0 - 4294967295 |
| `輸出格式` | 音訊輸出格式。 | COMBO | 否 | `"mp3_44100_192"`<br>`"opus_48000_192"` |

**注意：** `inputs` 參數是動態的。當您選擇一個數字（例如「3」）時，節點將顯示三個對應的 `text` 和 `voice` 輸入欄位（例如 `text1`、`voice1`、`text2`、`voice2`、`text3`、`voice3`）。每個 `text` 欄位至少須包含一個字元。每個 `voice` 欄位預期接收來自 Voice Selector 或 Instant Voice Clone 節點連接的語音。

## 輸出

| 輸出名 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `audio` | 以所選輸出格式生成的多說話者對話音訊。 | AUDIO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsTextToDialogue/zh-TW.md)

---
**Source fingerprint (SHA-256):** `95b16143391a2282c58ebc66561b85338a8ce1f87e0ec769405225599d2c76ae`
