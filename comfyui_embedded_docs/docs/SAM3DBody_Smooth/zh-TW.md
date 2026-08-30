# 平滑化 SAM3D Body 姿勢資料

## 平滑 SAM3D 人體姿勢數據

平滑 SAM3D 人體姿勢數據會透過隨時間平均運動來減少 3D 人體姿勢序列中的幀間抖動。它對攝影機和外觀資料套用完整平滑，而當主體快速旋轉時，則會減弱對網格幾何的平滑，因此快速旋轉不會被扁平化。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `mhr_pose_data` | 要平滑的 MHR 姿勢資料序列，包含模型參數、形狀參數、表情參數、MHR70 關鍵點佈局以及相關網格資料。 | MHR_POSE_DATA | 是 | — |
| `strength` | 平滑強度。0 = 原始，1 = 已平滑。（預設值：1.0） | FLOAT | 是 | 0.0 至 1.0 (step 0.05) |
| `method` | gaussian：對稱加權平均，最佳的通用平滑器。<br>savgol：滑動多項式擬合，保留尖銳峰值。（預設值："savgol"） | COMBO | 是 | "gaussian"<br>"savgol" |
| `window` | 以幀為單位的時間窗口（奇數值）。（預設值：7） | INT | 是 | 1 至 51 (odd values, step 2) |
| `rotation_threshold_degrees` | 對此根旋轉速率（度/幀）停用平滑，以保留快速旋轉。30° 適用於大多數內容，較低的值可能會對普通抖動停用平滑，並靜默地影響品質。0 = 停用。（預設值：30.0） | FLOAT | 是 | 0.0 至 90.0 (step 1.0) |

注意：當 `strength` 為 0.0 或更低，或 `window` 為 1 或更低時，節點會原封不動地傳回輸入資料。輸入必須包含至少 2 幀和關鍵點資料；否則節點會原封不動地傳回輸入資料。當 `rotation_threshold_degrees` 為 0.0 時，基於旋轉的平滑減弱會被停用。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `mhr_pose_data` | 平滑後的 MHR 姿勢資料序列，幀間抖動較少。 | MHR_POSE_DATA |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SAM3DBody_Smooth/zh-TW.md)

---
**Source fingerprint (SHA-256):** `a80a1c121f1d2bc49e9112576775588d5deab4690c4cd6ec9c1f98de78457b30`
