# ComfyCloudZImageTurboNode

此節點使用 Z-Image Turbo 模型從文字提示生成圖像，僅需 8 個步驟即可完成。生成過程在 Comfy Cloud GPU 上遠端執行，並按 GPU 時間計費，使其成為此處用於迭代圖像創意的最快速且最便宜的選項之一。生成完成後，節點會下載完成的圖像以供工作流程使用。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 描述要生成圖像的文字提示。接受多行輸入，並在提交前去除前後空白。去除空白後不得為空。 | STRING | 是 | 1 - 4096 characters |
| `seed` | 用於控制生成可重現性的隨機種子。更改它會產生不同的變體。包含「生成後控制」選項。預設值：42。 | INT | 否 | 0 - 18446744073709551615 |
| `aspect_ratio` | 生成圖像的長寬比。預設值："1:1"。 | COMBO | 否 | "1:1"<br>"3:4"<br>"2:3"<br>"3:2"<br>"4:3"<br>"16:9"<br>"9:16"<br>"21:9" |
| `megapixels` | 總像素預算。在正方形比例下，1.0 約為 1024x1024。預設值：1.0。 | FLOAT | 否 | 0.1 - 16.0<br>(step of 0.1) |

注意：輸入值在提交生成前會進行驗證。`prompt` 在去除空白後必須包含 1 至 4,096 個字元，`aspect_ratio` 必須是所列選項之一，且 `megapixels` 必須以 0.1 的增量輸入。

## 輸出

| 輸出名 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `IMAGE` | 生成的圖像以圖像張量形式返回，可用於進一步的圖像處理或保存節點。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyCloudZImageTurboNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `9c78bf9aca5800212d1c5a8f9581dc6c154a82220cd60a8b55ebe74111d2f542`
