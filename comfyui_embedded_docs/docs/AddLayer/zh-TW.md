# AddLayer

Add Layer 節點會將輸入影像轉換為圖層，並將其放置在畫布上，可以建立新的圖層堆疊，或附加到現有的圖層堆疊。您可以設定圖層的名稱、位置、大小、旋轉、不透明度、混合模式、堆疊順序，以及水平或垂直翻轉。此節點被標記為實驗性。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `layers` | 要附加到的圖層堆疊。保持未連接以開始新的堆疊。 | LAYERS | 否 | — |
| `image` | 圖層內容，使用其原始大小。一批影像會展開為連續的多個圖層。 | IMAGE | 是 | — |
| `mask` | 此圖層的透明度遮罩。遮罩區域（值 1）變成透明，並與圖像已有的 Alpha 通道相乘。 | MASK | 否 | — |
| `name` | 在合成器編輯器中顯示的圖層名稱。（預設值：""） | STRING | 否 | — |
| `x` | 在畫布上的初始水平位置。（預設值：0） | INT | 否 | -MAX_RESOLUTION 至 MAX_RESOLUTION |
| `y` | 在畫布上的初始垂直位置。（預設值：0） | INT | 否 | -MAX_RESOLUTION 至 MAX_RESOLUTION |
| `opacity` | 初始圖層不透明度。（預設值：1.0） | FLOAT | 否 | 0.0 至 1.0（步長：0.01） |
| `blend_mode` | 初始混合模式，套用於下方的圖層。在預設透明背景上的底層，非 normal 模式會產生透明度。（預設值："normal"） | COMBO | 否 | 多個選項可用 |
| `rotation` | 初始旋轉角度，順時針。（預設值：0.0） | FLOAT | 否 | -360.0 至 360.0（步長：1.0） |
| `width` | 初始顯示寬度。設為 0 時保留圖像的原始寬度。（預設值：0） | INT | 否 | 0 至 MAX_RESOLUTION |
| `height` | 初始顯示高度。設為 0 時保留圖像的原始高度。（預設值：0） | INT | 否 | 0 至 MAX_RESOLUTION |
| `z_index` | 堆疊覆寫。圖層依 z_index 進行穩定排序；相同值保持其列表順序。（預設值：0） | INT | 否 | -1000 至 1000 |
| `flip_h` | 水平翻轉圖層。（預設值：False） | BOOLEAN | 否 | false / true |
| `flip_v` | 垂直翻轉圖層。（預設值：False） | BOOLEAN | 否 | false / true |

備註：
- 僅 `image` 為必填；所有其他輸入皆為選填。
- 當 `layers` 保持未連接時，會建立新的圖層堆疊。當連接了圖層堆疊時，新圖層會附加到其中。
- `image` 輸入中的一批圖像會建立多個連續圖層。
- `width` 和 `height` 預設為 0，這會保留圖像的原始尺寸。大於 0 的值會覆寫顯示大小。
- `opacity`、`blend_mode`、`rotation`、`width` 和 `height` 僅在與其預設值不同時才會套用。
- 已連接圖層堆疊的畫布大小會保留在輸出中。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `layers` | 附加了此圖層的圖層堆疊。 | LAYERS |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AddLayer/zh-TW.md)

---
**Source fingerprint (SHA-256):** `b7bf1a012d17cb5768b49d5c0617e13562ba015f695e6c9b1d1bbefba4150f9e`
