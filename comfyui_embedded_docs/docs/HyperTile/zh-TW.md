# HyperTile

HyperTile 節點對擴散模型中的注意力機制套用切塊（tiling）技術，以在生成影像時最佳化記憶體使用。它將潛在空間分割成較小的區塊並分別處理，然後重新組裝結果。這使得可以在不耗盡記憶體的情況下處理更大的影像尺寸。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 要套用 HyperTile 最佳化的擴散模型 | MODEL | 是 | - |
| `tile_size` | 處理時使用的目標區塊大小（預設值：256）。有效區塊大小會向下取整為 8 的倍數，且最小值為 32。 | INT | 否 | 1 - 2048 |
| `swap_size` | 節點隨機選擇如何分割影像時所考慮的候選區塊分割數量。較大的值允許分割時有更多變化（預設值：2） | INT | 否 | 1 - 128 |
| `max_depth` | 套用切塊的最大深度層級（解析度尺度）。值為 0 時僅在最高解析度下套用切塊（預設值：0） | INT | 否 | 0 - 10 |
| `scale_depth` | 啟用時，區塊大小會在較深的深度層級按比例縮放。這有助於在較低解析度下維持品質（預設值：False） | BOOLEAN | 否 | True / False |

注意：`scale_depth` 僅在 `max_depth` 大於 0 時才會生效，因為在最高解析度層級（深度 0）下，區塊大小永遠不會被縮放。

## 輸出

| 輸出名 | 描述 | 資料類型 |
| --- | --- | --- |
| `model` | 已套用 HyperTile 最佳化的修改後模型 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HyperTile/zh-TW.md)

---
**Source fingerprint (SHA-256):** `fb2fa29a403b6b7de7d5263240cc51a74126078457a3ff9ea63aeded45b9b74a`
