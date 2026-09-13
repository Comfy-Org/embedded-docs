# LTXV 雙重 CFG 引導器

此節點為 LTXV-AV 模型建立一個引導取樣物件（CFG guider）。它會對封裝式 LTXV-AV 潛在空間中的視訊部分與音訊部分分別套用不同的引導強度，讓你獨立控制條件作用對每種模態的影響。若兩個強度值相等，或該潛在空間未包含獨立的視訊與音訊元件，則改用單一整體強度。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | 取樣時使用的模型。 | MODEL | 是 | - |
| `positive` | 正向條件，用以引導生成朝向的目標。 | CONDITIONING | 是 | - |
| `negative` | 負向條件，用以引導生成避開的方向。 | CONDITIONING | 是 | - |
| `video_cfg` | 套用於潛在空間視訊模態的引導強度（預設值：3.0）。 | FLOAT | 是 | 0.0 至 100.0 |
| `audio_cfg` | 套用於潛在空間音訊模態的引導強度（預設值：7.0）。 | FLOAT | 是 | 0.0 至 100.0 |

注意：當 `video_cfg` 與 `audio_cfg` 相等（或數值極為接近）時，引導器會以該數值作為整個潛在空間的單一 CFG 強度。若該潛在空間並非封裝式 LTXV-AV 潛在空間，則僅使用 `video_cfg` 的值。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `guider` | 設定完成的 CFG 引導器，可傳遞至取樣器節點。 | GUIDER |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVDualCFGGuider/zh-TW.md)

---
**Source fingerprint (SHA-256):** `8b5ea32d0e73ab4f9b9f053ac7513d621fcc047e1ff468b6d0b5dd2aa3ff791a`
