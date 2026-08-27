# BakeNormalMapFromMesh

此節點會將高解析度網格上的切線空間法線貼圖，烘焙到低解析度網格的 UV 佈局上，以捕捉在減面過程中遺失的表面細節。請連接已展開 UV 的低解析度網格，以及其所來自的高解析度網格，節點便會輸出可用於「Apply Texture To Mesh」之 `normal_map` 輸入的影像。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `low_poly` | 接收烘焙細節的已展開 UV 低解析度網格。必須具備現有的 UV；此節點絕不會自行展開 UV。 | MESH | 是 | — |
| `high_poly` | 其表面細節將被烘焙至低解析度網格 UV 佈局中的高解析度網格。 | MESH | 是 | — |
| `resolution` | 方形輸出的法線貼圖之邊緣長度（像素），預設值：1024。 | INT | 是 | 64 到 8192（間距 64） |
| `cage_distance` | 表面搜尋帶，以邊界框對角線的比例表示。若在大量減面後出現錯誤或缺失的區塊，請調高此值；若其跨越間隙抓取，則調低此值。預設值：0.05。 | FLOAT | 是 | 0.001 到 0.5（間距 0.001） |
| `ignore_backfaces` | 跳過背向紋素的高解析度表面，避免裂縫或封閉空間抓取到對向牆面。僅在高解析度網格的頂點繞序不一致時停用。預設值：true。 | BOOLEAN | 是 | true / false |

注意：`low_poly` 必須具有 UV 座標。若沒有，節點會產生錯誤，因為它會烘焙到既有的 UV 佈局上，且不會對網格進行 UV 展開。當 `low_poly` 是批次時，每個項目會依序烘焙；若 `high_poly` 只包含一個項目，則該項目會對批次中的每個項目重複使用。批次中的空白網格會跳過並發出警告，且會產生平坦的中灰色（0.5）法線貼圖。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `normal_map` | 烘焙完成的切線空間法線貼圖（glTF/OpenGL +Y 慣例），為方形 resolution × resolution 的 RGB 影像，數值範圍在 [0,1]。可將其連接到「Apply Texture To Mesh」的 `normal_map` 輸入。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BakeNormalMapFromMesh/zh-TW.md)

---
**Source fingerprint (SHA-256):** `29df10014b5998b741d71db21d0c982d7bca85ad966a720063af15062e203322`
