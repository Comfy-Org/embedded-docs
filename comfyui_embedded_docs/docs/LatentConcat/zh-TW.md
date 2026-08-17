# 潛空間合併

LatentConcat 節點會沿著指定維度拼接兩個潛在樣本。此節點接收兩個潛在輸入，沿著 x、y 或 t 軸進行拼接，並可控制哪個樣本在前。節點在執行拼接前，會自動將第二個輸入的批次大小調整為與第一個輸入一致。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `samples1` | 要拼接的第一個潛在樣本 | LATENT | 是 | - |
| `samples2` | 要拼接的第二個潛在樣本 | LATENT | 是 | - |
| `dim` | 拼接潛在樣本時所沿用的維度。正值（x、y、t）會在結果中將 `samples1` 置於 `samples2` 之前。負值（-x、-y、-t）會將 `samples2` 置於 `samples1` 之前。維度對應關係：x = 寬度，y = 高度，t = 時間/幀數 | COMBO | 是 | `"x"`<br>`"-x"`<br>`"y"`<br>`"-y"`<br>`"t"`<br>`"-t"` |

**注意：** 在拼接之前，第二個潛在樣本（`samples2`）會自動調整，以匹配第一個潛在樣本（`samples1`）的批次大小。

## 輸出

| 輸出名 | 描述 | 資料類型 |
| --- | --- | --- |
| `output` | 沿指定維度合併兩個輸入樣本後所得的拼接潛在樣本 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentConcat/zh-TW.md)

---
**Source fingerprint (SHA-256):** `dfe27f76ad12e16623d62c9e7f0b2772df6ecadb543a4eee430bc38ab04a12f2`
