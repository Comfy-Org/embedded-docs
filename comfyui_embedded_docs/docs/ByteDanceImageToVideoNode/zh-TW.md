# 字節跳動圖片轉影片

ByteDance Image to Video 節點會透過 API 使用 ByteDance 模型，根據輸入的圖片和文字提示來產生影片。它會採用一張起始圖片幀，並建立遵循所提供描述的影片序列。此節點提供各種自訂選項，包括影片解析度、長寬比、持續時間及其他生成參數。

**注意：** 此節點在原始碼中標記為已棄用。

**注意:** BytePlus 將於 2026 年 11 月 11 日停止提供 Seedance 1.5 Pro 模型，因此此節點不再提供該模型，使用該模型儲存的工作流程將無法運作。請改用 `seedance-1-0-pro-250528`、`seedance-1-0-pro-fast-251015` 或 [Seedance 2.5 合作夥伴節點](https://docs.comfy.org/zh-TW/tutorials/partner-nodes/bytedance/seedance-2-5)。

## 輸入

| 參數 | 描述 | 資料型別 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | 用於影片生成的 ByteDance 模型（預設值：`"seedance-1-0-pro-fast-251015"`）。 | COMBO | 是 | `"seedance-1-0-pro-250528"`<br>`"seedance-1-0-pro-fast-251015"` |
| `prompt` | 用於產生影片的文字提示。移除開頭和結尾的空白後，長度必須至少為 1 個字元。 | STRING | 是 | - |
| `image` | 要用作影片的第一幀。尺寸必須介於 300x300 與 6000x6000 像素之間，長寬比介於 0.4 與 2.5 之間。 | IMAGE | 是 | - |
| `resolution` | 輸出影片的解析度。 | COMBO | 是 | `"480p"`<br>`"720p"`<br>`"1080p"` |
| `aspect_ratio` | 輸出影片的長寬比。 | COMBO | 是 | `"adaptive"`<br>`"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"` |
| `duration` | 輸出影片的持續時間（秒），預設值為 5。 | INT | 是 | 3 - 12 |
| `seed` | 用於生成的隨機種子（預設值：0）。 | INT | 否 | 0 - 2147483647 |
| `camera_fixed` | 指定是否固定攝影機。平台會在你的提示詞末尾附加固定攝影機的指令，但不保證實際效果（預設值：False）。 | BOOLEAN | 否 | `False`<br>`True` |
| `watermark` | 是否在影片中加入「AI generated」浮水印（預設值：False）。 | BOOLEAN | 否 | `False`<br>`True` |
| `generate_audio` | 新增 AI 生成的音軌。其餘模型會忽略此輸入（預設值：False）。. | BOOLEAN | 否 | `False`<br>`True` |

**注意：** 提示詞中不得包含以下詞語（不區分大小寫）：`resolution`、`ratio`、`duration`、`seed`、`camerafixed`、`watermark`。這些參數會透過各自的專用輸入進行設定。

## 輸出

| 輸出名稱 | 描述 | 資料型別 |
|-------------|-------------|-----------|
| `output` | 根據輸入圖片和提示參數所產生的影片檔案。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceImageToVideoNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `a1841a368e625bd90583e0f0dbdc32369e6701a44cf985f01de8faa3d999b224`
