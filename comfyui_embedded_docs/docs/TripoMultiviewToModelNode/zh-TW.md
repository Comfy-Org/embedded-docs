# Tripo：多視角轉模型

此節點使用 Tripo 的 API，透過處理最多四張顯示物件不同視角的影像（正面、左側、背面、右側）來同步生成 3D 模型。它需要一張正面影像以及至少一個額外視角（左側、背面或右側）才能建立 3D 模型。可從此節點控制紋理、PBR 材質、幾何品質與輸出格式。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `圖像` | 物件的正面視角影像。 | IMAGE | 是 | - |
| `左側圖像` | 物件的左側視角影像。 | IMAGE | 否 | - |
| `後方圖像` | 物件的背面視角影像。 | IMAGE | 否 | - |
| `右側圖像` | 物件的右側視角影像。 | IMAGE | 否 | - |
| `model_version` | 用於生成的模型版本。 | COMBO | 否 | 提供多個選項 |
| `orientation` | 3D 模型的方向設定（預設：`"default"`）。 | COMBO | 否 | 提供多個選項 |
| `texture` | 生成紋理貼圖。關閉時會傳回裸幾何，並忽略 `pbr`。（預設：True） | BOOLEAN | 否 | - |
| `pbr` | PBR 材質貼圖（base color、metallic、roughness、normal）。需要 `texture`。（預設：True） | BOOLEAN | 否 | - |
| `model_seed` | 模型生成的隨機種子（預設：42）。 | INT | 否 | 0 到 2,147,483,647 |
| `texture_seed` | 紋理生成的隨機種子（預設：42）。 | INT | 否 | 0 到 2,147,483,647 |
| `texture_quality` | 紋理生成的品質等級（預設：`"standard"`）。`"detailed"` = HD 紋理，`"extreme"` = 8K Ultra 紋理。 | COMBO | 否 | `"standard"`<br>`"detailed"`<br>`"extreme"` |
| `texture_alignment` | 用於將紋理對齊到模型的方法（預設：`"original_image"`）。 | COMBO | 否 | `"original_image"`<br>`"geometry"` |
| `face_limit` | 最大面數。-1 會讓 Tripo 自適應選擇（在 v3.x standard 上約 1.4M 面，detailed 約 2M）。Tripo 會默默限制：四邊形網格為 150,000。（預設：-1） | INT | 否 | -1 到 2,000,000 |
| `quad` | 四邊形網格輸出。Tripo 以 FBX 格式提供四邊形網格，因此結果會出現在 FBX 輸出，而 GLB 輸出會保持為空。（預設：False） | BOOLEAN | 否 | - |
| `幾何品質` | 幾何生成的品質等級（預設：`"standard"`）。 | COMBO | 否 | `"standard"`<br>`"detailed"` |
| `smart_low_poly` | 低多邊形網格，具有乾淨、手工風格的拓撲（500-20,000 面，四邊形 500-10,000）。最適合簡單主體；複雜主體可能會失敗。（預設：False） | BOOLEAN | 否 | - |
| `auto_size` | 將有紋理的模型縮放到以公尺為單位的真實世界尺寸。Tripo 會將尺寸儲存為模型的場景變換，並在模型被轉換、綁定或重新定向時烘焙進去；沒有紋理時會被忽略。（預設：False） | BOOLEAN | 否 | - |

**注意：** 正面影像（`image`）一律為必填，且必須額外提供 `image_left`、`image_back` 或 `image_right` 其中至少一個。關閉 `texture` 也會自動關閉 `pbr`，因為 `pbr` 需要 `texture`。啟用 `smart_low_poly` 且 `face_limit` 未設為 -1 時，三角形網格的 `face_limit` 必須介於 500 到 20,000 之間，四邊形網格則必須介於 500 到 10,000 之間。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `模型檔案` | 生成的 3D 模型檔案路徑或識別碼（僅供向後相容）。 | STRING |
| `模型任務 ID` | 用於追蹤模型生成程序的任務識別碼。 | MODEL_TASK_ID |
| `GLB` | 生成的 GLB 格式 3D 模型檔案。啟用 `quad` 時為空。 | FILE3DGLB |
| `FBX` | 生成的 FBX 格式 3D 模型檔案。僅在啟用 `quad` 時填入。 | FILE3DFBX |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoMultiviewToModelNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `b66df4cad6167fa27edf1fe21b96cb47af90027b3fbe0a3c9c14101506281ed7`
