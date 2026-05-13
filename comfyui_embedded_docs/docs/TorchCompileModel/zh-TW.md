> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TorchCompileModel/zh-TW.md)

TorchCompileModel 節點將 PyTorch 編譯功能應用於模型，以優化其效能。它會建立輸入模型的副本，並使用指定的後端以 PyTorch 的編譯功能進行包裝。這可以在推論過程中提升模型的執行速度。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | 是 | - | 要進行編譯和優化的模型 |
| `backend` | STRING | 是 | "inductor"<br>"cudagraphs" | 用於優化的 PyTorch 編譯後端（預設值："inductor"） |

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `model` | MODEL | 已套用 PyTorch 編譯的模型 |

---
**Source fingerprint (SHA-256):** `923e71b528e6e53468916f74c2a02924bf51738f29e36638312c6da6357fcedb`
