# LTXVDualCFGGuider

此節點為 LTXV-AV 模型建立一個引導取樣物件（CFG guider）。它會對打包後的潛在表示（packed latent）中的影片部分與音訊部分分別套用不同的引導比例，讓您能獨立控制每個模態受條件作用的影響程度。若兩個比例相等，或潛在表示中不包含獨立的影片與音訊元件，則會使用單一的整體比例。

## Inputs

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `model` | 取樣時使用的模型。 | MODEL | 是 | - |
| `positive` | 正向條件作用，用於引導生成朝向此方向。 | CONDITIONING | 是 | - |
| `negative` | 負向條件作用，用於引導生成遠離此方向。 | CONDITIONING | 是 | - |
| `video_cfg` | 套用於潛在表示影片模態的引導強度（預設：3.0）。 | FLOAT | 是 | 0.0 至 100.0 |
| `audio_cfg` | 套用於潛在表示音訊模態的引導強度（預設：7.0）。 | FLOAT | 是 | 0.0 至 100.0 |

注意：當 `video_cfg` 與 `audio_cfg` 數值相同時，guider 會將該值作為整個潛在表示的單一 CFG 比例。若潛在表示不是打包的 LTXV-AV 潛在表示，則僅使用 `video_cfg` 的值。

## Outputs

| Output Name | Description | Data Type |
|-------------|-------------|-----------|
| `guider` | 已設定的 CFG guider，用於傳遞給取樣器節點。 | GUIDER |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVDualCFGGuider/zh-TW.md)

---
**Source fingerprint (SHA-256):** `8b5ea32d0e73ab4f9b9f053ac7513d621fcc047e1ff468b6d0b5dd2aa3ff791a`
