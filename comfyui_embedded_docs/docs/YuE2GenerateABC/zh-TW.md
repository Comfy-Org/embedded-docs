# YuE2 產生 ABC

此節點會使用 YuE2 文字與歌詞模型，根據風格描述和歌詞為歌曲生成 ABC 記譜。產生的 `abc` 輸出可連接到 YuE2 Generate Music 節點以產生音訊。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `clip` | 用於將風格與歌詞分詞，並生成 ABC 記譜的 YuE2 模型。 | CLIP | 是 | - |
| `style` | 描述歌曲音樂風格的文字。支援多行輸入和動態提示詞。 | STRING | 是 | - |
| `lyrics` | 包含歌曲歌詞的文字。支援多行輸入和動態提示詞。 | STRING | 是 | - |
| `種子` | 用於生成的隨機種子。變更它會產生不同結果。預設值：0。 | INT | 是 | 0 至 18446744073709551615 |
| `模式` | full：生成旋律與和弦；melody：僅生成旋律，建議用於翻唱。 | COMBO | 是 | "full"<br>"melody" |
| `max_abc_tokens` | 為 ABC 記譜生成的最大 token 數量。預設值：8192。進階設定。 | INT | 是 | 1 至 20000 |
| `temperature` | 控制生成 token 的隨機性。值越高，輸出越多樣。預設值：0.7。進階設定。 | FLOAT | 是 | 0.0 至 5.0 |
| `top_p` | 核取樣閾值；僅考慮累計機率在該閾值內的 token。預設值：0.9。進階設定。 | FLOAT | 是 | 0.01 至 1.0 |
| `top_k` | 將 token 選擇限制為機率最高的 K 個。預設值：30。進階設定。 | INT | 是 | 1 至 32768 |
| `repetition_penalty` | 生成過程中對重複 token 施加的懲罰。預設值：1.005。進階設定。 | FLOAT | 是 | 0.01 至 10.0 |
| `penalty_window` | 用於懲罰重複的最近 ABC token 數量。預設值：100。進階設定。 | INT | 是 | 1 至 20000 |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-----------|-----------|
| `abc` | 生成的歌曲 ABC 記譜，可連接到 YuE2 Generate Music 節點。 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/YuE2GenerateABC/zh-TW.md)

---
**Source fingerprint (SHA-256):** `2c1bf0841a044724ff0477f920972d70bbd97de49b56fbe6213a9ac134797130`
