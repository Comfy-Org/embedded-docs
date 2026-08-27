# VaeDecodeShapeTrellis

此節點將 Trellis2 形狀潛在表示解碼為 3D 網格。它使用 VAE 將稀疏形狀潛在資料轉換為網格幾何，並輸出在解碼過程中產生的形狀細分資料。此節點支援單一與批次潛在輸入，並自動將網格方向調整至預期的座標框架。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `samples` | 要解碼的潛在樣本，包含樣本張量與稀疏座標資料。潛在字典也可能包含選用欄位：用於批次形狀的 `coord_counts`、用於控制網格解析度的 `coord_resolution`，以及用於座標方向的 `model_frame`。 | LATENT | 是 | None |
| `vae` | 用於將形狀潛在資料解碼為網格的 VAE 模型。 | VAE | 是 | None |

### 關於 `samples` 的說明

- `samples` 輸入是一個潛在字典，必須包含 `samples` 張量與 `coords` 稀疏座標。
- 如果提供了 `coord_counts`，它必須是一個由非負整數組成的 1D 張量，且所有計數的總和必須等於座標列的總數。每個計數代表批次中的一個形狀。
- 如果提供了 `coord_resolution`，網格解析度將計算為 `coord_resolution * 16`。否則，將使用 VAE 內建的解析度緩衝區（預設值：1024）。
- 如果 `model_frame` 設為 `"z_up"`，解碼後的網格頂點會從 Z-up 座標系統旋轉至 glTF 所使用的 Y-up 慣例。預設值為 `"y_up"`。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `mesh` | 解碼後的 3D 網格，包含頂點位置與面索引。 | MESH |
| `shape_subdivides` | 在解碼過程的每個階段所產生的形狀細分資料。 | SHAPE_SUBDIVIDES |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VaeDecodeShapeTrellis/zh-TW.md)

---
**Source fingerprint (SHA-256):** `50f1b8200bd750671473278aaf94e6b08d6f9a6a72d5d1dc882ea7ab87084681`
