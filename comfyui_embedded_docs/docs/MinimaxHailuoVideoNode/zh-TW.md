# MiniMax 海螺影片

此節點使用 MiniMax Hailuo-02 模型從文字提示生成影片。您可以選擇性地提供一張起始影像作為第一幀，以建立從該影像延續的影片。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt_text` | 用於引導影片生成的文字提示。 | STRING | 是 | - |
| `seed` | 用於建立雜訊的隨機種子（預設值：0）。 | INT | 否 | 0 to 18446744073709551615 |
| `first_frame_image` | 可選影像，用作生成影片的第一幀。 | IMAGE | 否 | - |
| `prompt_optimizer` | 在需要時最佳化提示以提高生成品質（預設值：True）。 | BOOLEAN | 否 | - |
| `duration` | 輸出影片的長度（秒）（預設值：6）。 | COMBO | 否 | `6`<br>`10` |
| `resolution` | 影片顯示的尺寸。1080p 為 1920x1080，768p 為 1366x768（預設值："768P"）。 | COMBO | 否 | `"768P"`<br>`"1080P"` |

**注意事項：**
- 當未提供 `first_frame_image` 時，`prompt_text` 必須是非空字串。
- 使用 MiniMax-Hailuo-02 模型搭配 1080P 解析度時，持續時間限制為 6 秒。

## 輸出

| 輸出名 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `output` | 生成的影片檔案。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuoVideoNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `f371aae15cfbe7353236bc679c8a6d558703c5037e49ab7ddb9bdf5c50ef0995`
