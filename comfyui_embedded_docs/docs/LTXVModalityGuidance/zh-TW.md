# LTXV 模態引導（A/V 耦合）

此節點對 LTXV-AV 模型套用跨模態（音訊-影片）引導。在採樣過程中，每個步驟會額外執行一次前向傳播，並停用音訊轉影片與影片轉音訊的交叉注意力連接，然後將結果推向耦合預測，以增強影音同步（例如唇形同步）。`modality_scale` 的參考預設值為 3.0；將其設定為 1.0 會停用額外的前向傳播，且此功能可與 dual-CFG guider 和 STG 搭配使用。

## 輸入

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `model` | 將套用模態引導的基礎模型。此模型會在內部複製，原始模型保持不變。 | MODEL | 是 | - |
| `modality_scale` | 音訊-影片耦合引導的強度。預設值為 3.0。設定為 1.0 可停用額外的前向傳播。 | FLOAT | 是 | 1.0 至 100.0 (default: 3.0) |
| `start_percent` | 採樣過程中模態引導開始的點，以 0.0 到 1.0 的百分比表示。這是一個進階參數。預設值為 0.0。 | FLOAT | 是 | 0.0 至 1.0 (default: 0.0) |
| `end_percent` | 採樣過程中模態引導結束的點，以 0.0 到 1.0 的百分比表示。這是一個進階參數。預設值為 1.0。 | FLOAT | 是 | 0.0 至 1.0 (default: 1.0) |

僅當採樣步驟的 sigma 值落在 `start_percent` 與 `end_percent` 定義的範圍內時，才會套用引導。在此範圍之外，節點會直接回傳去噪後的結果而不做變更。此外，`modality_scale` 為 1.0 時也會完全停用額外的前向傳播。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `model` | 已附加 post-CFG 引導函數的複製模型。此修改後的模型會在採樣期間套用模態引導。 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVModalityGuidance/zh-TW.md)

---
**Source fingerprint (SHA-256):** `038be607c42e626a8a8f5fe336ee466d0847d43835edb71e20ff38f668069cfb`
