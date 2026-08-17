# LatentCutToBatch

LatentCutToBatch 節點會沿著選定的維度將潛在表示分割成多個切片，並將它們堆疊成新的批次。這讓您可以獨立處理潛在樣本的不同部分。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `samples` | 要被分割並批次化的潛在表示。 | LATENT | 是 | - |
| `dim` | 用於切割潛在樣本的維度。`"t"` 指的是時間維度，`"x"` 指的是寬度，`"y"` 指的是高度。 | COMBO | 是 | `"t"`<br>`"x"`<br>`"y"` |
| `slice_size` | 從指定維度切割的每個切片的大小。如果維度大小無法被此值整除，其餘部分將被丟棄。（預設值：1） | INT | 是 | 1 to 16384 (max resolution) |

注意：如果選定的維度是批次或通道軸，輸入將保持不變地回傳。如果 `slice_size` 大於維度的大小，則整個維度將作為單一切片使用。

## 輸出

| 輸出名 | 描述 | 資料類型 |
| --- | --- | --- |
| `samples` | 結果潛在批次，包含切片並堆疊後的樣本。 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentCutToBatch/zh-TW.md)

---
**Source fingerprint (SHA-256):** `873c9bc8391971887f1ab636c086cab86f5504a9c653bc80b54120ee53980bdf`
