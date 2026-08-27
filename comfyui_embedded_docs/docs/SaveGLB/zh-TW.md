# SaveGLB

SaveGLB 節點會將 3D 網格資料或 3D 檔案輸入儲存到輸出目錄。它接受網格資料及常見的 3D 檔案格式（GLB、GLTF、OBJ、FBX、STL、USDZ、PLY、SPLAT、SPZ、KSPLAT），並以指定的檔案名稱前綴匯出。網格輸入會以 GLB 檔案寫入，每個批次項目一個檔案，而 3D 檔案輸入則以原始格式儲存。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `mesh` | 要儲存的網格或 3D 檔案 | MESH or FILE3D | 是 | Mesh data<br>GLB<br>GLTF<br>OBJ<br>FBX<br>STL<br>USDZ<br>PLY<br>SPLAT<br>SPZ<br>KSPLAT<br>Any splat format<br>Any point cloud format<br>Any 3D file format |
| `檔名前綴` | 輸出檔案名稱的前綴（預設值："3d/ComfyUI"）。前綴可包含子資料夾路徑，因此檔案預設會儲存在輸出目錄的「3d」子資料夾中 | STRING | 否 | - |

注意：當 `mesh` 輸入是 3D 檔案時，節點會使用其原始格式副檔名儲存（若檔案沒有格式，則使用 GLB）。當輸入是網格資料時，批次中的每個項目會分別儲存為獨立的 `.glb` 檔案；空項目（沒有頂點或面）會被跳過並顯示警告。輸出檔案名稱遵循模式 `{filename_prefix}_{counter:05}_.{ext}`，並使用遞增的計數器。啟用中繼資料時，工作流程中繼資料（提示詞與額外的 PNG 資訊）會嵌入到儲存的檔案中。

## 輸出

| 輸出名 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `ui` | 在使用者介面中顯示已儲存的 3D 檔案，包含檔案名稱、子資料夾與類型資訊 | UI |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveGLB/zh-TW.md)

---
**Source fingerprint (SHA-256):** `366b56c4fd6e3c2f7783222990792a982857b3419a2becfa27ddfa37853bb22c`
