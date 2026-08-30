# 將臉部表情轉為 SAM3D 身體

此節點透過使用 MediaPipe Face Landmarker 在影像中偵測臉部，將每個偵測到的臉部對應到已追蹤的人物，並將 52 個 ARKit 混合形狀（blendshapes）映射到 MHR 的 72 軸表情參數，從而為 SAM3D 身體添加臉部表情。然後它會重新執行身體模型，使輸出的網格頂點和關鍵點與新的表情相匹配。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `sam3d_body_model` | 包含用於偵測臉部及重新生成身體網格的臉部地標偵測器的 SAM3D 身體模型。 | SAM3D_BODY_MODEL | 是 | - |
| `mhr_pose_data` | 包含逐幀追蹤人物（含邊界框、關鍵點與表情參數）的姿勢資料。此節點將每個偵測到的臉部對應到一個人，並將更新後的表情參數寫入此資料。 | MHR_POSE_DATA | 是 | - |
| `image` | 用於偵測臉部的影像幀。如果影像批次中的幀數少於姿勢資料，則最後一幀會重複用於其餘幀。 | IMAGE | 是 | - |
| `strength` | 所有混合形狀的整體倍率。>1 會誇大效果。預設：1.0。 | FLOAT | 否 | 0.0 至 4.0 (step 0.05, default 1.0) |
| `mouth_strength` | 嘴巴/下巴形狀的倍率。MediaPipe 的 jawOpen 在接近 1.0 時飽和。預設：1.0。 | FLOAT | 否 | 0.0 至 4.0 (step 0.05, default 1.0) |
| `eye_strength` | 眼睛形狀的倍率。MediaPipe 很少超過 0.5；通常需要 2-3 倍。預設：2.0。 | FLOAT | 否 | 0.0 至 4.0 (step 0.05, default 2.0) |
| `brow_strength` | 眉毛/臉頰/嗤笑形狀的倍率。MediaPipe 輸出約 0.1-0.3；建議 2-3 倍。預設：2.0。 | FLOAT | 否 | 0.0 至 4.0 (step 0.05, default 2.0) |
| `input_threshold` | MediaPipe 原始輸出的死區（低於此值設為零，高於此值進行線性重新映射）。預設：0.02。 | FLOAT | 否 | 0.0 至 0.5 (step 0.01, default 0.02) |
| `blendshape_smooth_window` | 在 MHR 映射之前，對 MediaPipe 的逐幀訊號套用高斯視窗。MediaPipe 的原始輸出在靜態臉部上會逐幀波動 30-70%。1 = 停用。請使用奇數值。預設：7。 | INT | 否 | 1 至 31 (step 2, default 7) |

注意：僅當片段中至少有 30 個幀包含偵測到的人物時，才會套用每個片段的基線減除。每個人物最多 12 幀的偵測間隙會透過插值填補。

## 輸出

| 輸出名 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `mhr_pose_data` | 更新後的姿勢資料。每個追蹤人物的表情參數都會被替換為映射後的臉部表情，並重新生成網格頂點和關鍵點以與之匹配。 | MHR_POSE_DATA |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SAM3DBody_FaceExpression/zh-TW.md)

---
**Source fingerprint (SHA-256):** `b2299e51be3556e639d5b04fcbee541ecf41e0d84c2c8a0fd4e211b2f6caba0b`
