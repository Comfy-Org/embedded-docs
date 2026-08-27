# BakeAmbientOcclusion

將環境光遮蔽（ambient occlusion）貼圖從高多邊形網格（high-poly mesh）烘焙到低多邊形網格（low-poly mesh）的 UV 佈局中。輸出是一張灰階影像，其中白色紋素（texel）代表開放區域，深色紋素代表裂縫處；此影像用於「Apply Texture To Mesh」節點的 occlusion 輸入。請連接已展開 UV 的低多邊形網格，以及用於精簡出該低多邊形網格的高多邊形網格。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `low_poly` | 要烘焙到的已展開 UV 的低多邊形網格。必須具有 UV；如果缺少 UV，節點會產生錯誤。 | MESH | 是 | - |
| `high_poly` | 低多邊形網格所精簡自的高多邊形網格，作為遮蔽的來源幾何。 | MESH | 是 | - |
| `resolution` | 紋理解析度（像素）；每個紋素會接收一個遮蔽值。預設值：1024。 | INT | 是 | 64 to 8192 (step 64) |
| `samples` | 每個紋素的光線數。越多 = 越平滑，但越慢。如有顆粒感可提高此值。預設值：64。 | INT | 是 | 4 to 1024 (step 4) |
| `max_distance` | 光線長度，以邊界框對角線的比例表示。越小 = 更緊密、更局部的遮蔽。預設值：0.5。 | FLOAT | 是 | 0.01 to 2.0 (step 0.01) |
| `strength` | 縮放遮蔽強度。>1 變暗，<1 變亮。預設值：1.0。 | FLOAT | 是 | 0.0 to 2.0 (step 0.05) |
| `bias` | 光線原點從表面抬升的距離，以邊界框對角線的比例表示。如果平坦表面出現深色斑點或孔洞，請提高此值。預設值：0.01。 | FLOAT | 是 | 0.0001 to 0.2 (step 0.0005) |

注意：`low_poly` 必須具有 UV 座標——此節點永遠不會展開網格。如果 `high_poly` 僅包含一個批次項目，則它會對 `low_poly` 的每個批次項目重複使用；`low_poly` 中沒有面的批次項目會被略過，並以全白影像替代，同時記錄警告。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `occlusion` | 灰階環境光遮蔽影像，數值範圍在 [0,1]（白色 = 開放，深色 = 裂縫），每個 `low_poly` 批次項目對應一張影像。用於「Apply Texture To Mesh」節點的 occlusion 輸入（封裝在 ORM 貼圖 / occlusionTexture 中）。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BakeAmbientOcclusion/zh-TW.md)

---
**Source fingerprint (SHA-256):** `63ea6ce5289728d351fdd7d722e9a299ebb1283e1128262a817466ec6d23786a`
