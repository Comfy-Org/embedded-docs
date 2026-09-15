# 套用 MiniMax H3 Fun ControlNet

此節點將 MiniMax H3 Fun ControlNet 作為模型修補（model patch）套用至文字轉影片模型。它可以使用選用的控制影片與選用的遮罩來引導生成，並回傳套用修補後的模型副本以供後續取樣使用。當 `strength` 設為 0，或未提供控制影片與遮罩時，會原封不動地回傳輸入模型。

## 輸入

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `model` | 要套用 MiniMax H3 Fun ControlNet 修補的擴散模型。 | MODEL | 是 | N/A |
| `model_patch` | MiniMax H3 Fun ControlNet 修補，其控制訊號會注入模型中；它必須與指定的 `model` 相容。 | MODEL_PATCH | 是 | N/A |
| `vae` | 用於將控制影片與來源影片的影格編碼為模型所預期的潛在空間的 VAE。 | VAE | 是 | N/A |
| `strength` | ControlNet 效果的整體強度。設為 0 時，此節點不會執行任何操作，並原封不動地回傳輸入模型。（預設值：1.0） | FLOAT | 是 | min 0.0, max 10.0, step 0.01 |
| `start_percent` | 取樣範圍的起點，以取樣排程的百分比表示，ControlNet 在此範圍內作用。它會在內部轉換為等效的 sigma 值。這是進階設定。（預設值：0.0） | FLOAT | 是 | min 0.0, max 1.0, step 0.001 |
| `end_percent` | 取樣範圍的終點，以取樣排程的百分比表示，ControlNet 在此範圍內作用。它會在內部轉換為等效的 sigma 值。這是進階設定。（預設值：1.0） | FLOAT | 是 | min 0.0, max 1.0, step 0.001 |
| `control_video` | 選用的影片影格，用作 ControlNet 的視覺提示。這些影格會被調整大小以符合生成的影片，並使用 `vae` 進行編碼。 | IMAGE | 否 | N/A |
| `mask` | 1 表示要重新生成的區域。遮罩值高於 0.5 的區域會被視為標記區域。 | MASK | 否 | N/A |
| `source_video` | 遮罩後方的影片；僅在提供遮罩時才會讀取。 | IMAGE | 否 | N/A |

注意：若要讓修補產生效果，`strength` 必須大於 0，且必須提供 `control_video` 或 `mask` 其中至少一項。除非提供 `mask`，否則 `source_video` 會被忽略；若提供了 `mask` 但沒有 `source_video`，遮罩區域後方的內容會被視為黑色。當同時提供 `control_video` 與 `mask` 時，控制提示會結合控制影片特徵與被遮罩的來源內容。

## 輸出

| Output Name | Description | Data Type |
|-------------|-------------|-----------|
| `model` | 已套用 MiniMax H3 Fun ControlNet 的輸入模型修補副本。若 `strength` 為 0，或未提供控制影片或遮罩，則會原封不動地回傳原始模型。 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MiniMaxH3FunControlNetApply/zh-TW.md)

---
**Source fingerprint (SHA-256):** `e907fb8e5ae60663d1d10b315985695ee5d49397fef6bd76b0e723637457a74a`
