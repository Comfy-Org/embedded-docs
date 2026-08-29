# 建立影片

Create Video 節點從一系列影像生成影片檔案。您可以設定每秒幀數的播放速度，可選擇加入音訊，並選擇生成影片的位元深度和色彩空間。

## 輸入

| 參數 | 描述 | 資料型別 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `影像` | 要從中建立影片的影像。 | IMAGE | 是 | - |
| `每秒影格數` | 影片播放速度的每秒幀數（預設：30.0）。 | FLOAT | 是 | 1.0 - 120.0 |
| `音訊` | 要加入影片的音訊。 | AUDIO | 否 | - |
| `bit_depth` | Auto 對 sRGB 使用 8 位元，對 HDR 使用 10 位元。明確選擇 8 位元和 10 位元則與色彩空間無關。（預設：`"auto"`） | COMBO | 否 | `"auto"`<br>8<br>10 |
| `color_space` | 輸入影像的色彩空間。HDR 選用 BT.2020/HLG，HDR PQ 選用 BT.2020/PQ。（預設：`"sRGB"`） | COMBO | 否 | `"sRGB"`<br>`"HDR"`<br>`"HDR PQ"` |

注意：當 `bit_depth` 設定為 `"auto"` 時，節點對 HDR 和 HDR PQ 色彩空間使用 10 位元，對 sRGB 使用 8 位元。

## 輸出

| 輸出名 | 描述 | 資料型別 |
|-------------|-------------|-----------|
| `output` | 包含輸入影像和可選音訊的生成影片。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateVideo/zh-TW.md)

---
**Source fingerprint (SHA-256):** `2fa73f38b0609de4159e557b6abe73652c5bebab9d34ffdda743b0eac6049f13`
