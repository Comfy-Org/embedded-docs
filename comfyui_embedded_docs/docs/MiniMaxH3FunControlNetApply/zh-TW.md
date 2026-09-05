# MiniMaxH3FunControlNetApply

此節點將 MiniMax H3 Fun ControlNet 作為模型補丁套用於文字轉影片模型。它可以選擇性地使用控制影片與遮罩來引導生成，並回傳模型的補丁副本以供後續取樣。當強度設為 0，或未提供控制影片與遮罩時，輸入模型會原樣回傳。

## 輸入

| 參數 | 描述 | 資料型別 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | 套用 MiniMax H3 Fun ControlNet 補丁的擴散模型。 | MODEL | 是 | N/A |
| `model_patch` | 此 MiniMax H3 Fun ControlNet 補丁會將其控制信號注入模型中；它必須與給定的 `model` 相容。 | MODEL_PATCH | 是 | N/A |
| `vae` | 用於將控制影片與來源影片畫面編碼為模型預期之潛在空間的 VAE。 | VAE | 是 | N/A |
| `strength` | ControlNet 效果的整體強度。設為 0 時，節點不執行任何操作，並原樣回傳輸入模型。（預設：1.0） | FLOAT | 是 | min 0.0, max 10.0, step 0.01 |
| `start_percent` | 取樣範圍的開始，以取樣排程的百分比表示，在此期間 ControlNet 處於啟用狀態。內部會轉換為等效的 sigma 值。（預設：0.0） | FLOAT | 是 | min 0.0, max 1.0, step 0.001 |
| `end_percent` | 取樣範圍的結束，以取樣排程的百分比表示，在此期間 ControlNet 處於啟用狀態。內部會轉換為等效的 sigma 值。（預設：1.0） | FLOAT | 是 | min 0.0, max 1.0, step 0.001 |
| `control_video` | 可選的影片畫面，作為 ControlNet 的視覺提示。畫面會調整大小以符合生成的影片，並使用 `vae` 進行編碼。 | IMAGE | 否 | N/A |
| `mask` | 1 標記要重新生成的區域。遮罩值高於 0.5 的區域會被視為已標記區域。 | MASK | 否 | N/A |
| `source_video` | 位於遮罩後方的影片；只有在提供遮罩時才會讀取。 | IMAGE | 否 | N/A |

注意：若要讓補丁生效，`strength` 必須大於 0，且至少需要提供 `control_video` 或 `mask`。除非提供 `mask`，否則會忽略 `source_video`；如果提供 `mask` 但未提供 `source_video`，遮罩區域後方的內容會被視為黑色。

## 輸出

| 輸出名稱 | 描述 | 資料型別 |
|-------------|-------------|-----------|
| `model` | 已套用 MiniMax H3 Fun ControlNet 的輸入模型補丁副本。若 `strength` 為 0，或未提供控制影片與遮罩，則原樣回傳原始模型。 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MiniMaxH3FunControlNetApply/zh-TW.md)

---
**Source fingerprint (SHA-256):** `e907fb8e5ae60663d1d10b315985695ee5d49397fef6bd76b0e723637457a74a`
