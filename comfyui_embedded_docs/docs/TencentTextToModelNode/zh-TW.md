# Hunyuan3D：文字轉模型（專業版）

此節點使用騰訊的 Hunyuan3D Pro API，從文字描述生成 3D 模型。它會發送請求以建立生成任務，輪詢結果，並下載最終的 GLB 和 OBJ 格式模型檔案。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `模型` | 要使用的 Hunyuan3D 模型版本。`3.1` 模型不提供 LowPoly 選項。 | COMBO | 是 | `"3.0"`<br>`"3.1"` |
| `提示詞` | 要生成的 3D 模型的文字描述。最多支援 1024 個字元。 | STRING | 是 | - |
| `面數` | 生成的 3D 模型的目標面數。預設值：500000。 | INT | 是 | 3000 - 1500000 |
| `生成類型` | 要生成的 3D 模型類型。可用的選項及其相關參數如下：<br>- **Normal**：生成標準模型。包含一個 `pbr` 參數（預設值：`False`）。<br>- **LowPoly**：生成低多邊形模型。包含 `polygon_type`（`"triangle"` 或 `"quadrilateral"`）和 `pbr`（預設值：`False`）參數。<br>- **Geometry**：生成僅幾何形狀的模型。 | DYNAMICCOMBO | 是 | `"Normal"`<br>`"LowPoly"`<br>`"Geometry"` |
| `種子` | 生成用的種子值。無論種子為何，結果都是非確定性的。設定新的種子值可控制節點是否應重新執行。預設值：0。 | INT | 否 | 0 - 2147483647 |

**注意：** `generate_type` 參數是動態的。選擇 `"LowPoly"` 將會顯示 `polygon_type` 和 `pbr` 的額外輸入。選擇 `"Normal"` 將會顯示 `pbr` 的輸入。選擇 `"Geometry"` 則不會顯示任何額外輸入。

**限制：** `"LowPoly"` 生成類型不能與 `"3.1"` 模型一起使用。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `GLB` | 為向後相容性保留的舊版輸出。 | STRING |
| `OBJ` | 以 GLB 檔案格式生成的 3D 模型。 | FILE3DGLB |
| `texture_image` | 以 OBJ 檔案格式生成的 3D 模型。 | FILE3DOBJ |
| `texture_image` | 從生成的 OBJ 檔案中提取的紋理影像（如果有的話）。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TencentTextToModelNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `e35f5165941cc7761639dd72e78141326d37d5e169be9a0e326afcbcdc572b7d`
