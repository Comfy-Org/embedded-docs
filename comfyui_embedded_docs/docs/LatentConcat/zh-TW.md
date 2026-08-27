# 潛空間合併

LatentConcat 節點透過沿所選維度將兩個潛在樣本拼接在一起，以組合它們。它接受兩個潛在輸入，並沿 x、y 或 t 軸進行拼接，且可控制哪個樣本在前。節點在執行拼接前，會自動調整第二個輸入的批次大小以符合第一個輸入。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `樣本1` | 要拼接的第一個潛在樣本 | LATENT | 是 | - |
| `樣本2` | 要拼接的第二個潛在樣本 | LATENT | 是 | - |
| `維度` | 拼接潛在樣本所沿的維度。正值（x、y、t）會在結果中將 samples1 置於 samples2 之前。負值（-x、-y、-t）會將 samples2 置於 samples1 之前。維度對應：x = 寬度，y = 高度，t = 時間/幀 | COMBO | 是 | `"x"`<br>`"-x"`<br>`"y"`<br>`"-y"`<br>`"t"`<br>`"-t"` |

**注意：** 第二個潛在樣本（`samples2`）會在拼接前自動按需重複，以符合第一個潛在樣本（`samples1`）的批次大小。

## 輸出

| 輸出名 | 描述 | 資料類型 |
| --- | --- | --- |
| `output` | 沿指定維度組合兩個輸入樣本後所得的拼接潛在樣本 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentConcat/zh-TW.md)

---
**Source fingerprint (SHA-256):** `dfe27f76ad12e16623d62c9e7f0b2772df6ecadb543a4eee430bc38ab04a12f2`
