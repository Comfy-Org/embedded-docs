# HeyGenVideoTranslateNode

將一段含語音的影片翻譯成另一種語言，並進行語音克隆與唇形同步。此節點會克隆原始說話者的聲音，並重新動畫化嘴部動作以匹配翻譯後的語音，產生自然逼真的效果。

## 輸入
| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `video` | 含有待翻譯語音的影片。 | VIDEO | 是 | - |
| `output_language` | 翻譯後影片的目標語言。 | STRING | 是 | "Arabic"<br>"Bengali"<br>"Chinese"<br>"Danish"<br>"Dutch"<br>"English"<br>"French"<br>"German"<br>"Greek"<br>"Hindi"<br>"Indonesian"<br>"Italian"<br>"Japanese"<br>"Korean"<br>"Malay"<br>"Polish"<br>"Portuguese"<br>"Russian"<br>"Spanish"<br>"Swedish"<br>"Tamil"<br>"Telugu"<br>"Thai"<br>"Turkish"<br>"Ukrainian"<br>"Vietnamese" |
| `mode` | 'speed' 模式速度較快；'precision' 模式可產生更高品質的唇形同步，但成本為兩倍。 | STRING | 是 | "speed"<br>"precision" |
| `translate_audio_only` | 僅更換音軌，保留原始嘴部動作（不進行唇形同步）。（預設值：False） | BOOLEAN | 否 | True<br>False |
| `speaker_count` | 影片中的說話者人數。0 = 自動偵測。（預設值：0） | INT | 否 | 0 至 10 |
| `seed` | 不會發送至 HeyGen；變更此值可強制重新執行。（預設值：42） | INT | 否 | 0 至 2147483647 |

## 輸出
| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `video` | 經過語音克隆與唇形同步處理後的翻譯影片。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenVideoTranslateNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `31056060b6309b8ec28b37b353322403e173fd2862b56021392dba24e7a15f69`
