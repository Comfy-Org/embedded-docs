# 將臉部表情轉為 SAM3D 身體

此節點透過使用 MediaPipe Face Landmarker 偵測影像中的人臉，將每個偵測到的人臉與追蹤的人物配對，並將 52 個 ARKit 混合形狀映射到 MHR 的 72 軸表情參數，藉此為 SAM3D 身體加入面部表情。接著會重新執行身體模型，使輸出的網格頂點與關鍵點反映新的表情。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `sam3d_body_model` | 包含用於偵測人臉並重新產生身體網格的人臉特徵點偵測器的 SAM3D 身體模型。 | SAM3D_BODY_MODEL | 是 | - |
| `mhr_pose_data` | 包含逐幀追蹤人物及其邊界框、關鍵點與表情參數的姿勢資料。此節點會將每個偵測到的人臉與人物配對，並將更新後的表情參數寫入此資料。 | MHR_POSE_DATA | 是 | - |
| `image` | 用於偵測人臉的影像幀。若影像批次的幀數少於姿勢資料，剩餘幀會重複使用最後一幀。 | IMAGE | 是 | - |
| `strength` | 所有混合形狀的全域乘數。>1 會誇大效果。預設：1.0。 | FLOAT | 否 | 0.0 至 4.0 (step 0.05, default 1.0) |
| `mouth_strength` | 嘴部/下顎形狀的乘數。MediaPipe 的 jawOpen 在接近 1.0 時會飽和。預設：1.0。 | FLOAT | 否 | 0.0 至 4.0 (step 0.05, default 1.0) |
| `eye_strength` | 眼部形狀的乘數。MediaPipe 很少超過 0.5；通常需要 2-3 倍。預設：2.0。 | FLOAT | 否 | 0.0 至 4.0 (step 0.05, default 2.0) |
| `brow_strength` | 眉毛/臉頰/皺鼻形狀的乘數。MediaPipe 輸出約 0.1-0.3；需 2-3 倍。預設：2.0。 | FLOAT | 否 | 0.0 至 4.0 (step 0.05, default 2.0) |
| `input_threshold` | MediaPipe 原始輸出的死區（低於 = 零，高於 = 線性重新映射）。預設：0.02。 | FLOAT | 否 | 0.0 至 0.5 (step 0.01, default 0.02) |
| `blendshape_smooth_window` | 在 MHR 映射之前，套用於 MediaPipe 逐幀訊號的高斯視窗。在靜態臉部上，MediaPipe 的原始輸出會在幀與幀之間擺動 30-70%。1 = 停用。請使用奇數值。預設：7。 | INT | 否 | 1 至 31 (step 2, default 7) |

注意：只有在片段中至少有 30 幀包含偵測到的人物時，才會套用每個片段的基準減除。每個人最多 12 幀的偵測缺口會以插值填補。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `mhr_pose_data` | 更新後的姿勢資料。每個追蹤人物的表情參數會替換為映射後的人臉表情，並重新產生網格頂點與關鍵點以相符。 | MHR_POSE_DATA |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SAM3DBody_FaceExpression/zh-TW.md)

---
**Source fingerprint (SHA-256):** `b2299e51be3556e639d5b04fcbee541ecf41e0d84c2c8a0fd4e211b2f6caba0b`
