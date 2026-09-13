# 重新網格化網格（窄帶 DC）

Remesh Mesh 會透過取樣原始表面周圍的窄帶距離場，並以 Dual Contouring 擷取該場，來重建具有乾淨、均勻細分的網格。這會將雜亂、非流形或自相交的拓撲正規化，且設計上應在 Decimate Mesh 之前執行，以達到精確的面數。處理會在使用中的運算裝置上執行，且輸出網格會保持焊接狀態。

## 輸入

### 通用輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `網格` | 要重新網格化的輸入網格。 | MESH | 是 | — |
| `解析度` | 體素網格解析度（輸出密度）。256 ~ 100k 面，512 ~ 1M。若要取得精確的面數，請接著使用 Decimate Mesh。（預設值：512） | INT | 是 | 32 - 2048 |
| `sign_mode` | 表面擷取模式。"udf" 對雜亂/非流形輸入具有穩健性；"sdf" 會產生乾淨的單一表面，並搭配 QEF（Quadratic Error Function，二次誤差函式）進行銳利特徵還原，但需要一致的繞向。選取模式後會顯示其特定子選項。（預設值："udf"） | DYNAMIC_COMBO | 是 | "udf"<br>"sdf" |
| `窄帶` | 以體素單位表示的窄帶寬度。在 UDF 模式下也會偏移表面。（進階，預設值：1.0） | FLOAT | 是 | 0.5 - 4.0 |
| `project_back` | 將頂點朝原始表面線性插值（0 = 純 DC，1 = 貼合）。（進階，預設值：0.0） | FLOAT | 是 | 0.0 - 1.0 |
| `fix_poles` | 收合價數為 3 的頂點對（DC T 形接點偽影）。（進階，預設值：false） | BOOLEAN | 是 | true / false |
| `smooth_iters` | Taubin 平滑迭代次數（0 = 關閉）。2-3 可清除 DC 階梯狀偽影；更高會過度平滑 QEF 邊。（預設值：0） | INT | 是 | 0 - 20 |
| `drop_small_components` | 捨棄面數低於最大元件面數此比例的元件。0 表示停用。（進階，預設值：0.01） | FLOAT | 是 | 0.0 - 0.5 |
| `precluster_max_verts` | 在距離場查詢之前限制輸入頂點數；超過此值的輸入會先被叢集簡化至此數量。可避免巨大網格發生 OOM。（進階，預設值：20,000,000） | INT | 是 | 0 - 100,000,000 |

### "udf" 模式輸入

當 `sign_mode` 設為 `"udf"` 時，會顯示這些參數。

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `qef` | 使用 QEF（Quadratic Error Function，二次誤差函式）對偶頂點放置，以獲得更銳利的邊。（進階，預設值：false） | BOOLEAN | 否 | true / false |
| `drop_inverted_components` | 捨棄向內法線（負體積）的封閉元件 — UDF 內殼。（進階，預設值：false） | BOOLEAN | 否 | true / false |
| `drop_enclosed_components` | 捨棄位於最大元件 bbox 內、且未通過網格內點射線檢測的元件。若為合法的巢狀零件，請停用此選項。（進階，預設值：false） | BOOLEAN | 否 | true / false |

### "sdf" 模式輸入

當 `sign_mode` 設為 `"sdf"` 時，會顯示這些參數。

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `qef` | QEF（Quadratic Error Function，二次誤差函式）對偶頂點放置（可還原銳利特徵），而非邊交叉質心。（預設值：true） | BOOLEAN | 否 | true / false |
| `manifold` | Manifold Dual Contouring：在多薄片情況下，每個體素使用 1-4 個對偶頂點。較慢。（預設值：false） | BOOLEAN | 否 | true / false |

注意：`qef` 選項的預設值會依所選模式而異 — 在 "udf" 模式中為 false，在 "sdf" 模式中為 true。當 `precluster_max_verts` 大於 0，且輸入網格的頂點數超過此值時，網格會在距離場查詢之前先被叢集簡化至該目標值。處理完成後，節點會顯示輸入至輸出的面數變化（例如，"faces: 1.23M → 200K (-84%)"）。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `mesh` | 重新網格化後的網格，具有均勻細分與焊接拓撲。若輸入含有頂點顏色，會予以保留；任何 UV、法線與切線都不會保留。 | MESH |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RemeshMesh/zh-TW.md)

---
**Source fingerprint (SHA-256):** `aa9b7e4465196fab81a4a484ca9dd03d999b4621a611aed2b39d618e53702a06`
