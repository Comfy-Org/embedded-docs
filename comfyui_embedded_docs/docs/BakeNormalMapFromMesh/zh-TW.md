# BakeNormalMapFromMesh

此節點將高多邊形網格（high-poly mesh）的切線空間法線貼圖烘焙到低多邊形網格（low-poly mesh）的 UV 佈局上，捕捉減面過程中遺失的表面細節。連接已展開 UV 的低多邊形網格及其來源的高多邊形網格，節點便會輸出一個影像，可直接用於 Apply Texture To Mesh 的 `normal_map` 輸入。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `low_poly` | 接收烘焙細節的 UV 展開低多邊形網格。必須具有現有的 UV；此節點絕不會自動展開 UV。 | MESH | 是 | — |
| `high_poly` | 其表面細節會被烘焙到低多邊形網格 UV 佈局中的高多邊形網格。 | MESH | 是 | — |
| `resolution` | 正方形輸出法線貼圖的邊長（像素），預設值：1024。 | INT | 是 | 64 至 8192 (step 64) |
| `cage_distance` | 表面搜尋範圍，以邊界框對角線的比例表示。在重度減面導致錯誤/缺失區塊時調高；若跨越間隙抓取則調低。預設值：0.05。 | FLOAT | 是 | 0.001 至 0.5 (step 0.001) |
| `ignore_backfaces` | 跳過背向紋素的高多邊形表面，使縫隙/封閉空間不會抓取對面牆壁。僅在高多邊形繞序不一致時停用。預設值：true。 | BOOLEAN | 是 | true / false |

注意：`low_poly` 必須具有 UV 座標。如果沒有任何 UV 座標，節點會引發錯誤，因為它會烘焙到現有的 UV 佈局上，而不會展開網格。當 `low_poly` 是一個批次時，每個項目會依序烘焙；如果 `high_poly` 只包含一個項目，該項目會重複用於每個批次項目。批次中的空白網格會被跳過並發出警告，產生平坦的中灰色（0.5）法線貼圖。

## 輸出

| 輸出名 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `normal_map` | 烘焙後的切線空間法線貼圖（glTF/OpenGL +Y 慣例），為 resolution × resolution 的正方形 RGB 影像，數值範圍在 [0,1]。將其連接到 Apply Texture To Mesh 的 `normal_map` 輸入。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BakeNormalMapFromMesh/zh-TW.md)

---
**Source fingerprint (SHA-256):** `29df10014b5998b741d71db21d0c982d7bca85ad966a720063af15062e203322`
