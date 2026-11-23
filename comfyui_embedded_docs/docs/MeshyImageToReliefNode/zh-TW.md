# Meshy: Image to Relief

此節點會將照片轉換為浮雕模型，另附 16 位元深度圖，用於 3D 列印、雷射雕刻與 CNC 雕刻。淺色背景上的深色圖案會凸起，淺色區域則保持低平。只會產生並下載你有連接的輸出，因此若未連接任何模型輸出，任務只會回傳深度圖。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `image` | 要轉換成浮雕的照片。淺色背景上的深色圖案會凸起。上傳前會移除透明度，因此請先將透明標誌平面化到白色背景上。 | IMAGE | 是 | 單張圖片 |
| `relief_type` | 雕刻預設集。`"low"` 是較淺的雕刻，適用於雷射雕刻、CNC 加工與牌匾；`"high"` 較深，適用於 3D 列印成品。此預設集會選擇 `carving_depth_mm` 的值。 | DYNAMIC_COMBO | 是 | `"low"`<br>`"high"` |
| `carving_depth_mm` | 雕刻深度，單位為毫米。當設定 `relief_type` 時可用（預設：`"low"` 為 3.0，`"high"` 為 6.0）。 | FLOAT | 是 | 0.1 至 60.0（步進值：0.1） |
| `size_mm` | 模型上照片長邊的長度，單位為毫米，以任何彎曲前的平面狀態測量（預設：60.0）。 | FLOAT | 是 | 20.0 至 250.0（步進值：1.0） |
| `carving_mode` | `"emboss"` 會將照片中較近的部分凸起，`"engrave"` 則將其刻入。 | COMBO | 是 | `"emboss"`<br>`"engrave"` |
| `base` | `"plate"` 會在浮雕下方保留底板，`"none"` 會切除背景且不建立底板。選取選項後會顯示其參數。 | DYNAMIC_COMBO | 是 | `"plate"`<br>`"none"` |
| `base_thickness_mm` | 底板厚度，單位為毫米。當 `base` 為 `"plate"` 時可用（預設：1.0）。 | FLOAT | 是 | 0.1 至 10.0（步進值：0.1） |
| `removal_threshold` | 在 0 至 1 的深度圖上，低於此深度的背景會被切除。0.3 可保留完整半身像，0.8 會使其破碎成片段。當 `base` 為 `"none"` 時可用（預設：0.01）。 | FLOAT | 是 | 0.01 至 1.0（步進值：0.01） |
| `bend` | `"convex"` 會使正面向外凸起，`"concave"` 會使其向內彎曲，`"off"` 則保持浮雕平坦。選取彎曲選項後會顯示 `bend_axis` 與 `bend_angle`。 | DYNAMIC_COMBO | 是 | `"off"`<br>`"convex"`<br>`"concave"` |
| `bend_axis` | `"xz"` 會捲曲左右邊緣，`"yz"` 則捲曲上下邊緣。當 `bend` 為 `"convex"` 或 `"concave"` 時可用。 | COMBO | 是 | `"xz"`<br>`"yz"` |
| `bend_angle` | 彎曲所跨越的弧度，單位為度；360 會將浮雕閉合成圓柱。當 `bend` 為 `"convex"` 或 `"concave"` 時可用（預設：60.0）。 | FLOAT | 是 | 1.0 至 360.0（步進值：1.0） |
| `seed` | 控制節點是否重新執行的種子；無論種子為何，結果都是非確定性的。若要在上次執行後要求產生已連接的輸出，請變更此值（預設：42）。 | INT | 是 | 0 至 2147483647 |
| `mesh_resolution` | 沿照片長邊的網格點數。1024 時，GLB 約 50 MB、STL 約 105 MB；2048 時約 200 MB 與 420 MB；若有彎曲，大小會加倍。（預設：1024；進階選項） | INT | 是 | 512 至 2048 |
| `color_mapping` | 使用照片為 GLB、OBJ、FBX 與 USDZ 檔案上色。STL 與 3MF 保持白色。（預設：False；進階選項） | BOOLEAN | 是 | True 或 False |

**注意：** 只有當模型格式的輸出有連接時，才會產生並下載該格式。若未連接任何模型輸出，任務只會回傳深度圖；單獨連接 `preview` 時，仍會為縮圖產生模型，但不會回傳模型檔案。`depth_map` 會保留完整的 16 位元範圍；Save Image (Advanced) 會將其寫入為 16 位元 PNG。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `GLB` | 以 GLB 格式下載的浮雕模型。 | FILE3DGLB |
| `STL` | 以 STL 格式下載的浮雕模型。 | FILE3DSTL |
| `OBJ` | 以 OBJ 格式下載的浮雕模型。 | FILE3DOBJ |
| `FBX` | 以 FBX 格式下載的浮雕模型。 | FILE3DFBX |
| `USDZ` | 以 USDZ 格式下載的浮雕模型。 | FILE3DUSDZ |
| `3MF` | 以 3MF 格式下載的浮雕模型。 | FILE3D |
| `depth_map` | 保留完整 16 位元範圍的深度圖；Save Image (Advanced) 會將其寫入為 16 位元 PNG。 | IMAGE |
| `preview` | 由 Meshy 為完成後的浮雕所渲染的縮圖。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyImageToReliefNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `6f2f0eb49074281b99d7ee10daf3bcc5616c6596c1c4d8491c72739550395f52`
