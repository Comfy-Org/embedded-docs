# ByteDance Seedance 2.0 參考影片節點

ByteDance Seedance 2.0 參考影片節點使用 Seedance 2.0 AI 模型，根據您的文字提示和提供的參考素材來建立、編輯或延伸影片。它可以將圖片、影片和音訊作為參考來引導生成過程，支援影片編輯和延伸等任務。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `模型` | 要使用的 AI 模型。Seedance 2.0 提供最高品質，而 Seedance 2.0 Fast 則針對速度進行最佳化。選擇模型後會顯示 `prompt`、`resolution`、`duration`、`ratio`、`generate_audio` 的額外必要輸入，以及 `reference_images`、`reference_videos`、`reference_audios`、`reference_assets` 和 `auto_downscale` 的選用輸入。 | COMBO | 是 | `"Seedance 2.0"`<br>`"Seedance 2.0 Fast"` |
| `種子` | 用於控制節點是否應重新執行的數值。無論種子值為何，結果都非確定性（預設值：0）。 | INT | 否 | 0 到 2147483647 |
| `浮水印` | 是否在生成的影片中添加浮水印（預設值：False）。 | BOOLEAN | 否 | `True` / `False` |

**重要限制：**
*   節點運作需要至少一張參考圖片或一部參考影片（透過 `reference_images`、`reference_videos` 或 `reference_assets` 輸入提供）。
*   總共最多可使用 9 張參考圖片（包括來自 `reference_images` 和 `reference_assets` 的圖片）。
*   總共最多可使用 3 部參考影片（包括來自 `reference_videos` 和 `reference_assets` 的影片）。
*   總共最多可使用 3 個參考音訊片段（包括來自 `reference_audios` 和 `reference_assets` 的音訊）。
*   每部參考影片的長度必須至少 1.8 秒。所有參考影片的總時長不得超過 15.1 秒。
*   每個參考音訊片段的長度必須至少 1.8 秒。所有參考音訊的總時長不得超過 15.1 秒。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `video` | 生成的影片檔案。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2ReferenceNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `72c8a2f821b9fb9853a4d0428785c432d0852ae562080292817f8a7d52967c7f`
