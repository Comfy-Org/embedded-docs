> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokVideoReferenceNode/zh-TW.md)

## 概述

Grok 參考轉影片節點會根據文字提示生成影片，並使用最多七張參考影像來引導輸出內容的風格與樣貌。此節點會連接到外部 API 來建立影片，隨後下載並回傳該影片。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | 是 | 不適用 | 對所需影片的文字描述。 |
| `model` | COMBO | 是 | `"grok-imagine-video"` | 用於影片生成的模型。 |
| `model.reference_images` | IMAGE | 是 | 1 至 7 張影像 | 最多 7 張參考影像，用於引導影片生成。 |
| `model.resolution` | COMBO | 是 | `"480p"`<br>`"720p"` | 輸出影片的解析度。 |
| `model.aspect_ratio` | COMBO | 是 | `"16:9"`<br>`"4:3"`<br>`"3:2"`<br>`"1:1"`<br>`"2:3"`<br>`"3:4"`<br>`"9:16"` | 輸出影片的長寬比。 |
| `model.duration` | INT | 是 | 2 至 10 | 輸出影片的持續時間（秒），預設值為 6。 |
| `seed` | INT | 否 | 0 至 2147483647 | 用於決定節點是否應重新執行的種子；實際結果無論種子為何皆為非確定性，預設值為 0。 |

**注意：** `model` 參數是一個群組，包含 `reference_images`、`resolution`、`aspect_ratio` 和 `duration`。您必須提供至少一張參考影像，最多可提供七張。

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `video` | VIDEO | 生成的影片檔案。 |

---
**Source fingerprint (SHA-256):** `e368769b869b7a0d0be8e6fdcc2b82774c11805483b2e83a448b6985a6dd9f96`
