# Luma Ray 3.2 關鍵影格

此節點會將引導圖像錨定到 Luma Ray 3.2 輸出影片時間軸上的特定位置。將此節點連接到 Luma Ray 3.2 Keyframes to Video 節點的 `keyframes` 輸入，並透過連接選用的 `keyframes` 輸入，將數個關鍵影格串接在一起。

## 輸入

### 通用輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `image` | 要放置在輸出影片所選時刻的引導圖像。 | IMAGE | 是 | - |
| `position` | 如何將此圖像放置在輸出影片的時間軸上。 | DYNAMIC_COMBO | 是 | "Fraction of duration (0.0-1.0)"<br>"Absolute time (seconds)" |
| `keyframes` | 選用的先前關鍵影格，用來與此關鍵影格串接。 | LUMA_RAY32_KEYFRAME | 否 | - |

### Fraction of duration (0.0-1.0) 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `fraction` | 此圖像在輸出影片中套用的位置（0.0 = 開始，1.0 = 結束）。預設值：0.0。 | FLOAT | 是 | 0.0 至 1.0 （步進值：0.01） |

### Absolute time (seconds) 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `seconds` | 從輸出影片開始算起，此圖像套用的時間（秒）。預設值：0.0。 | FLOAT | 是 | 0.0 至 10.0 （步進值：0.1） |

`position` 參數決定使用哪個值將圖像放置在時間軸上。只有屬於所選選項的子參數會顯示並使用：`fraction` 對應 "Fraction of duration (0.0-1.0)"，而 `seconds` 對應 "Absolute time (seconds)"。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `keyframes` | 包含新關鍵影格並結合任何選用之先前關鍵影格的關鍵影格鏈。 | LUMA_RAY32_KEYFRAME |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaRay32KeyframeNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `b49d879888e6e83d6937068e799ea583ed5c90284e829ac496821eea330fe9c7`
