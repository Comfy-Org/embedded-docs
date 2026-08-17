# LTXV 文字轉影片

LTXV Text To Video 節點可根據文字描述生成專業品質的影片。此節點連接到外部 API，以建立可自訂持續時間、解析度和幀率的影片。您也可以選擇加入 AI 生成的音訊。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 用於影片生成的 AI 模型。"LTX-2 (Pro)" 提供較高品質，而 "LTX-2 (Fast)" 則針對速度最佳化。 | COMBO | 是 | `"LTX-2 (Pro)"`<br>`"LTX-2 (Fast)"` |
| `prompt` | AI 用來生成影片的文字描述。此欄位支援多行文字。 | STRING | 是 | - |
| `duration` | 生成影片的長度（秒）（預設：8）。 | COMBO | 是 | `6`<br>`8`<br>`10`<br>`12`<br>`14`<br>`16`<br>`18`<br>`20` |
| `resolution` | 輸出影片的像素尺寸（寬度 x 高度）。 | COMBO | 是 | `"1920x1080"`<br>`"2560x1440"`<br>`"3840x2160"` |
| `fps` | 影片的每秒幀數（預設：25）。 | COMBO | 是 | `25`<br>`50` |
| `generate_audio` | 設定為 true 時，生成的影片將包含與場景匹配的 AI 生成音訊（預設：False）。 | BOOLEAN | 否 | `True`<br>`False` |

**重要限制：**

* `prompt` 的長度必須介於 1 到 10,000 個字元之間。
* 如果您選擇的 `duration` 大於 10 秒，則也必須使用 `"LTX-2 (Fast)"` 模型、`"1920x1080"` 解析度以及 `fps` 為 `25`。這是較長影片所必需的組合。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `output` | 生成的影片檔案。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LtxvApiTextToVideo/zh-TW.md)

---
**Source fingerprint (SHA-256):** `8cf7409e46bb92abdff8a12e0d4ab49d67bb70e66c0c9074c9af99d1cf250df8`
