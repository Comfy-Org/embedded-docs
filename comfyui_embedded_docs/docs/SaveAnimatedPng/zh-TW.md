# SaveAnimatedPNG 節點

SaveAnimatedPNG 節點專為從一系列影格建立和儲存動畫 PNG 影像而設計。它負責將單獨的影像影格組合成連貫的動畫，並允許自訂影格持續時間、循環播放和中繼資料包含。

## 輸入

| 欄位 | 說明 | 資料類型 |
| --- | --- | --- |
| `images` | 要處理並儲存為動畫 PNG 的影像列表。列表中的每個影像代表動畫中的一個影格。 | `IMAGE` |
| `檔名前綴` | 指定輸出檔案的基本名稱，將用作產生的動畫 PNG 檔案的前綴。 | `STRING` |
| `每秒影格數` | 動畫的每秒影格數，控制影格顯示的速度。 | `FLOAT` |
| `壓縮等級` | 應用於動畫 PNG 檔案的壓縮級別，影響檔案大小和影像清晰度。 | `INT` |

## 輸出

| 欄位 | 說明 | 資料類型 |
| --- | --- | --- |
| `images` | 提供一個 UI 元件，顯示產生的動畫 PNG 影像，並指示動畫是單影格還是多影格。 | N/A |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAnimatedPNG/zh-TW.md)
