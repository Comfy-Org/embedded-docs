# Kling 文字轉影片（含音訊）

Kling Text to Video with Audio 節點會根據文字描述生成短影片。它會向 Kling AI 服務傳送請求，該服務會處理提示詞並傳回影片檔案。此節點也可以根據文字為影片生成伴隨音訊。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model_name` | 用於影片生成的特定 AI 模型。 | COMBO | 是 | `"kling-v2-6"` |
| `提示詞` | 正向文字提示詞。用於生成影片的描述。長度必須介於 1 到 2500 個字元之間。 | STRING | 是 | - |
| `模式` | 影片生成的運作模式。 | COMBO | 是 | `"pro"` |
| `長寬比` | 生成影片所需的寬高比。 | COMBO | 是 | `"16:9"`<br>`"9:16"`<br>`"1:1"` |
| `時長` | 影片長度，以秒為單位。 | COMBO | 是 | `5`<br>`10` |
| `生成音訊` | 控制是否為影片生成音訊。啟用時，AI 會根據提示詞建立聲音（預設：`True`）。 | BOOLEAN | 否 | - |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `output` | 生成的影片檔案。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingTextToVideoWithAudio/zh-TW.md)

---
**Source fingerprint (SHA-256):** `ddd2f3c1799abac067a05f3f5d6442ad4fe023d2f4f9afbde2894ca66854977e`
