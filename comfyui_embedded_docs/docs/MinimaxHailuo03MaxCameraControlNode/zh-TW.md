# MiniMax H3 Max Camera Control

此節點會生成一段影片，影片從靜態影像開始，並將攝影機移動到主體周圍的新角度與距離。方位角、仰角和距離描述攝影機最終的位置；第一幀會完全保持提供時的樣子。未提供提示詞時，場景會保持靜止，只有攝影機會移動。

## 輸入

### 通用輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 用於影片生成的模型。 | DYNAMIC_COMBO | 是 | "MiniMax H3 Max" |

### MiniMax H3 Max 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `image` | 影片的第一幀，至少 256x256 像素。長寬比必須介於 0.4 和 2.5 之間。 | IMAGE | 是 | 單張圖片 |
| `camera_info` | 選填的結束攝影機，例如來自 Create Camera Info 或 Compose Camera Angle Prompt，並以該影像作為前視圖。連接後會設定 `azimuth` 和 `elevation`。 | LOAD3D_CAMERA | 否 | 相機資訊 |
| `prompt` | 選填。留空時，場景會保持靜止，只有攝影機會移動。 | STRING | 是 | 0 至 50000 個字元 |
| `azimuth` | 影片結束時圍繞主體的水平環繞角度，以影像為基準的度數表示（預設：90）。正值會將攝影機向右移動，因此主體會轉向畫面左側。這是一個目標值：90 度的環繞通常會落在 30 到 90 度之間。連接 `camera_info` 時會忽略此參數。 | INT | 是 | -360 至 360 |
| `elevation` | 影片結束時攝影機的垂直角度，以度為單位（預設：0）。正值表示從上方俯視，負值表示從下方仰視。連接 `camera_info` 時會忽略此參數。 | INT | 是 | -90 至 90 |
| `distance` | 影片結束時攝影機相對於影像的距離：1 表示保持不變，小於 1 表示靠近，大於 1 表示拉遠（預設：1.0）。 | FLOAT | 是 | 0.1 至 10.0 |
| `duration` | 輸出影片的長度，以秒為單位（預設：5）。 | INT | 是 | 1 至 15 |
| `resolution` | 輸出影片的解析度（預設："768P"）。 | COMBO | 是 | "480P"<br>"768P"<br>"1080P" |
| `prompt_expansion_mode` | 生成前改寫提示詞所投入的程度（預設："balanced"）。 | COMBO | 是 | "disabled"<br>"balanced"<br>"quality" |
| `seed` | 隨機種子。使用相同種子的相同請求會得到相似但不保證完全相同的結果（預設：42）。 | INT | 是 | 0 至 4294967295 |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `video` | 已套用攝影機移動的生成影片。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03MaxCameraControlNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `d9eed1a3ae91891b974bea39ea00101c0577cf5b204d4c701b13b232e0604153`
