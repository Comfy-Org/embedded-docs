# 平滑化 SAM3D Body 姿勢資料

Smooth SAM3D Body Pose Data 會透過隨時間平均運動，減少一串 3D 身體姿勢中的逐幀抖動。攝影機與外觀資料會完整平滑處理，而當主體快速旋轉時，網格幾何的平滑程度會降低，因此快速旋轉不會被壓平。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `mhr_pose_data` | 要平滑處理的 MHR 姿勢資料序列，包含模型參數、形狀參數、表情參數、MHR70 關鍵點佈局及相關網格資料。 | MHR_POSE_DATA | 是 | — |
| `strength` | 平滑強度。0 = 原始，1 = 平滑。（預設值：1.0） | FLOAT | 是 | 0.0 至 1.0（步長 0.05） |
| `method` | gaussian：對稱加權平均，最佳通用平滑器。<br>savgol：滑動多項式擬合，保留尖銳峰值。（預設值："savgol"） | COMBO | 是 | "gaussian"<br>"savgol" |
| `window` | 以幀為單位的時間視窗（奇數值）。（預設值：7） | INT | 是 | 1 至 51（奇數值，步長 2） |
| `rotation_threshold_degrees` | 當根部旋轉速率達到此值（度/幀）時停用平滑，以保留快速旋轉。30° 適合大多數內容；較低的值可能會在一般抖動上停用平滑，並悄悄影響品質。0 = 停用。（預設值：30.0） | FLOAT | 是 | 0.0 至 90.0（步長 1.0） |

注意：當 `strength` 為 0.0 或更低，或 `window` 為 1 或更低時，節點會原樣傳回輸入資料。輸入必須包含至少 2 幀與關鍵點資料；否則節點會原樣傳回輸入資料。當 `rotation_threshold_degrees` 為 0.0 時，會停用基於旋轉的平滑退避機制。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `mhr_pose_data` | 已平滑的 MHR 姿勢資料序列，具有減少後的逐幀抖動。 | MHR_POSE_DATA |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SAM3DBody_Smooth/zh-TW.md)

---
**Source fingerprint (SHA-256):** `a80a1c121f1d2bc49e9112576775588d5deab4690c4cd6ec9c1f98de78457b30`
