# ModelAttentionBackend

此節點可讓您選擇模型用於其注意力計算的注意力後端。它會建立模型的副本，並換入您選擇的注意力函式，這可能會影響效能或行為。如果所選的後端不可用，它會自動回退到 PyTorch 注意力，並記錄警告。

## 輸入
| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | 套用所選注意力後端的模型。 | MODEL | 是 |  |
| `attention` | 要使用的注意力後端（預設值："pytorch attention"）。如果所選後端不可用，則會使用 PyTorch 注意力作為回退。 | STRING | 是 | "pytorch attention"<br>"comfy kitchen attention" |

注意：「comfy kitchen attention」選項只有在目前環境中具備 comfy kitchen int8 注意力模組時才會列出。

## 輸出
| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `MODEL` | 已套用所選注意力後端的輸入模型副本。 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelAttentionBackend/zh-TW.md)

---
**Source fingerprint (SHA-256):** `4ba613cc0bf5b3e7f9effa895b98b3a3bd302e5d20e9d7e18d1633906c783244`
