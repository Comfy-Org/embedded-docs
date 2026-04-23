> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ColorTransfer/zh-TW.md)

ColorTransfer 節點會調整目標影像的色彩調色盤，使其與參考影像的色彩相匹配。它使用不同的數學演算法來分析並轉移參考影像的色彩特徵（例如亮度、對比度和色調分佈）到目標影像上。這對於在多張影像間建立視覺一致性，或套用特定的色彩分級非常有用。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `image_target` | IMAGE | 是 | - | 要套用色彩轉換的影像。 |
| `image_ref` | IMAGE | 否 | - | 要匹配色彩的參考影像。如果未提供，則跳過處理並直接返回未更改的目標影像。 |
| `method` | COMBO | 是 | `"reinhard_lab"`<br>`"mkl_lab"`<br>`"histogram"` | 要使用的色彩轉移演算法。 |
| `source_stats` | DYNAMICCOMBO | 是 | `"per_frame"`<br>`"uniform"`<br>`"target_frame"` | 決定如何從來源（目標）影像計算色彩統計數據。 |
| `strength` | FLOAT | 是 | 0.0 至 10.0 | 色彩轉移效果的強度。值為 1.0 時套用完整轉換，值為 0.0 時返回原始影像。預設值：1.0 |

**參數詳情：**
*   **`source_stats` 選項：**
    *   **`per_frame`**：批次中的每個影格都單獨與 `image_ref` 進行匹配。
    *   **`uniform`**：匯總所有來源影格的色彩統計數據以建立單一基準，然後與 `image_ref` 進行匹配。
    *   **`target_frame`**：從目標批次中選擇一個影格作為計算轉換到 `image_ref` 的基準。然後將此轉換統一應用到所有影格，這能保留影格之間的相對色彩差異。選擇此選項時，會出現額外的 `target_index` 參數。
*   **`target_index`**（當 `source_stats` 為 `"target_frame"` 時出現）：用作計算轉換的來源基準的影格索引（從 0 開始）。預設值：0。必須介於 0 到 10000 之間。

**限制條件：**
*   如果未提供 `image_ref` 或 `strength` 設為 0.0，節點將返回未經處理的原始 `image_target`。
*   當 `source_stats` 設為 `"target_frame"` 時，`target_index` 必須是 `image_target` 批次中的有效索引。如果超過影格數量，則使用最後一個影格。
*   對於 `method` 設為 `"histogram"` 且 `source_stats` 設為 `"per_frame"` 的情況，如果 `image_ref` 的批次大小大於 1，則每個目標影格會按索引與對應的參考影格匹配。如果參考批次只有一個影格，則該影格將用於所有目標影格。

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `image` | IMAGE | 套用色彩轉移後產生的影像。 |