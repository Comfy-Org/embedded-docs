# 從網格烘焙法線貼圖

此節點將高多邊形網格的切線空間法線貼圖烘焙到低多邊形網格的 UV 佈局上，以捕捉減面過程中遺失的表面細節。連接已展開 UV 的低多邊形網格與其來源高多邊形網格，節點會輸出可直接用於 Apply Texture To Mesh 的 `normal_map` 輸入的影像。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `low_poly` | 接收烘焙細節的已展開 UV 低多邊形網格。必須已有 UV；此節點不會進行展開。 | MESH | 是 | — |
| `high_poly` | 其表面細節會烘焙到低多邊形網格 UV 佈局中的高多邊形網格。 | MESH | 是 | — |
| `resolution` | 方形輸出法線貼圖的邊長（以像素為單位，預設：1024）。 | INT | 是 | 64 至 8192 （步進值：64） |
| `cage_distance` | 表面搜尋帶狀範圍，以邊界框對角線的比例表示。在大量減面後若出現錯誤/缺失區塊，請調高；若它跨越間隙抓取，請調低。預設：0.05。 | FLOAT | 是 | 0.001 至 0.5 （步進值：0.001） |
| `ignore_backfaces` | 略過背向紋素的高多邊形表面，使裂隙/封閉空間不會抓到對向牆壁。僅在高多邊形繞序不一致時停用。預設：true。 | BOOLEAN | 是 | true / false |

注意：`low_poly` 必須有 UV 座標。如果沒有，節點會引發錯誤，因為它會烘焙到現有的 UV 佈局上，不會展開網格。當 `low_poly` 是批次時，每個項目會依序烘焙；如果 `high_poly` 只包含一個項目，該項目會重複用於每個批次項目。批次中的空網格會被跳過並發出警告，並產生平坦的中灰色 (0.5) 法線貼圖。如果低多邊形網格的 UV 超出 [0,1] 範圍，它們會均勻擬合到 [0,1]（當佈局看起來是平鋪/UDIM 時會發出警告），因此烘焙與 Apply Texture To Mesh 會使用相同的 UV。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `normal_map` | 烘焙後的切線空間法線貼圖（glTF/OpenGL +Y 慣例），為 resolution × resolution 的方形 RGB 影像，數值範圍在 [0,1]。將其連接到 Apply Texture To Mesh 的 `normal_map` 輸入。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BakeNormalMapFromMesh/zh-TW.md)

---
**Source fingerprint (SHA-256):** `29df10014b5998b741d71db21d0c982d7bca85ad966a720063af15062e203322`
