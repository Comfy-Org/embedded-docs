> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TorchCompileModel/zh-TW.md)

TorchCompileModel 節點會對模型應用 PyTorch 編譯功能以優化其效能。它會建立輸入模型的副本，並使用指定的後端將其封裝在 PyTorch 的編譯功能中。這可以提升模型在推理過程中的執行速度。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | 是 | - | 需要進行編譯和優化的模型 |
| `backend` | STRING | 是 | "inductor"<br>"cudagraphs" | 用於優化的 PyTorch 編譯後端 |

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `model` | MODEL | 已應用 PyTorch 編譯的已編譯模型 |