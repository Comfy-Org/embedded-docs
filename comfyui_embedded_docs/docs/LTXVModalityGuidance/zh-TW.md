# LTXVModalityGuidance

此節點對 LTXV-AV 模型套用跨模態（音訊-視訊）引導。在取樣期間，每次步驟會額外執行一次前向傳遞，並停用音訊到視訊與視訊到音訊的交叉注意力連線，然後將結果推向耦合預測。這能強化音訊與視覺的同步，例如唇形同步。`modality_scale` 的參考預設值為 3.0；將其設為 1.0 會停用額外的前向傳遞。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | 套用模態引導的基礎模型。此模型會在內部複製，原始模型保持不變。 | MODEL | 是 | - |
| `modality_scale` | 音訊-視訊耦合引導的強度。預設為 3.0。設為 1.0 可停用額外的前向傳遞。 | FLOAT | 是 | 1.0 至 100.0 (default: 3.0) |
| `start_percent` | 取樣過程中，模態引導開始生效的點，以 0.0 到 1.0 的百分比表示。預設為 0.0。 | FLOAT | 是 | 0.0 至 1.0 (default: 0.0) |
| `end_percent` | 取樣過程中，模態引導結束生效的點，以 0.0 到 1.0 的百分比表示。預設為 1.0。 | FLOAT | 是 | 0.0 至 1.0 (default: 1.0) |

引導僅套用於 sigma 值落在 `start_percent` 與 `end_percent` 所定義範圍內的取樣步驟。在此範圍之外，節點會直接回傳去雜訊後的結果而不做任何修改。`modality_scale` 設為 1.0 時，也會完全停用額外的前向傳遞。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `model` | 附加了 post-CFG 引導函數的複製模型。此修改後的模型會在取樣期間套用模態引導。 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVModalityGuidance/zh-TW.md)

---
**Source fingerprint (SHA-256):** `038be607c42e626a8a8f5fe336ee466d0847d43835edb71e20ff38f668069cfb`
