# Vidu2 圖像轉影片生成

Vidu2 圖片轉影片生成節點可從單張輸入圖片建立影片序列。它使用指定的 Vidu2 模型，根據可選的文字提示來為場景製作動畫，並控制影片的長度、解析度以及動作強度。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 用於影片生成的 Vidu2 模型。不同模型在速度與品質之間提供不同的權衡取捨。 | COMBO | 是 | `"viduq2-pro-fast"`<br>`"viduq2-pro"`<br>`"viduq2-turbo"` |
| `image` | 用作生成影片起始幀的圖片。僅允許一張圖片。 | IMAGE | 是 | - |
| `prompt` | 用於影片生成的可選文字提示（最多 2000 個字元）。預設為空字串。 | STRING | 否 | - |
| `duration` | 生成影片的長度，以秒為單位。預設為 5。 | INT | 是 | 1 到 10 |
| `seed` | 用於隨機數生成的種子值，以確保結果可重現。預設為 1。 | INT | 否 | 0 到 2147483647 |
| `resolution` | 生成影片的輸出解析度。此參數為進階設定。 | COMBO | 是 | `"720p"`<br>`"1080p"` |
| `movement_amplitude` | 畫面中物體的移動幅度。此參數為進階設定。 | COMBO | 是 | `"auto"`<br>`"small"`<br>`"medium"`<br>`"large"` |

**限制條件：**

* `image` 輸入必須恰好包含一張圖片。
* 輸入圖片的長寬比必須介於 1:4 與 4:1 之間。
* `prompt` 文字最多限制為 2000 個字元。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `output` | 生成的影片檔案。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu2ImageToVideoNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `204f8d2b9edf17c2c180480f98a852718416a54725d92e5fec574b8517ada398`
