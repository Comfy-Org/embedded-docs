# Convert SDR to HDR

**Convert SDR to HDR** 節點會將標準動態範圍的 sRGB 影像擴展為 Rec.2020 HLG HDR。它會保留影像現有的外觀，並將其亮度映射到更廣泛的範圍，因此結果必須在選取 HDR 色彩空間的情況下儲存。Alpha 會保持不變。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `image` | 要擴展為 HDR 的 sRGB SDR 影像。 | IMAGE | 是 | - |
| `algorithm` | HDR 擴展演算法。選取演算法後會顯示其參數 (`target_luminance`)。 | DYNAMIC_COMBO | 是 | `"lottes"` |

### lottes 輸入

當 `algorithm` 設為 `"lottes"` 時，會顯示這些參數。

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `target_luminance` | 以 nits 為單位的峰值白目標。0 會保留校準後的渲染。暗部影像不會被正規化到此峰值。（預設值：650.0） | FLOAT | 是 | 0.0 至 10000.0 （步進值：1.0） |

批次中的每張影像都會個別轉換：先將 sRGB 編碼反轉為線性光，再使用 Lottes 風格的有理曲線擴展亮度，並與校準過的單調對數增益曲線混合，最後將結果重新編碼為 Rec.2020 HLG。由於輸出是 HDR，儲存節點必須使用 `HDR` 色彩空間；若將其儲存為 sRGB，會導致亮度渲染不正確。

HLG 假設參考顯示器為 1000 nits，因此 `target_luminance` 低於 1000 的值會保留該參考，而值為 `0` 時則維持校準後的渲染不變。單通道影像在轉換前會擴展為三個通道，而 Alpha 通道會原樣複製。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `IMAGE` | Rec.2020 HLG HDR 影像。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageSDRToHDR/zh-TW.md)

---
**Source fingerprint (SHA-256):** `51eb0beac3d48345a30ba66d80d95873384cf5155fc06c33353b6d1dc029658a`
