# HeyGen Voice 1.0 Instant Clone

使用 HeyGen 的 Voice 1.0 引擎，從單一說話者的錄音克隆聲音。此節點會上傳錄音、建立即時聲音克隆、等待 HeyGen 完成處理，並回傳 `voice_id`。將其連接到 HeyGen Voice 1.0 Text to Speech，或連接到 HeyGen Avatar Video 和 HeyGen Talking Photo 中的 `custom_voice_id`。建立克隆是免費的；系統會就您使用該聲音生成的語音收費。

**注意：** 此節點在原始碼中已標記為廢棄。請改用 HeyGen Voice 1.0 Instant Clone Text to Speech，在同一個節點中複製語音並朗讀文字。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `音訊` | 單一說話者的錄音。請使用至少 10 秒的清晰語音；僅會使用前 3 分鐘。 | AUDIO | 是 | N/A |
| `語言` | 錄音中使用的語言（預設："auto"）。 | COMBO | 是 | `"auto"`<br>多種語言預設 |
| `相似度` | 聲音與錄音的貼近程度（預設："max"）。 | COMBO | 是 | `"medium"`<br>`"high"`<br>`"extra_high"`<br>`"max"` |
| `移除背景雜訊` | 在克隆前清除錄音中的背景噪音（預設：True）。 | BOOLEAN | 是 | True<br>False |
| `種子` | 變更 `seed` 以再次克隆錄音；每次克隆的聲音都會略有不同（預設：42）。 | INT | 是 | 0 至 2147483647 |

**注意：** 該聲音會在您的 HeyGen 帳戶中建立為 "ComfyUI Voice"，且 `voice_id` 會出現在輸出中，連接文字顯示節點即可查看。除非說話者所說的語言容易與密切相關的語言混淆，否則請將 `language` 保持在 "auto"。`seed` 輸入在 UI 中包含固定的 Control After Generate 控制項，因此當您想要另一個克隆時，請手動變更它。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `voice_id` | 克隆聲音的 ID，可用於 HeyGen Voice 1.0 Text to Speech 節點，或作為 `custom_voice_id` 重複使用。 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenVoiceCloneNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `a44924942311ca520e8d77d89119cb56c1b8030124ce608ae89efd72a0e2ad28`
