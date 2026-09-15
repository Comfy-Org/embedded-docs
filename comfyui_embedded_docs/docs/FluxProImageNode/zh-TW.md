# FluxProImageNode

根據 `prompt` 與解析度同步生成圖像。此節點使用 Flux 1.1 Pro 模型，透過向 API 端點傳送請求並等待完整回應後，再傳回生成的圖像。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `prompt` | 用於圖像生成的提示詞（預設：空字串） | STRING | 是 | - |
| `prompt_upsampling` | 是否對 `prompt` 執行上採樣。若啟用，會自動修改 `prompt` 以進行更具創意的生成，但結果為非確定性（相同的 `seed` 不會產生完全相同的結果）。（預設：False） | BOOLEAN | 是 | - |
| `width` | 圖像寬度，單位為像素（預設：1024，步長：32） | INT | 是 | 256-1440 |
| `height` | 圖像高度，單位為像素（預設：768，步長：32） | INT | 是 | 256-1440 |
| `seed` | 用於建立雜訊的隨機種子。（預設：0） | INT | 是 | 0-18446744073709551615 |
| `image_prompt` | 選用的參考圖像，用於引導生成 | IMAGE | 否 | - |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `output` | 從 API 傳回的生成圖像 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxProImageNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `89316d84f364854541157b5b60bae3d4e25024bd4af61a47a1748c6671b463c1`
