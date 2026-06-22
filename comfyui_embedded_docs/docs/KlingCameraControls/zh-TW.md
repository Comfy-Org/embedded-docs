# Kling 攝影機控制

## 概述

Kling 攝影機控制節點允許您配置各種攝影機移動和旋轉參數，以在影片生成中創建動態控制效果。它提供對攝影機定位、旋轉和縮放的控制，以模擬不同的攝影機運動。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `camera_control_type` | 指定要使用的攝影機控制配置類型 | COMBO | 是 | `"simple"`<br>`"advanced"` |
| `horizontal_movement` | 控制攝影機沿水平軸（x 軸）的移動。負值表示向左，正值表示向右（預設值：0.0） | FLOAT | 否 | -10.0 至 10.0 |
| `vertical_movement` | 控制攝影機沿垂直軸（y 軸）的移動。負值表示向下，正值表示向上（預設值：0.0） | FLOAT | 否 | -10.0 至 10.0 |
| `pan` | 控制攝影機在垂直平面（x 軸）的旋轉。負值表示向下旋轉，正值表示向上旋轉（預設值：0.5） | FLOAT | 否 | -10.0 至 10.0 |
| `tilt` | 控制攝影機在水平平面（y 軸）的旋轉。負值表示向左旋轉，正值表示向右旋轉（預設值：0.0） | FLOAT | 否 | -10.0 至 10.0 |
| `roll` | 控制攝影機的翻滾量（z 軸）。負值表示逆時針，正值表示順時針（預設值：0.0） | FLOAT | 否 | -10.0 至 10.0 |
| `zoom` | 控制攝影機焦距的變化。負值表示視野變窄，正值表示視野變寬（預設值：0.0） | FLOAT | 否 | -10.0 至 10.0 |

**注意：** 至少需要一個攝影機控制參數（`horizontal_movement`、`vertical_movement`、`pan`、`tilt`、`roll` 或 `zoom`）具有非零值，配置才有效。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `camera_control` | 返回已配置的攝影機控制設定，用於影片生成 | CAMERA_CONTROL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingCameraControls/zh-TW.md)

---
**Source fingerprint (SHA-256):** `4e1d826518ae17afd2c0aa22ebf6cce67b3ef33bb1730f0ce5ead5b9431cd548`
