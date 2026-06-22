# LumaRay32KeyframeNode

此節點將引導圖像錨定到 Luma Ray 3.2 輸出影片時間軸上的特定位置。將此節點連接到 Luma Ray 3.2 Keyframes to Video 節點的 `keyframes` 輸入，並透過連接可選的 `keyframes` 輸入來將多個關鍵影格串聯在一起。

## ## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|------|------|---------|------|------|
| `image` | 放置在輸出影片所選時刻的引導圖像。 | IMAGE | 是 | - |
| `position` | 如何將此圖像放置在輸出影片的時間軸上。 | COMBO | 是 | "Fraction of duration (0.0-1.0)"<br>"Absolute time (seconds)" |
| `keyframes` | 可選的先前關鍵影格，用於與此關鍵影格串聯。 | LUMA_RAY32_KEYFRAME | 否 | - |

當為 `position` 參數選擇「Fraction of duration (0.0-1.0)」時，您可以指定一個 `fraction` 值（預設值：0.0，範圍：0.0 至 1.0，步長：0.01），該值決定此圖像在輸出影片中的應用位置（0.0 = 開頭，1.0 = 結尾）。

當為 `position` 參數選擇「Absolute time (seconds)」時，您可以指定一個 `seconds` 值（預設值：0.0，範圍：0.0 至 10.0，步長：0.1），該值決定此圖像在輸出影片中從開頭算起的應用時間（以秒為單位）。

## ## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|---------|------|---------|
| `keyframes` | 一個關鍵影格鏈，包含新的關鍵影格以及任何可選的先前關鍵影格。 | LUMA_RAY32_KEYFRAME |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaRay32KeyframeNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `b49d879888e6e83d6937068e799ea583ed5c90284e829ac496821eea330fe9c7`
