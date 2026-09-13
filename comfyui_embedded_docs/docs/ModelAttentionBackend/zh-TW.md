# 模型注意力後端

此節點會為模型選取稠密注意力實作，複製模型、套用所選後端，並傳回修補後的複本。當與 Block Sparse Attention 搭配使用時，每當稀疏注意力未啟用或不受支援，就會使用此外端。若所選後端無法使用，節點會自動退回至 PyTorch attention。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | 要修補的模型。 | MODEL | 是 |  |
| `attention` | 要套用的稠密注意力後端。Comfy Kitchen 注意力使用量化 INT8 注意力，且僅適用於 Nvidia 和 AMD GPU。預設："pytorch attention"。若所選後端無法使用，將以 PyTorch attention 作為後備。 | COMBO | 是 | "pytorch attention"<br>"comfy kitchen attention" |

注意："comfy kitchen attention" 選項僅會在目前環境中可使用 Comfy Kitchen INT8 注意力模組時列出。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-----------|-----------|
| `model` | 已套用所選注意力後端的輸入模型複本。 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelAttentionBackend/zh-TW.md)

---
**Source fingerprint (SHA-256):** `4f6e4800c2a3bb09b47b7c8f0481e1b6de3070f57234e610df5d3ce60dfdb309`
