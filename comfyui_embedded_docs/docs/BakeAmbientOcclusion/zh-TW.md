# BakeAmbientOcclusion

將高多邊形網格烘焙出環境光遮蔽貼圖，對應到低多邊形網格的 UV 佈局。輸出為灰階影像，其中白色紋素代表開放區域，深色紋素代表縫隙區域；此貼圖供 Apply Texture To Mesh 節點的 occlusion 輸入使用。請連接已展開 UV 的低多邊形網格，以及其減面來源的高多邊形網格。

## 輸入
| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `low_poly` | 要烘焙到的 UV 已展開低多邊形網格。必須具有 UV；若缺少 UV，節點會拋出錯誤。 | MESH | 是 | - |
| `high_poly` | 低多邊形網格減面來源的高多邊形網格，用作遮蔽的來源幾何。 | MESH | 是 | - |
| `resolution` | 紋素解析度（像素）；每個紋素接收一個遮蔽值。預設值：1024。 | INT | 是 | 64 至 8192 (step 64) |
| `samples` | 每個紋素的射線數。越多 = 越平滑、越慢。若出現顆粒感請調高。預設值：64。 | INT | 是 | 4 至 1024 (step 4) |
| `max_distance` | 射線長度，以邊界框對角線的比例表示。越小 = 越緊湊、更局部性的遮蔽。預設值：0.5。 | FLOAT | 是 | 0.01 至 2.0 (step 0.01) |
| `strength` | 縮放遮蔽強度。>1 變暗，<1 變亮。預設值：1.0。 | FLOAT | 是 | 0.0 至 2.0 (step 0.05) |
| `bias` | 射線原點自表面抬升的高度，以邊界框對角線的比例表示。若平坦表面也出現暗斑或孔洞，請調高。預設值：0.01。 | FLOAT | 是 | 0.0001 至 0.2 (step 0.0005) |

注意：`low_poly` 必須具有 UV 座標——此節點絕不會自動展開網格。若 `high_poly` 僅包含一個批次項目，該項目會重複用於 `low_poly` 的每個批次項目；`low_poly` 中沒有面的批次項目會被跳過，並以全白影像取代，同時記錄警告。

## 輸出
| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `occlusion` | 灰階環境光遮蔽影像，數值介於 [0,1]（白色 = 開放區域，深色 = 縫隙），每個 `low_poly` 批次項目對應一張影像。供 Apply Texture To Mesh 節點的 occlusion 輸入使用（包裝於 ORM map / occlusionTexture 中）。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BakeAmbientOcclusion/zh-TW.md)

---
**Source fingerprint (SHA-256):** `63ea6ce5289728d351fdd7d722e9a299ebb1283e1128262a817466ec6d23786a`
