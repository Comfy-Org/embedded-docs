> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingDualCharacterVideoEffectNode/zh-TW.md)

Kling 雙角色影片特效節點根據選取的場景建立帶有特效的影片。它接收兩張圖片，並將第一張圖片置於合成影片的左側，第二張圖片置於右側。根據選擇的特效場景，會套用不同的視覺效果。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `image_left` | IMAGE | 是 | - | 左側圖片 |
| `image_right` | IMAGE | 是 | - | 右側圖片 |
| `effect_scene` | COMBO | 是 | 多個選項可用 | 套用於影片生成的特效場景類型 |
| `model_name` | COMBO | 否 | 多個選項可用 | 用於角色特效的模型（預設值："kling-v1"） |
| `mode` | COMBO | 否 | 多個選項可用 | 影片生成模式（預設值："std"） |
| `時長` | COMBO | 是 | 多個選項可用 | 生成影片的持續時間 |

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `時長` | VIDEO | 帶有雙角色特效的生成影片 |
| `時長` | STRING | 生成影片的持續時間資訊 |