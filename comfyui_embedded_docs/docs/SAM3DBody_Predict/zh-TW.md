# 執行 SAM3D 身體預測

SAM3D Body Prediction 會在輸入影像上執行 3D 身體與手部姿勢估計，並在每一幀中偵測一或多個人。可提供追蹤資料或邊界框來改善偵測結果；若兩者皆未提供，節點會改為在整個畫面中進行單人偵測。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `sam3d_body_model` | 用於預測的 SAM3D 身體模型。 | SAM3D_BODY_MODEL | 是 | — |
| `image` | 要執行身體預測的影像或影像批次。 | IMAGE | 是 | — |
| `track_data` | 來自 SAM3 Video Track 的追蹤資料，多人偵測時必填。 | SAM3_TRACK_DATA | 否 | — |
| `bboxes` | 用於改善偵測效果的逐幀邊界框。可作為追蹤資料的替代方案。 | BBOX | 否 | — |
| `run_hand_refinement` | 改善手部姿勢，但會增加額外的推論時間與記憶體使用量。預設：true。 | BOOLEAN | 否 | true<br>false |
| `fov` | 垂直視場角（度）。會影響預測的深度與絕對比例。0 = 回退至約 53°（16:9）。預設：0.0。 | FLOAT | 否 | 0.0 或更大 |
| `batch_size` | 批次處理的最大人物裁切數量。數值越大會使用更多 VRAM，以換取更快的推論速度。預設：64。 | INT | 否 | 1 至 512 |

注意：當提供 `track_data` 時，其優先順序高於 `bboxes`。若 `track_data` 與 `bboxes` 皆未提供，節點會回退至單人全畫面偵測。邊界框可針對單一幀提供（套用到所有幀），或逐幀提供。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `mhr_pose_data` | 包含逐幀姿勢偵測結果、臉部幾何、輸入影像尺寸、標準頂點顏色，以及手部頂點遮罩的身體姿勢資料包。 | MHR_POSE_DATA |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SAM3DBody_Predict/zh-TW.md)

---
**Source fingerprint (SHA-256):** `f1039349cd2809423053bffde1c7d119c7c42f217327d23c608b1224d183770e`
