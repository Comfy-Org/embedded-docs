> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsTextToDialogue/zh-TW.md)

此節點從文字生成多說話者的音訊對話。它允許您透過為每個參與者指定不同的文字行和獨特的聲音來創建對話。該節點將對話請求發送到 ElevenLabs API 並返回生成的音訊。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `stability` | FLOAT | 否 | 0.0 - 1.0 | 聲音穩定性。較低的值提供更廣泛的情感範圍，較高的值產生更一致但可能單調的語音。(預設值: 0.5) |
| `apply_text_normalization` | COMBO | 否 | `"auto"`<br>`"on"`<br>`"off"` | 文字正規化模式。'auto' 讓系統決定，'on' 總是套用正規化，'off' 則跳過。 |
| `model` | COMBO | 否 | `"eleven_v3"` | 用於對話生成的模型。 |
| `inputs` | DYNAMICCOMBO | 是 | `"1"`<br>`"2"`<br>`"3"`<br>`"4"`<br>`"5"`<br>`"6"`<br>`"7"`<br>`"8"`<br>`"9"`<br>`"10"` | 對話條目的數量。選擇一個數字將生成相應數量的文字和聲音輸入欄位。 |
| `language_code` | STRING | 否 | - | ISO-639-1 或 ISO-639-3 語言代碼 (例如 'en', 'es', 'fra')。留空則自動偵測。(預設值: 空) |
| `seed` | INT | 否 | 0 - 4294967295 | 用於重現性的種子值。(預設值: 1) |
| `output_format` | COMBO | 否 | `"mp3_44100_192"`<br>`"opus_48000_192"` | 音訊輸出格式。 |

**注意：** `inputs` 參數是動態的。當您選擇一個數字 (例如 "3") 時，節點將顯示三個對應的 `text` 和 `voice` 輸入欄位 (例如 `text1`, `voice1`, `text2`, `voice2`, `text3`, `voice3`)。每個 `text` 欄位必須至少包含一個字元。

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `audio` | AUDIO | 以所選輸出格式生成的多說話者對話音訊。 |