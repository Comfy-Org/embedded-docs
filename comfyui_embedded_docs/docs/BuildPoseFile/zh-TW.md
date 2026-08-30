# 建立 3D 動畫檔案

此節點會從姿勢資料建立可直接儲存的 3D 動畫檔案。您可以匯出多種視覺風格的動畫 GLB——全身網格、僅關節預覽、OpenPose 骨架或 SCAIL 膠囊骨架——也可以改為儲存 BVH 動作捕捉片段。輸出可連接到如 Save 3D Model 等檔案儲存節點，將檔案寫入磁碟。

## 輸入

### 通用輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `pose_data` | 3D 姿勢資料。接受 MHR 姿勢資料（模型/形狀/表情參數、MHR70 關鍵點、標準色彩、手部頂點遮罩）或 Kimodo 姿勢資料（外部 Y-up 骨架，含每幀預測頂點與相機）。 | MHR_POSE_DATA / KIMODO_POSE_DATA | 是 | — |
| `格式` | 輸出格式，兩種格式皆可饋送至 Save 3D Model 以寫入磁碟。'glb' = 動畫 GLB（mesh / bones / openpose / scail）。'bvh' = BVH 動作捕捉片段（單一骨架；需要模型）。（預設：glb） | DYNAMIC_COMBO | 是 | "glb"<br>"bvh" |
| `sam3d_body_model` | 可選的 SAM3D 身體模型。除非姿勢資料帶有骨架覆寫（skeleton override），否則 'bvh'、'body_mesh' 與 'bones_only' 格式需要此模型。 | SAM3D_BODY_MODEL | 否 | — |
| `fps` | 動畫幀率。（預設：24.0） | FLOAT | 是 | 1.0-240.0 |
| `camera_translation` | 將 pred_cam_t 烘焙到根節點的平移：'off' = 綁定位置；'centered' = 與第 0 幀的差值；'absolute' = 原始值（Z 為相機深度——通常以公尺為單位）。（預設：off） | COMBO | 是 | "off"<br>"centered"<br>"absolute" |
| `track_index` | 軌道選取：-1 = 所有軌道；≥0 = 單一軌道。（預設：-1） | INT | 是 | -1 至 15 |

### GLB 輸入

當 `format` 設為 "glb" 時，會顯示這些輸入。

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `mesh_style` | GLB 的視覺風格：'body_mesh' = 真實 Armature（127 根骨骼、蒙皮、TRS 關鍵幀、72 個臉部變形；需要模型）。'bones_only' = 每個關節處的骨骼形狀基本體（預覽骨架）。'openpose' = 由關鍵點產生的 OpenPose-18 3D 骨架。'scail' = SCAIL 3D 膠囊骨架（開放式圓柱體，由關節球體平齊封口）。（預設：body_mesh） | DYNAMIC_COMBO | 是 | "body_mesh"<br>"bones_only"<br>"openpose"<br>"scail" |
| `bone_smooth_window` | 對每根骨骼的旋轉關鍵幀/關鍵點軌道套用的高斯平滑視窗。0 = 關閉。7-15 可平穩上游 Smooth 漏掉尖峰時造成的旋轉/抖動。（預設：0） | INT | 是 | 0-51, step 2 |

#### Body Mesh 輸入

當 `mesh_style` 為 "body_mesh" 時出現。

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `bone_vis` | 骨骼視覺化形狀，剛性蒙皮至每個關節。'off' = 不顯示骨骼視覺化；'octahedrons' = Blender 風格的指向性骨骼。（預設：off） | DYNAMIC_COMBO | 是 | "off"<br>"octahedrons" |
| `bone_vis_radius_m` | 當 `bone_vis` = "octahedrons" 時出現。半徑，單位為 m（球體半徑 / 八面體半寬）。（預設：0.02） | FLOAT | 是 | 0.005-0.5 |
| `bone_vis_color` | 當 `bone_vis` = "octahedrons" 時出現。每根骨骼的頂點顏色（unlit 材質）。'white' = 無，'rainbow_y' = 從頭到腳的 jet 漸層。（預設：rainbow_y） | COMBO | 是 | "white"<br>"rainbow_y" |
| `shader` | 烘焙與 Render 節點著色器相符的每頂點顏色（COLOR_0 + KHR_materials_unlit）。'default' = 無顏色。（預設：default） | DYNAMIC_COMBO | 是 | "default"<br>"rainbow"<br>"rainbow_face_normal"<br>"rainbow_face_semantic" |
| `rainbow_tilt_z` | 當 `shader` 為彩虹變體時出現。繞 Z 軸（前）旋轉彩虹 jet 軸。可區分左/右。（預設：-35.0） | FLOAT | 是 | -90.0 至 90.0 |
| `rainbow_tilt_x` | 當 `shader` 為彩虹變體時出現。繞 X 軸（右）旋轉彩虹 jet 軸。可區分前/後。（預設：0.0） | FLOAT | 是 | -90.0 至 90.0 |
| `person_palette_falloff` | 當 `shader` 為彩虹變體時出現。逐人降低飽和度：每個軌道會取得 (1 - falloff^k) 的粉彩混合。（預設：0.6） | FLOAT | 是 | 0.1-1.0 |

#### Bones Only 輸入

當 `mesh_style` 為 "bones_only" 時出現。

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `bone_vis` | 骨骼視覺化形狀，剛性蒙皮至每個關節。'octahedrons' = Blender 風格的指向性骨骼（關節 → 主要子節點）。 | DYNAMIC_COMBO | 是 | "octahedrons" |
| `bone_vis_radius_m` | 半徑，單位為 m（球體半徑 / 八面體半寬）。（預設：0.02） | FLOAT | 是 | 0.005-0.5 |
| `bone_vis_color` | 每根骨骼的頂點顏色（unlit 材質）。'white' = 無，'rainbow_y' = 從頭到腳的 jet 漸層。（預設：rainbow_y） | COMBO | 是 | "white"<br>"rainbow_y" |

#### OpenPose 輸入

當 `mesh_style` 為 "openpose" 時出現。

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `marker_radius_m` | 球體半徑，單位為 m。（預設：0.010） | FLOAT | 是 | 0.005-0.1 |
| `stick_radius_m` | 肢體半寬，單位為 m。自動限制為 bone_length × 0.1。（預設：0.008） | FLOAT | 是 | 0.002-0.05 |
| `include_hands` | 附加 21+21 個 OpenPose 手部關鍵點（手腕 + 5 根手指 × 4 個關節，基部→指尖），來源為 pred_keypoints_3d。（預設：False） | BOOLEAN | 是 | True / False |
| `hand_marker_radius_m` | 手部球體半徑，單位為 m。（預設：0.005） | FLOAT | 是 | 0.001-0.1 |
| `hand_stick_radius_m` | 手部肢體半寬，單位為 m。（預設：0.003） | FLOAT | 是 | 0.001-0.05 |
| `face_style` | 從 pred_vertices 中依固定頭部網格頂點 ID 取樣的面部輪廓地標（需要 pose_data 上的 canonical_colors）。'full' = 全部約 30 個點；'eyes_mouth' = 僅眼睛 + 外唇。（預設：disabled） | COMBO | 是 | "disabled"<br>"full"<br>"eyes_mouth" |
| `face_marker_radius_m` | 面部點的半徑。0 = 自動 = 0.3 × marker_radius_m。（預設：0.0） | FLOAT | 是 | 0.0-0.05 |

#### SCAIL 輸入

當 `mesh_style` 為 "scail" 時出現。

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `stick_radius_m` | 圓柱體半徑，單位為 m。骨骼是等半徑的開放式圓柱體；關節球體（自動調整大小以配合）封住開放端。SCAIL 參考值 = 0.0215 m。（預設：0.022） | FLOAT | 是 | 0.002-0.1 |
| `marker_radius_m` | 關節球體半徑。0 = 自動 = stick_radius_m（平齊封口）。（預設：0.0） | FLOAT | 是 | 0.0-0.1 |
| `material_roughness` | PBR 粗糙度。SCAIL 參考值 = 0.3。1 = 霧面；0 = 鏡面。（預設：0.3） | FLOAT | 是 | 0.0-1.0 |
| `include_hands` | 每個軌道附加 21+21 個手部關鍵點 + 膠囊棒。（預設：False） | BOOLEAN | 是 | True / False |
| `hand_marker_radius_m` | 手部球體半徑，單位為 m。（預設：0.005） | FLOAT | 是 | 0.001-0.05 |
| `hand_stick_radius_m` | 手部圓柱體半徑，單位為 m。（預設：0.003） | FLOAT | 是 | 0.001-0.05 |
| `face_style` | 從 pred_vertices 取樣的面部輪廓地標（需要 pose_data 上的 canonical_colors）。'full' = 全部約 30 個點；'eyes_mouth' = 僅眼睛 + 外唇。（預設：disabled） | COMBO | 是 | "disabled"<br>"full"<br>"eyes_mouth" |

### BVH 輸入

當 `format` 設為 "bvh" 時，會顯示這些輸入。

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `units` | BVH OFFSET/位置單位。'cm' 是動作捕捉的標準單位。（預設：cm） | COMBO | 是 | "cm"<br>"m" |

**備註：**

- `bvh` 格式以及 `body_mesh` 和 `bones_only` 網格樣式需要 `sam3d_body_model` 輸入，除非 `pose_data` 本身帶有骨架覆寫（例如來自 KimodoSample 節點的 `_skeleton_override` 字典）。若兩者皆無，節點會擲出錯誤。`openpose` 和 `scail` 樣式與骨架無關，可直接從關鍵點運作，不需要身體模型。
- 在 `bvh` 格式中，輸出包含單一骨架。當 `track_index` 為 -1（所有軌道）時，會使用第一個軌道。
- `full` 與 `eyes_mouth` 的 `face_style` 選項需要 pose data 上的 `canonical_colors`；當姿勢資料與身體模型一起從 MHR 流程產生時，即會包含此資料。
- `bone_smooth_window` 在 0 到 51 之間以 2 為步進遞增。

## 輸出

| 輸出名 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `model_3d` | 產生的動畫檔案：動畫 GLB 或 BVH 動作捕捉片段，可使用如 Save 3D Model 等節點儲存至磁碟。 | 3D_FILE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BuildPoseFile/zh-TW.md)

---
**Source fingerprint (SHA-256):** `f3672f0749c4f9affcc92da98198c5b142f6fcd9f5e317ab43dd7e53533c0fa3`
