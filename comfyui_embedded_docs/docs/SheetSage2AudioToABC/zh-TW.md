# SheetSage2 音訊轉 ABC

此節點會將音樂中的歌聲與樂器旋律轉錄為 ABC 記譜法，這是一種以文字記錄樂譜的格式。它會分析連接的音訊，並將產生的記譜以文字形式回傳，之後可搭配對應模式輸入到 YuE2 Generate Music 節點。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `audio_encoder` | 用於分析音訊並產生 ABC 記譜的音訊編碼器模型。 | AUDIO_ENCODER | 是 | - |
| `audio` | 要轉錄為 ABC 記譜的音樂音訊。 | AUDIO | 是 | - |
| `mode` | 控制要轉錄的內容。`"full"` 會產生旋律與和弦；`"melody"` 只產生旋律，建議用於翻唱。 | COMBO | 是 | `"melody"`<br>`"full"` |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `abc` | 以 ABC 記譜法轉錄的音樂，以字串列表形式回傳。請將其連接到 YuE2 Generate Music 節點，並使用對應模式。 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SheetSage2AudioToABC/zh-TW.md)

---
**Source fingerprint (SHA-256):** `612d18dedd09b64210087c340b8f304ace8cd7b30b1a6e8e8ba7c749b355a497`
