# SyncTalkingImageNode

將靜態肖像動畫化為由語音音訊驅動的對話影片，使用 sync.so 的 sync-3 模型。輸出時長與音訊時長相符，費用隨輸出時長增加。

## 輸入
| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `image` | 一張清晰可見臉部的單張圖片，最高支援 4K (4096x2160)。 | IMAGE | 是 | 恰好需要一張圖片 |
| `audio` | 驅動對話影片的語音音訊；輸出時長與其相符。在此鏈接任何 TTS 節點，即可從文字驅動動畫。 | AUDIO | 是 | 最大時長：600 秒 |
| `prompt` | 可選的引導提示，用於控制肖像如何生動呈現，例如「讓主體微笑並看向鏡頭」。留空則產生自然的說話動作。（預設值：""） | STRING | 否 | 多行文字 |
| `seed` | 種子控制節點是否應重新執行；無論種子為何，結果均不具確定性。（預設值：0） | INT | 否 | 0 至 2147483647 |
| `model` | sync.so 生成模型。圖片輸入僅限於 sync-3。 | COMBO | 是 | `"sync-3"` |
| `speaker_selection` | 當畫面中有多人時，選擇要動畫化的臉部。`default`：讓模型決定。`coordinates`：定位圖片中像素座標 (speaker_x, speaker_y) 處的臉部。圖片不支援自動偵測。（預設值："default"） | COMBO | 否 | `"default"`<br>`"coordinates"` |
| `speaker_x` | 說話者臉部的 X 像素座標。僅在 speaker_selection 設為 'coordinates' 時使用。（預設值：0） | INT | 否 | 0 至 4096 |
| `speaker_y` | 說話者臉部的 Y 像素座標。僅在 speaker_selection 設為 'coordinates' 時使用。（預設值：0） | INT | 否 | 0 至 4096 |
| `auto_downscale` | 當圖片超過 4K (4096x2160) 輸入限制時自動縮小；說話者座標會相應縮放。停用時，超尺寸圖片會引發錯誤。（預設值：True） | BOOLEAN | 否 | True<br>False |

**注意：** `speaker_x` 和 `speaker_y` 參數僅在 `speaker_selection` 設為 `"coordinates"` 時使用。啟用 `auto_downscale` 時，說話者座標會自動縮放以匹配縮小後的圖片尺寸。

## 輸出
| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `video` | 生成的對話影片，動畫肖像與輸入音訊同步。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SyncTalkingImageNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `21f722cdcc5ff017949887ed2252854feebb9b913034dc6a6c3ce196ad089468`
