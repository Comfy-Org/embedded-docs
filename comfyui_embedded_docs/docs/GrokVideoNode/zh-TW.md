# Grok 影片

Grok Video 節點會根據文字描述生成短影片。它可以使用提示從頭建立影片，或從單一輸入影像生成影片。此節點會將請求傳送至外部 API，並傳回生成的影片。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | 用於影片生成的模型（預設：`"grok-imagine-video-1.5-lite"`）。 | COMBO | 是 | `"grok-imagine-video"`<br>`"grok-imagine-video-1.5"`<br>`"grok-imagine-video-1.5-lite"` |
| `prompt` | 所需影片的文字描述。當提供輸入影像時，`grok-imagine-video-1.5` 模型可省略此項。 | STRING | 是 | - |
| `resolution` | 輸出影片的解析度。`grok-imagine-video` 不支援 `1080p`。 | COMBO | 是 | `"480p"`<br>`"720p"`<br>`"1080p"` |
| `aspect_ratio` | 輸出影片的長寬比。當提供輸入影像時會忽略此項；影片會遵循影像的長寬比。 | COMBO | 是 | `"auto"`<br>`"16:9"`<br>`"4:3"`<br>`"3:2"`<br>`"1:1"`<br>`"2:3"`<br>`"3:4"`<br>`"9:16"` |
| `duration` | 輸出影片的長度，以秒為單位（預設：6）。 | INT | 是 | 1 至 15 |
| `seed` | 用於決定節點是否應重新執行的種子；無論種子為何，實際結果皆不具確定性（預設：0）。 | INT | 是 | 0 至 2147483647 |
| `image` | 選填的起始影像。若省略，則僅根據文字提示生成影片。 | IMAGE | 否 | - |

**注意：** 當提供 `image` 時，僅支援一張輸入影像；提供多張影像會導致錯誤。未提供影像時，或使用 `grok-imagine-video` 時（即使有提供影像），`prompt` 在移除空白字元後必須為非空。對於 `grok-imagine-video-1.5` 模型，只有在提供輸入影像時，`prompt` 才是選填。`grok-imagine-video` 不支援 `1080p` 解析度。當 `aspect_ratio` 設為 `"auto"` 時，長寬比會由服務自動選擇；當提供輸入影像時，會忽略 `aspect_ratio`，影片會遵循影像的長寬比。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `output` | 生成的影片。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokVideoNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `ed5a1c39598a319d5b350b19f39a352dedd1150471695d25f7637fc0f8735d02`
