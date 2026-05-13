> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaConceptsNode/zh-TW.md)

此文件由 AI 生成。若發現任何錯誤或有改進建議，歡迎隨時貢獻！[在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaConceptsNode/en.md)

用於保存一個或多個攝影機概念，以配合 Luma 文字轉影片和 Luma 圖片轉影片節點使用。此節點允許您選擇最多四個攝影機概念，並可選擇性地將它們與現有的概念鏈結合。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `concept1` | STRING | 是 | 提供多個選項<br>包含「無」選項 | 從可用的 Luma 概念中選擇第一個攝影機概念 |
| `concept2` | STRING | 是 | 提供多個選項<br>包含「無」選項 | 從可用的 Luma 概念中選擇第二個攝影機概念 |
| `concept3` | STRING | 是 | 提供多個選項<br>包含「無」選項 | 從可用的 Luma 概念中選擇第三個攝影機概念 |
| `concept4` | STRING | 是 | 提供多個選項<br>包含「無」選項 | 從可用的 Luma 概念中選擇第四個攝影機概念 |
| `luma_concepts` | LUMA_CONCEPTS | 否 | 不適用 | 可選的攝影機概念，用於添加到此處選擇的概念中 |

**注意：** 如果您不想使用全部四個概念欄位，所有概念參數（`concept1` 到 `concept4`）都可以設為「無」。此節點會將任何提供的 `luma_concepts` 與所選概念合併，以建立一個組合的概念鏈。

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `luma_concepts` | LUMA_CONCEPTS | 包含所有所選概念的組合攝影機概念鏈 |

---
**Source fingerprint (SHA-256):** `d0e334104884eadab86987f188dff079e11ee4a3de05d2537d88fa9d2a30534a`
