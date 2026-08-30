# HeyGen 影片翻譯

使用語音克隆和唇形同步，將有語音的影片翻譯成另一種語言。此節點會複製原始說話者的聲音，並重新調整嘴型以配合翻譯後的語音，呈現自然的效果。

## 輸入

| 參數 | 說明 | 資料型別 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `影片` | 含有要翻譯語音的影片。 | VIDEO | 是 | - |
| `目標語言` | 翻譯後影片的目標語言。 | COMBO | 是 | "Arabic"<br>"Bengali"<br>"Chinese"<br>"Danish"<br>"Dutch"<br>"English"<br>"French"<br>"German"<br>"Greek"<br>"Hindi"<br>"Indonesian"<br>"Italian"<br>"Japanese"<br>"Korean"<br>"Malay"<br>"Polish"<br>"Portuguese"<br>"Russian"<br>"Spanish"<br>"Swedish"<br>"Tamil"<br>"Telugu"<br>"Thai"<br>"Turkish"<br>"Ukrainian"<br>"Vietnamese" |
| `模式` | 'speed' 速度較快；'precision' 以較高成本產生更高品質的唇形同步。（預設值："speed"） | COMBO | 是 | "speed"<br>"precision" |
| `僅翻譯音訊` | 僅替換音軌，保留原始嘴部動作（不進行唇形同步）。（預設值：False） | BOOLEAN | 否 | True<br>False |
| `說話者數量` | 影片中的說話者人數。0 = 自動偵測。高於 0 的值會作為說話者人數傳送到 API。（預設值：0） | INT | 否 | 0 至 10 |
| `隨機種子` | 不會傳送至 HeyGen；變更此值以強制重新執行。（預設值：42） | INT | 否 | 0 至 2147483647 |

## 輸出

| 輸出名稱 | 說明 | 資料型別 |
|-------------|-------------|-----------|
| `video` | 已套用語音克隆和唇形同步的翻譯後影片。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenVideoTranslateNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `709438c0c713d6db750643cc48f75352c6f293ae1ff2fd82c1bacb03b2581923`
