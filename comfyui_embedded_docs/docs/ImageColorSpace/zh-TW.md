# 轉換影像色彩空間

ImageColorSpace 節點可在 sRGB（Rec.709）、linear Rec.709、HDR（Rec.2020 HLG）、HDR PQ（Rec.2020 PQ）、HDR LogC3 與 HDR ACEScct 色彩空間之間轉換影像。LogC3 使用 EI 800 曲線與 Rec.709 原色，且編碼限制在 [0, 1]；ACEScct 使用 AP1 原色與 D60 白點，並以 Bradford 適應轉換至 D65。當轉換為 SDR 輸出，或從 HDR PQ 轉換為 HDR 時，它會對整個批次中過量的亮度進行色調映射，並壓縮超出色域的色彩；linear 與 ACEScct 輸出，以及 linear-to-HDR 轉換，會保留擴展值。HLG 與 PQ 輸出會截斷負值通道。轉換以 float32 計算，且任何 Alpha 通道都會原樣傳遞。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `image` | 要轉換的輸入影像。 | IMAGE | 是 | 任何有效影像。 |
| `source` | 輸入像素的色彩空間。預設值："sRGB"。 | COMBO | 是 | `"sRGB"`<br>`"HDR"`<br>`"HDR PQ"`<br>`"linear"`<br>`"HDR LogC3"`<br>`"HDR ACEScct"` |
| `destination` | 輸出像素的色彩空間。將儲存節點設為這個相同的色彩空間。在儲存 EXR 前，先將 LogC3 或 ACEScct 轉換為 linear；或在儲存影片前，轉換為 sRGB/HDR/HDR PQ。預設值："sRGB"。 | COMBO | 是 | `"sRGB"`<br>`"HDR"`<br>`"HDR PQ"`<br>`"linear"`<br>`"HDR LogC3"`<br>`"HDR ACEScct"` |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `image` | 在指定目的地色彩空間中轉換後的影像。 | IMAGE |

## 備註

- Linear 1.0 使用與 sRGB 相同的 203-nit 參考白；HLG 使用 1000-nit 參考顯示器。
- Linear 與 ACEScct 輸出會保留擴展值；linear-to-HDR 轉換會保留高光，且不進行色調映射。
- SDR 輸出與 PQ-to-HLG 轉換會對整個批次中過量的亮度進行色調映射（共用一個白點，因此曝光不會逐幀改變），並壓縮超出色域的色彩。HLG 與 PQ 輸出會截斷負值通道。
- 轉換以 float32 計算，並傳回中間裝置與 dtype。
- LogC3 與 ACEScct 是攝影機對數編碼：若要儲存 EXR，請將它們轉換為 linear；或在儲存影片前轉換為 sRGB/HDR/HDR PQ。
- Straight alpha 不會進行色彩轉換；只有 RGB 通道會被轉換。
- 如果 `source` 與 `destination` 相同，則不會套用任何色彩轉換——影像只會被移到中間裝置與 dtype。

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageColorSpace/zh-TW.md)

---
**Source fingerprint (SHA-256):** `fdf8b4f16a1e0c7ff9a86b8cc40f6f796175205e4b1f491b595a74a8456b9b94`
