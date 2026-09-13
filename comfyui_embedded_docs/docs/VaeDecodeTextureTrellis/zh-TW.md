# VaeDecodeTextureTrellis

此節點使用 VAE 將 Trellis2 紋理 latent 解碼為體素顏色。輸入 latent 包含帶有座標的稀疏特徵樣本；此節點會重建每個體素的顏色，並將結果以體素網格形式回傳，供下游節點（例如 PaintMesh）用來為 3D 網格上色。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `樣本` | 要解碼的紋理 latent。它包含樣本特徵與稀疏座標，並可能包含可選的中繼資料，例如座標計數（`coord_counts`）、模型框架（`model_frame`，預設：`"y_up"`）以及座標解析度（`coord_resolution`）。 | LATENT | 是 | — |
| `vae` | 用於將紋理 latent 解碼為體素顏色的 Trellis2 VAE。 | VAE | 是 | — |
| `形狀細分` | 用於在解碼期間引導更高細節重建的形狀資訊。有助於在更高解析度下保持結構一致性。 | SHAPE_SUBDIVIDES | 是 | — |

注意：當 `samples` latent 包含 `coord_counts` 時，這些計數必須為非負數，其總和必須與座標列數相符，且每個批次必須正好包含預期的列數；否則此節點會引發錯誤。如果 latent 的 `model_frame` 為 `"z_up"`，解碼後的體素座標會重新映射為 Y-up，以便與網格頂點對齊。提供 `coord_resolution` 時，輸出紋理解析度為該值乘以 16。否則，會從最大體素座標加一推斷，並向上取整至 256、512、1024、1536 或 2048 其中之一；若所需值超過 2048，則使用該較大值。若沒有可用的座標，解析度預設為 1024。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `voxel_colors` | 解碼後的體素資料，包含座標、顏色特徵與紋理解析度。每個體素有 6 個顏色通道：基礎顏色（RGB）、金屬度、粗糙度與 alpha，全部範圍均為 [0, 1]。使用頂點顏色的節點（例如 PaintMesh）會使用前 3 個通道。 | VOXEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VaeDecodeTextureTrellis/zh-TW.md)

---
**Source fingerprint (SHA-256):** `952ea7d7a0147519392bebe352a0da731462db278c8640fa527aa5b6f64e4aa7`
