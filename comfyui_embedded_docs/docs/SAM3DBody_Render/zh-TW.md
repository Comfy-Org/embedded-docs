# 渲染 3D 身體姿勢

使用可選樣式將 3D 身體姿態資料渲染為影像。此節點接受來自 SAM3D 身體追蹤器 (MHR) 或外部 Y-up 骨架（例如 Kimodo）的姿態資料，並可將結果合成到選填的背景影像上（若未提供則為黑色畫布）。可用的渲染樣式包括著色 3D 網格、二值剪影、2D 與 3D OpenPose 風格骨架，以及 SCAIL 風格的身體膠囊。

## 輸入

### 通用輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `render_style` | 渲染模式。'mesh' = 透過相機光柵化的 3D MHR 網格。'silhouette' = 網格的二值遮罩。'openpose_2d' = 平面 2D 骨架。'openpose_3d' = 以平面著色 3D 模型呈現的 OpenPose 骨架。'scail' = SCAIL 3D 膠囊。（預設值："mesh"） | DYNAMIC_COMBO | 是 | "mesh"<br>"silhouette"<br>"openpose_2d"<br>"openpose_3d"<br>"scail" |
| `pose_data` | MHR 姿態資料，或外部 Y-up 骨架姿態資料 (KimodoSample)。所有渲染樣式都適用於在其 `_skeleton_override` 中帶有 OpenPose 關節映射的外部骨架（KimodoSample 即是如此）。 | MHR_POSE_DATA or KIMODO_POSE_DATA | 是 | — |
| `background` | 逐幀背景。省略 = 黑色畫布。 | IMAGE | 否 | — |
| `width` | 輸出寬度（像素）。0 = 使用姿態資料的原生 image_size。若僅設定 `width`/`height` 其中之一，則會推導另一個並保留原始長寬比。（預設值：0） | INT | 否 | 0 至 16384, step 8 |
| `height` | 輸出高度（像素）。0 = 使用姿態資料的原生 image_size。若僅設定 `width`/`height` 其中之一，則會推導另一個並保留原始長寬比。（預設值：0） | INT | 否 | 0 至 16384, step 8 |
| `camera_info` | 自由 6DOF 相機覆寫。連接後，姿態會透過此相機（position/target/zoom/rotation/FoV）重新投影，而不是使用預測的相機。 | LOAD_3D_CAMERA | 否 | — |

### Mesh 輸入

當 `render_style` 為 "mesh" 時，會顯示這些參數。

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `shader` | 預設著色器。'normals' = 相機空間中的目前表面法線（OpenGL Y+ 法線貼圖慣例：+X→R、+Y→G、+Z→B）。'rainbow' = RealisDance 風格的 body-Y jet；'rainbow_face_*' 變體會以法線/各區域顏色覆寫臉部頂點；'depth' = 線性灰階。（預設值："default"） | DYNAMIC_COMBO | 否 | "default"<br>"normals"<br>"rainbow"<br>"rainbow_face_normal"<br>"rainbow_face_semantic"<br>"depth" |
| `rainbow_tilt_z` | 繞 Z 軸（前方）旋轉彩虹 jet 軸。用於區分左/右。僅當 `shader` 為 "rainbow"、"rainbow_face_normal" 或 "rainbow_face_semantic" 時可用。（預設值：-35.0） | FLOAT | 否 | -90.0 至 90.0, step 0.5 |
| `rainbow_tilt_x` | 繞 X 軸（右方）旋轉彩虹 jet 軸。用於區分前/後。僅當 `shader` 為 "rainbow"、"rainbow_face_normal" 或 "rainbow_face_semantic" 時可用。（預設值：0.0） | FLOAT | 否 | -90.0 至 90.0, step 0.5 |
| `opacity` | 網格在背景影像上的 alpha，或在未連接背景時疊在黑色上的 alpha。（預設值：1.0） | FLOAT | 否 | 0.0 至 1.0, step 0.01 |
| `person_palette_falloff` | 每個人員朝向白色的去飽和：追蹤 k 會得到 (1 - falloff^k) 的粉彩混合（SCAIL「較柔和的第二人」）。1.0 = 關閉。（預設值：0.6） | FLOAT | 否 | 0.1 至 1.0, step 0.05 |
| `region` | 'hands_only' 會透過預先計算的 `hand_vert_mask`（相對於標準手部 KPs 的 LBS 權重）篩選面 — 將手部網格隔離出來以進行除錯。若遮罩缺失，則回退為完整網格。（預設值："full_body"） | COMBO | 否 | "full_body"<br>"hands_only" |

### Silhouette 輸入

當 `render_style` 為 "silhouette" 時，此節點會渲染 3D 網格的二值遮罩。此模式沒有其他參數。

### OpenPose 2D 輸入

當 `render_style` 為 "openpose_2d" 時，會顯示這些參數。

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `marker_radius_px` | 身體關鍵點圓點半徑（px）。（預設值：4） | INT | 否 | 1 至 32, step 1 |
| `stick_width_px` | 身體肢體橢圓半寬（px）。DWPose 預設值 = 4。（預設值：4） | INT | 否 | 1 至 32, step 1 |
| `limb_alpha` | 每個肢體的 alpha。DWPose 預設值 = 0.6。（預設值：0.6） | FLOAT | 否 | 0.0 至 1.0, step 0.05 |
| `face_style` | 'full' = 所有臉部特徵點（若有 sapiens-238，否則使用骨架回退約 30 個）。'eyes_mouth' = 骨架回退子集（約 12 個點：僅眼睛 + 外唇）。'disabled' = 不顯示臉部點。（預設值："disabled"） | COMBO | 否 | "disabled"<br>"full"<br>"eyes_mouth" |
| `hand_style` | 繪製 21+21 手部關鍵點 + 連線。'disabled' = 不顯示手部。'dwpose' = 純藍色圓點；'openpose' = 彩虹圓點。（預設值："disabled"） | COMBO | 否 | "disabled"<br>"dwpose"<br>"openpose" |
| `person_palette_falloff` | 每個人員的去飽和：追蹤 k 會以 1 - falloff^k 混合至白色。追蹤 0 保持鮮豔；1.0 會停用衰減。（預設值：0.6） | FLOAT | 否 | 0.1 至 1.0, step 0.05 |

### OpenPose 3D 輸入

當 `render_style` 為 "openpose_3d" 時，會顯示這些參數。

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `radius_m` | 肢體膠囊半徑（公尺）（越細 = 越像連線）。（預設值：0.015） | FLOAT | 否 | 0.004 至 0.1, step 0.001 |
| `include_hands` | 將 21+21 手部關鍵點繪製為 3D 膠囊。（預設值：True） | BOOLEAN | 否 | True or False |
| `person_palette_falloff` | 每個人員的去飽和：追蹤 k 會以 1 - falloff^k 混合至白色。追蹤 0 保持鮮豔；1.0 會停用衰減。（預設值：0.6） | FLOAT | 否 | 0.1 至 1.0, step 0.05 |

### SCAIL 輸入

當 `render_style` 為 "scail" 時，會顯示這些參數。

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `radius_m` | 膠囊半徑（公尺）（SCAIL 參考值：約 0.022 m）。（預設值：0.022） | FLOAT | 否 | 0.005 至 0.2, step 0.001 |
| `hand_style` | 將 2D OpenPose 手部合成到 3D 膠囊身體上（符合 SCAIL — 沒有 3D 手部膠囊）。'disabled' = 不顯示手部。'dwpose' = 純藍色手部圓點；'openpose' = 彩虹圓點。無論哪種，連線都會保持每指彩虹色。（預設值："dwpose"） | COMBO | 否 | "disabled"<br>"dwpose"<br>"openpose" |
| `face_style` | 'full' = 所有臉部特徵點（若有 sapiens-238，否則使用骨架回退約 30 個）。'eyes_mouth' = 骨架回退子集（約 12 個點：僅眼睛 + 外唇）。'disabled' = 不顯示臉部點。（預設值："disabled"） | COMBO | 否 | "disabled"<br>"full"<br>"eyes_mouth" |
| `person_palette_falloff` | 每個人員的去飽和：追蹤 k 會以 1 - falloff^k 混合至白色。追蹤 0 保持鮮豔；1.0 會停用衰減。（預設值：0.6） | FLOAT | 否 | 0.1 至 1.0, step 0.05 |

### 注意事項

- 如果 `width` 和 `height` 都為 0，輸出會使用姿態資料的原生影像尺寸。若僅設定其中一個，則會推導另一個並保留原始長寬比。連接的 `background` 會調整大小以符合渲染解析度。
- 連接 `camera_info` 時，姿態會透過該相機重新投影，而不是使用預測的相機。
- 在 mesh 模式中，僅當 `shader` 設為 "rainbow"、"rainbow_face_normal" 或 "rainbow_face_semantic" 時，才能使用 `rainbow_tilt_z` 和 `rainbow_tilt_x`。
- 在 mesh 模式中，當 `region` 為 "hands_only" 時，手部區域篩選需要姿態資料包含手部頂點遮罩；若遮罩缺失，則改為渲染完整網格。
- 在 scail 模式中，手部會以 2D OpenPose 疊加層繪製在 3D 膠囊身體上，而不是繪製為 3D 膠囊；將 `hand_style` 設為 "disabled" 會完全移除它們。
- 當輸出解析度與姿態資料的原生解析度不同時，openpose_2d 的標記與連線大小會按比例縮放。
- 如果背景的影格數少於姿態資料，最後一個背景影格會重複用於剩餘影格。
- 輸出會為每個輸入姿態影格包含一個影格。如果姿態資料不含任何影格，則會傳回單一黑色影像。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `image` | 渲染後的影格：以選定的渲染樣式繪製姿態資料，並在連接背景時合成到背景上，否則合成到黑色上。每個輸入姿態影格對應一個影格，並以單一批次影像傳回。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SAM3DBody_Render/zh-TW.md)

---
**Source fingerprint (SHA-256):** `96556283cf07727e6b4bb3549537bf925ed771bab8607f65c93ab54a5f0e9ba5`
