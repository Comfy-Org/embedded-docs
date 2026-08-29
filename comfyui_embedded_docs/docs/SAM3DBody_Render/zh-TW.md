# 渲染 3D 身體姿勢

使用可選擇的樣式將 3D 人體姿態資料渲染為影像。此節點接受來自 SAM3D 身體追蹤器 (MHR) 或外部 Y-up 骨架（如 Kimodo）的姿態資料，並可將結果合成於可選的背景影像之上（若未提供則使用黑色畫布）。可用的渲染樣式包括著色的 3D 網格、二進位剪影、2D 與 3D OpenPose 風格骨架，以及 SCAIL 風格的膠囊身體。

## 輸入

### 通用輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `render_style` | 渲染模式。'mesh' = 透過相機光柵化的 3D MHR 網格。'silhouette' = 網格的二進位遮罩。'openpose_2d' = 平面 2D 骨架。'openpose_3d' = 以平坦著色 3D 模型呈現的 OpenPose 骨架。'scail' = SCAIL 3D 膠囊。（預設值："mesh"） | DYNAMIC_COMBO | 是 | "mesh"<br>"silhouette"<br>"openpose_2d"<br>"openpose_3d"<br>"scail" |
| `pose_data` | MHR 姿態資料，或外部 Y-up 骨架的姿態資料 (KimodoSample)。所有渲染樣式皆適用於在其 `_skeleton_override` 中帶有 OpenPose 關節對應的外部骨架 (KimodoSample 即具備此資料)。 | MHR_POSE_DATA or KIMODO_POSE_DATA | 是 | — |
| `background` | 逐幀背景。省略時使用黑色畫布。 | IMAGE | 否 | — |
| `width` | 輸出寬度（像素）。0 = 使用姿態資料的原生 image_size。若僅設定 width/height 其中一項，另一項將依原始比例推導。（預設值：0） | INT | 否 | 0 至 16384, step 8 |
| `height` | 輸出高度（像素）。0 = 使用姿態資料的原生 image_size。若僅設定 width/height 其中一項，另一項將依原始比例推導。（預設值：0） | INT | 否 | 0 至 16384, step 8 |
| `camera_info` | 自由的 6DOF 攝影機覆寫。當連線時，姿態會透過此攝影機（位置/目標/縮放/旋轉/FoV）重新投影，而非使用預測的攝影機。 | LOAD_3D_CAMERA | 否 | — |

### 網格輸入

當 `render_style` 為 "mesh" 時，會顯示以下參數。

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `shader` | 預設著色器。'normals' = 相機空間中的目前表面法線（OpenGL Y+ 法線貼圖慣例：+X→R, +Y→G, +Z→B）。'rainbow' = RealisDance 風格的身體 Y 軸彩虹漸層；'rainbow_face_*' 變體會以法線/區域顏色覆寫臉部頂點；'depth' = 線性灰階。（預設值："default"） | DYNAMIC_COMBO | 否 | "default"<br>"normals"<br>"rainbow"<br>"rainbow_face_normal"<br>"rainbow_face_semantic"<br>"depth" |
| `rainbow_tilt_z` | 繞 Z 軸（前向）旋轉彩虹漸層軸。用於區分左右。僅在 `shader` 為 "rainbow"、"rainbow_face_normal" 或 "rainbow_face_semantic" 時可用。（預設值：-35.0） | FLOAT | 否 | -90.0 至 90.0, step 0.5 |
| `rainbow_tilt_x` | 繞 X 軸（右向）旋轉彩虹漸層軸。用於區分前後。僅在 `shader` 為 "rainbow"、"rainbow_face_normal" 或 "rainbow_face_semantic" 時可用。（預設值：0.0） | FLOAT | 否 | -90.0 至 90.0, step 0.5 |
| `opacity` | 網格在背景影像上的 alpha 值；若未連接背景則為黑色底。（預設值：1.0） | FLOAT | 否 | 0.0 至 1.0, step 0.01 |
| `person_palette_falloff` | 每人的去飽和度（朝白色方向）：第 k 個人物會獲得 (1 - falloff^k) 的粉彩混合（SCAIL「第二人較柔和」效果）。1.0 = 關閉。（預設值：0.6） | FLOAT | 否 | 0.1 至 1.0, step 0.05 |
| `region` | 'hands_only' 會透過預先計算的 `hand_vert_mask`（針對標準手部關鍵點的 LBS 權重）篩選網格面，只留下手部網格以便除錯。若缺少遮罩，則退回完整網格。（預設值："full_body"） | COMBO | 否 | "full_body"<br>"hands_only" |

### 剪影輸入

當 `render_style` 為 "silhouette" 時，此節點會渲染 3D 網格的二進位遮罩。此模式沒有額外參數。

### OpenPose 2D 輸入

當 `render_style` 為 "openpose_2d" 時，會顯示以下參數。

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `marker_radius_px` | 身體關鍵點圓點半徑（像素）。（預設值：4） | INT | 否 | 1 至 32, step 1 |
| `stick_width_px` | 身體肢幹橢圓半寬（像素）。DWPose 預設值 = 4。（預設值：4） | INT | 否 | 1 至 32, step 1 |
| `limb_alpha` | 每個肢體的 alpha 值。DWPose 預設值 = 0.6。（預設值：0.6） | FLOAT | 否 | 0.0 至 1.0, step 0.05 |
| `face_style` | 'full' = 所有臉部特徵點（若有 sapiens-238 則使用，否則使用骨架回退約 30 個點）。'eyes_mouth' = 骨架回退子集（約 12 個點：僅眼睛與外唇）。'disabled' = 不繪製臉部點。（預設值："disabled"） | COMBO | 否 | "disabled"<br>"full"<br>"eyes_mouth" |
| `hand_style` | 繪製 21+21 手部關鍵點與連桿。'disabled' = 不繪製手部。'dwpose' = 實心藍色點；'openpose' = 彩虹色點。（預設值："disabled"） | COMBO | 否 | "disabled"<br>"dwpose"<br>"openpose" |
| `person_palette_falloff` | 每人去飽和度：第 k 個人物以 1 - falloff^k 的比例向白色混合。第 0 個人物保持鮮豔；1.0 停用去飽和。（預設值：0.6） | FLOAT | 否 | 0.1 至 1.0, step 0.05 |

### OpenPose 3D 輸入

當 `render_style` 為 "openpose_3d" 時，會顯示以下參數。

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `radius_m` | 肢體膠囊的半徑（公尺）；數值小則近似棍狀。（預設值：0.015） | FLOAT | 否 | 0.004 至 0.1, step 0.001 |
| `include_hands` | 將 21+21 手部關鍵點繪製為 3D 膠囊。（預設值：True） | BOOLEAN | 否 | True or False |
| `person_palette_falloff` | 每人去飽和度：第 k 個人物以 1 - falloff^k 的比例向白色混合。第 0 個人物保持鮮豔；1.0 停用去飽和。（預設值：0.6） | FLOAT | 否 | 0.1 至 1.0, step 0.05 |

### SCAIL 輸入

當 `render_style` 為 "scail" 時，會顯示以下參數。

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `radius_m` | 膠囊半徑（公尺）（SCAIL 參考值：約 0.022 公尺）。（預設值：0.022） | FLOAT | 否 | 0.005 至 0.2, step 0.001 |
| `hand_style` | 將 2D OpenPose 手部合成在 3D 膠囊身體之上（符合 SCAIL 風格 — 沒有 3D 手部膠囊）。'disabled' = 不繪製手部。'dwpose' = 實心藍色手部點；'openpose' = 彩虹色點。無論何種模式，手指連桿皆保持彩虹色。（預設值："dwpose"） | COMBO | 否 | "disabled"<br>"dwpose"<br>"openpose" |
| `face_style` | 'full' = 所有臉部特徵點（若有 sapiens-238 則使用，否則使用骨架回退約 30 個點）。'eyes_mouth' = 骨架回退子集（約 12 個點：僅眼睛與外唇）。'disabled' = 不繪製臉部點。（預設值："disabled"） | COMBO | 否 | "disabled"<br>"full"<br>"eyes_mouth" |
| `person_palette_falloff` | 每人去飽和度：第 k 個人物以 1 - falloff^k 的比例向白色混合。第 0 個人物保持鮮豔；1.0 停用去飽和。（預設值：0.6） | FLOAT | 否 | 0.1 至 1.0, step 0.05 |

### 備註

- 若 `width` 與 `height` 皆為 0，輸出將使用姿態資料的原生影像尺寸。若僅設定其中一項，另一項會以保留原始長寬比的方式推導。已連接的 `background` 會調整大小以符合渲染解析度。
- 當 `camera_info` 已連接時，姿態會透過該攝影機重新投影，而非使用預測的攝影機。
- 在網格模式下，只有當 `shader` 設定為 "rainbow"、"rainbow_face_normal" 或 "rainbow_face_semantic" 時，`rainbow_tilt_z` 與 `rainbow_tilt_x` 才可用。
- 在網格模式下，當 `region` 為 "hands_only" 時，手部區域篩選需要姿態資料包含手部頂點遮罩；若缺少該遮罩，則改為渲染完整網格。
- 在 scail 模式下，手部一律以 2D 疊加層繪製；沒有 3D 手部膠囊。
- 當輸出解析度與姿態資料的原生解析度不同時，openpose_2d 的標記與連桿大小會按比例縮放。
- 若背景的幀數少於姿態資料，則最後一個背景幀會重複用於其餘幀數。
- 輸出包含每個輸入姿態幀對應的一幀。若姿態資料不包含任何幀，則會回傳一張單一黑色影像。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `影像` | 渲染後的幀：以選定的渲染樣式繪製姿態資料，並在已連接背景時合成於背景之上，否則合成於黑色之上。每個輸入姿態幀對應一幀，並以單一批次影像回傳。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SAM3DBody_Render/zh-TW.md)

---
**Source fingerprint (SHA-256):** `96556283cf07727e6b4bb3549537bf925ed771bab8607f65c93ab54a5f0e9ba5`
