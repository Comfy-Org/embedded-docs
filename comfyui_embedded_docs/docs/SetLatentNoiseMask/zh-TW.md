# 設定 latent 雜訊遮罩

此節點旨在對一組潛在樣本應用噪聲遮罩。它透過整合指定的遮罩來修改輸入樣本，從而改變其噪聲特性。

## 輸入

| 參數 | 說明 | 資料類型 |
| --- | --- | --- |
| `樣本` | 將應用噪聲遮罩的潛在樣本。此參數對於決定將被修改的基礎內容至關重要。 | `LATENT` |
| `遮罩` | 要應用於潛在樣本的遮罩。它定義了樣本中噪聲改變的區域和強度。 | `MASK` |

## 輸出

| 參數 | 說明 | 資料類型 |
| --- | --- | --- |
| `latent` | 已應用噪聲遮罩的修改後潛在樣本。 | `LATENT` |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SetLatentNoiseMask/zh-TW.md)
