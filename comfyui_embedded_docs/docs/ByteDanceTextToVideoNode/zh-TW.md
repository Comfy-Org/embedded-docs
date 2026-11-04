# 字節跳動文字轉影片

ByteDance Text to Video 節點會透過 API 使用 ByteDance 模型，根據文字提示生成影片。您可提供提示詞，並選擇模型、解析度、長寬比與時長等設定；節點會提交生成請求，並傳回生成的影片。

**注意:** BytePlus 將於 2026 年 11 月 11 日停止提供 Seedance 1.5 Pro 模型，因此此節點不再提供該模型，使用該模型儲存的工作流程將無法運作。請改用 `seedance-1-0-pro-250528`、`seedance-1-0-pro-fast-251015` 或 [Seedance 2.5 合作夥伴節點](https://docs.comfy.org/zh-TW/tutorials/partner-nodes/bytedance/seedance-2-5)。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `模型` | 用於生成影片的 ByteDance 模型（預設：`"seedance-1-0-pro-fast-251015"`）。 | COMBO | 是 | `"seedance-1-0-pro-250528"`<br>`"seedance-1-0-pro-fast-251015"` |
| `提示詞` | 用於生成影片的文字提示。 | STRING | 是 | - |
| `解析度` | 輸出影片的解析度。 | COMBO | 是 | `"480p"`<br>`"720p"`<br>`"1080p"` |
| `長寬比` | 輸出影片的長寬比。 | COMBO | 是 | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"` |
| `持續時間` | 輸出影片的時長（秒）（預設：5）。 | INT | 是 | 3至12 |
| `種子值` | 用於生成的種子（預設：0）。 | INT | 否 | 0至2147483647 |
| `固定攝影機` | 指定是否固定相機。平台會將固定相機的指令附加到您的提示詞，但不保證實際效果（預設：False）。 | BOOLEAN | 否 | - |
| `浮水印` | 是否在影片中加入「AI generated」浮水印（預設：False）。 | BOOLEAN | 否 | - |
| `generate_audio` | 新增 AI 生成的音軌。其餘模型會忽略此輸入（預設：False）。. | BOOLEAN | 否 | - |

**參數約束：**

- `prompt` 參數在移除空白字元後，必須至少包含 1 個字元。
- `prompt` 參數不能包含下列文字參數："resolution"、"ratio"、"duration"、"seed"、"camerafixed"、"watermark"。
- 節點會將選定的 `resolution`、`aspect_ratio`、`duration`、`seed`、`camera_fixed` 與 `watermark` 設定附加到提示詞，以建構最終提示詞。
- `duration` 參數限制在 3 到 12 秒之間。
- `seed` 參數接受 0 到 2,147,483,647 之間的值。
- `generate_audio` 參數為相容性而保留，但其餘模型會忽略它。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-----------|-------------|-----------|
| `output` | 生成的影片檔案 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceTextToVideoNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `83b805b63e59a76cae378b0407b409e1bfe900677ef1e01fc836fede47283eee`
