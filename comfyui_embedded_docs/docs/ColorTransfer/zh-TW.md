> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ColorTransfer/zh-TW.md)

## 概述
ColorTransfer 節點會調整目標影像的色調，使其與參考影像的色彩相符。它使用不同的數學演算法來分析並將參考影像的色彩特性（如亮度、對比度和色調分佈）轉移到目標影像上。這對於在多張影像之間建立視覺一致性或套用特定色調非常有用。

## 輸入
| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `image_target` | IMAGE | 是 | - | 要套用色彩轉換的影像。 |
| `image_ref` | IMAGE | 是 | - | 作為色彩比對依據的參考影像。 |
| `method` | COMBO | 是 | `"reinhard_lab"`<br>`"mkl_lab"`<br>`"histogram"` | 要使用的色彩轉換演算法。 |
| `source_stats` | DYNAMICCOMBO | 是 | `"per_frame"`<br>`"uniform"`<br>`"target_frame"` | 決定如何從來源（目標）影像計算色彩統計數據。 |
| `strength` | FLOAT | 是 | 0.0 至 10.0 | 色彩轉換效果的強度。值為 1.0 時套用完整轉換，0.0 則回傳原始影像。預設值：1.0 |

**參數詳細說明：**
*   **`source_stats` 選項：**
    *   **`per_frame`**：批次中的每個影格會個別與 `image_ref` 進行比對。
    *   **`uniform`**：所有來源影格的色彩統計數據會被合併計算，建立單一基準線，再與 `image_ref` 進行比對。
    *   **`target_frame`**：從目標批次中選取一個影格作為計算轉換至 `image_ref` 的基準。此轉換會均勻套用至所有影格，從而保留它們之間的相對色彩差異。選取此選項時，會出現額外的 `target_index` 參數。
*   **`target_index`**（當 `source_stats` 設為 `"target_frame"` 時出現）：用作計算轉換之來源基準的影格索引（從 0 開始）。預設值：0。必須介於 0 到 10000 之間。

**限制條件：**
*   如果 `strength` 設為 0.0 或 `image_ref` 為 `None`，節點會直接回傳原始的 `image_target`，不進行處理。
*   當 `source_stats` 設為 `"target_frame"` 時，`target_index` 必須是 `image_target` 批次中的有效索引。如果超出影格數量，則會使用最後一個影格。
*   對於使用 `"per_frame"` 作為 `source_stats` 的 `histogram` 方法，如果 `image_ref` 的批次大小大於 1，則每個目標影格會根據索引與對應的參考影格進行比對。如果參考批次只有一個影格，則該影格會用於所有目標影格。

## 輸出
| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `image` | IMAGE | 套用色彩轉換後產生的影像。 |

---
**Source fingerprint (SHA-256):** `93a8447def4d2263a8a859c0474de694e6567dc6d32377032c2ddae2420bb10c`
