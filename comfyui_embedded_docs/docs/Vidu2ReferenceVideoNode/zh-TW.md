# Vidu2 參考影片生成節點

Vidu2 參考轉影片生成節點可根據文字提示和多張參考圖片建立影片。您可以定義最多七個主體，每個主體都有自己的一組參考圖片，並在提示中使用 `@subject{subject_id}` 來引用它們。此節點可產生具有可配置時長、長寬比和動態效果的影片。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 用於影片生成的 AI 模型。 | COMBO | 是 | `"viduq2"` |
| `subjects` | 為每個主體提供最多 3 張參考圖片（所有主體總共 7 張圖片）。透過 `@subject{subject_id}` 在提示中引用它們。 | AUTOGROW | 是 | 不適用 |
| `prompt` | 用於引導影片生成的文字描述。當啟用 `audio` 參數時，影片將包含根據此提示生成的語音和背景音樂。 | STRING | 是 | 不適用 |
| `audio` | 啟用時，影片將包含根據提示生成的語音和背景音樂（預設值：`False`）。 | BOOLEAN | 否 | 不適用 |
| `duration` | 生成影片的長度，以秒為單位（預設值：`5`）。 | INT | 否 | 1 到 10 |
| `seed` | 用於控制生成隨機性的數字，以獲得可重現的結果（預設值：`1`）。 | INT | 否 | 0 到 2147483647 |
| `aspect_ratio` | 影片畫面的形狀。 | COMBO | 否 | `"16:9"`<br>`"9:16"`<br>`"4:3"`<br>`"3:4"`<br>`"1:1"` |
| `resolution` | 輸出影片的像素解析度。 | COMBO | 否 | `"720p"`<br>`"1080p"` |
| `movement_amplitude` | 控制畫面中物體的動態幅度。 | COMBO | 否 | `"auto"`<br>`"small"`<br>`"medium"`<br>`"large"` |

**限制條件：**

* `prompt` 的長度必須在 1 到 2000 個字元之間。
* 您可以定義多個主體，但所有主體的參考圖片總數不得超過 7 張。
* 每個個別主體最多可以有 3 張參考圖片。
* 每張參考圖片的寬高比必須在 1:4 到 4:1 之間。
* 每張參考圖片的寬度和高度都必須至少為 128 像素。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `output` | 生成的影片檔案。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu2ReferenceVideoNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `3e02b05a0e374442a6ca4ce6a3dbc182b4059e19b5ed7dfc2794e036de7beffd`
