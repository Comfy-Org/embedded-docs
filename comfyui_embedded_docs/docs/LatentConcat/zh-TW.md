LatentConcat 節點透過沿著選定的維度將兩個潛在樣本連接在一起來組合它們。它接收兩個潛在輸入，並沿著 x、y 或 t 軸進行連接，並可選擇控制哪個樣本優先。在執行連接之前，節點會自動調整第二個輸入的批次大小以匹配第一個輸入。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `樣本1` | 要連接的第一個潛在樣本 | LATENT | 是 | - |
| `樣本2` | 要連接的第二個潛在樣本 | LATENT | 是 | - |
| `維度` | 用於連接潛在樣本的維度。正值 (x, y, t) 會將 samples1 放在 samples2 之前。負值 (-x, -y, -t) 會將 samples2 放在 samples1 之前。維度對應關係為：x = 寬度，y = 高度，t = 時間/影格 | COMBO | 是 | `"x"`<br>`"-x"`<br>`"y"`<br>`"-y"`<br>`"t"`<br>`"-t"` |

**注意：** 第二個潛在樣本 (`samples2`) 會在連接前自動調整以匹配第一個潛在樣本 (`samples1`) 的批次大小。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `output` | 沿著指定維度組合兩個輸入樣本後所產生的連接潛在樣本 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentConcat/zh-TW.md)

---
**Source fingerprint (SHA-256):** `46514ef85887279ec577ad88ac46f1c20f428903ee63b076888d7d5df09fde77`
