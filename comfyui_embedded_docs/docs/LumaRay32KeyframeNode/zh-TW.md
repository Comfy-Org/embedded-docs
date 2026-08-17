# Luma Ray 3.2 關鍵影格

此節點將引導影像錨定到 Luma Ray 3.2 輸出影片時間軸上的特定位置。將此節點連接到 Luma Ray 3.2 Keyframes to Video 節點的 `keyframes` 輸入，並透過連接可選的 `keyframes` 輸入來串連多個關鍵影格。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `image` | 要放置在輸出影片所選時間點的引導影像。 | IMAGE | 是 | - |
| `position` | 如何將此影像放置在輸出影片的時間軸上。 | DYNAMIC_COMBO | 是 | "Fraction of duration (0.0-1.0)"<br>"Absolute time (seconds)" |
| `keyframes` | 可選的較早關鍵影格，用於與此關鍵影格串連。 | LUMA_RAY32_KEYFRAME | 否 | - |

`position` 參數決定用哪個值來將影像放置在時間軸上。

當為 `position` 參數選取「Fraction of duration (0.0-1.0)」時，您可以指定一個 `fraction` 值（預設值：0.0，範圍：0.0 至 1.0，步長：0.01），此值決定該影像套用於輸出影片中的哪個位置（0.0 = 開頭，1.0 = 結尾）。

當為 `position` 參數選取「Absolute time (seconds)」時，您可以指定一個 `seconds` 值（預設值：0.0，範圍：0.0 至 10.0，步長：0.1），此值決定從輸出影片開始起算的秒數，也就是該影像套用的時間點。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `keyframes` | 一個關鍵影格鏈，包含新的關鍵影格以及任何可選的較早關鍵影格。 | LUMA_RAY32_KEYFRAME |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaRay32KeyframeNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `b49d879888e6e83d6937068e799ea583ed5c90284e829ac496821eea330fe9c7`
