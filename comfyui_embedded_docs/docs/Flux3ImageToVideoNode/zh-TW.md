# Flux3ImageToVideoNode

Flux 3 Image to Video 使用 FLUX 3 將 1 到 10 張圖片動畫化。每張圖片成為影片片段的一個影格：一張圖片開啟片段，兩張圖片從第一張過渡到第二張，更多圖片則均勻分布在片段中或固定在你選擇的時間點。

## 輸入

| 參數 | 描述 | 資料型別 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 場景應如何移動和發聲；提示詞在生成前會被解讀並擴展。必須至少包含一個字元。 | STRING | 是 | 多行文字（預設：空） |
| `keyframes` | 1 到 10 張圖片，按播放順序排列。每張至少 256x256 像素。每個關鍵影格成為影片片段中的一個點。 | IMAGE | 是 | 1 到 10 張圖片 |
| `placement` | 'spread across the clip' 讓 FLUX 3 放置圖片（一張開啟片段，兩張成為片段的開頭和結尾）；'at times' 將每張圖片固定在你選擇的秒數。 | STRING | 是 | `"spread across the clip"`（預設）<br>`"at times"` |
| `times` | 每張圖片對應一個以秒為單位的時間，以逗號分隔且遞增，例如 '0, 2.5, 5'。當 `placement` 為 `"at times"` 時必填。 | STRING | 否 | 逗號分隔的秒數（預設："0"） |
| `aspect_ratio` | 輸出的長寬比。'auto' 會根據提示詞和輸入自動選擇。 | STRING | 是 | `"auto"`（預設）<br>以及其他可用選項 |
| `duration` | 影片片段的長度（秒）。'auto' 會根據內容調整長度。 | STRING | 是 | `"auto"`（預設）<br>以及其他可用選項 |
| `resolution` | 輸出解析度。 | STRING | 是 | `"720p"`（預設）<br>`"1080p"` |
| `generate_audio` | 生成同步音訊（環境音、語音、特效）。關閉（Off）將產生沒有音軌的影片。 | BOOLEAN | 是 | true / false（預設：true） |
| `safety_tolerance` | 審核容忍度，0 為最嚴格。無論你在此設定什麼值，發送圖片或影片的請求都會被限制為 2。 | INT | 是 | 0 到 4（預設：2，進階設定） |
| `seed` | 決定節點是否應重新執行的種子值；FLUX 3 會自行選擇種子，因此無論此值為何，實際結果都是不確定的。 | INT | 是 | 0 到 4294967295（預設：42，具有生成後控制） |

注意：`keyframes` 為必填項 — 如果未連接任何關鍵影格圖片，節點將產生錯誤。當 `placement` 為 `"spread across the clip"` 且提供了 3 張或更多圖片時，`duration` 必須設定為明確的值（不能是 `"auto"`）；否則節點將產生錯誤。當 `placement` 為 `"at times"` 時，`times` 必須為每張圖片提供一個以秒為單位的遞增時間。發送圖片的請求無論設定為何值，其安全容忍度上限皆為 2。

## 輸出

| 輸出名稱 | 描述 | 資料型別 |
|-------------|-------------|-----------|
| `video` | 根據所選的長寬比、長度、解析度和音訊設定，由關鍵影格圖片生成的影片片段。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux3ImageToVideoNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `3b9472194020ec98cd4e8c60463cdd0e9dc074ec6cbc1fc03d313894fa570ba8`
