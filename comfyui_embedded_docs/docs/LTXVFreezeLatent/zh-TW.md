# LTXV 凍結潛空間

LTXV Freeze Latent 節點會將 latent 的雜訊遮罩設為零，這會在取樣執行期間讓該 latent 保持乾淨且不變。它同時適用於視訊與音訊 latent，因此可以在 latent 與其他項目串接之前，或在它完全不應被去雜訊時將其凍結。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `latent` | 要凍結的視訊或音訊 latent。音訊為 4D；視訊為 5D。 | LATENT | 是 | N/A |

### 限制

- 該 latent 必須包含純張量。不接受串接的音訊-視訊 latent；必須先使用 Separate AV Latent 節點將其拆分。
- 僅支援 4D latent（音訊）與 5D latent（視訊）。任何其他形狀都會導致錯誤。
- 產生的雜訊遮罩會以零建立，並使用與輸入張量相同的裝置。對於視訊 latent，遮罩的形狀為 (batch, 1, frames, 1, 1)；對於音訊 latent，其形狀為 (batch, 1, frames, 1)。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `latent` | 已加入零雜訊遮罩的輸入 latent，使其在取樣期間保持乾淨。 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVFreezeLatent/zh-TW.md)

---
**Source fingerprint (SHA-256):** `d5d228687f0a124644323c0448dcce53ed6eb2224d3f44d1756079b2a71539ca`
