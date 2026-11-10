# 建立影片

The Create Video 節點會將一連串圖像組合成一段影片。你可以設定播放速度（以每秒影格數為單位）、選擇性地加入音訊，並選擇輸出影片的壓縮格式、位元深度與色彩空間。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `影像` | 用於建立影片的圖像。 | IMAGE | 是 | - |
| `每秒影格數` | 影片播放速度的每秒影格數（預設：30.0）。 | FLOAT | 是 | 1.0 - 120.0 |
| `音訊` | 要加入影片的音訊。 | AUDIO | 否 | - |
| `bit_depth` | Auto 對 sRGB 使用 8 位元，對 HDR 與 HDR PQ 使用 10 位元。明確指定的 8 位元與 10 位元選項與色彩空間無關。（預設："auto"） | COMBO | 否 | `"auto"`<br>8<br>10 |
| `color_space` | 輸入圖像的色彩空間。HDR 會選擇 BT.2020/HLG，HDR PQ 會選擇 BT.2020/PQ。（預設："sRGB"） | COMBO | 否 | `"sRGB"`<br>`"HDR"`<br>`"HDR PQ"` |
| `chroma_subsampling` | 444 保留完整色彩解析度，422 將水平色彩解析度減半，420 則將兩個軸向的色彩解析度都減半。Auto 使用編解碼器的預設值。不受支援的選項會改用最接近的支援模式，並在主控台輸出警告。（預設："auto"） none 交由編碼器決定。 | COMBO | 否 | `"auto"`<br>`"444"`<br>`"422"`<br>`"420"`<br>`"none"` |
| `codec` | 可選擇立即編碼影片。None 會將圖像保持為張量形式；Auto 使用 H.264。（預設："none"） | COMBO | 否 | `"none"`<br>來自影片編解碼器清單的可用影片編解碼器選項（例如 `"auto"` 及其他支援的編解碼器） |

注意：當 `bit_depth` 設為 `"auto"` 時，節點會自動對 HDR 與 HDR PQ 色彩空間使用 10 位元，並對 sRGB 使用 8 位元。

注意：`codec` 參數是進階選項。當它保持為 `"none"` 時，輸出會維持張量形式；選擇任何其他編解碼器則會立即編碼影片。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `output` | 產生的影片，包含輸入的圖像與可選的音訊。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateVideo/zh-TW.md)

---
**Source fingerprint (SHA-256):** `e36be7cefdd794a39aa9e8806c89701d5b27bb8d49e856ae38af59eb43fbee48`
