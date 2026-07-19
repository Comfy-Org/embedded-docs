# Kling 雙角色影片特效

## 概述

Kling 雙角色影片特效節點可根據所選場景建立具有特殊效果的影片。它接收兩張圖片，並將第一張圖片放置在合成影片的左側，第二張圖片放置在右側。根據所選的效果場景，會套用不同的視覺效果。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `image_left` | 左側圖片 | IMAGE | 是 | - |
| `image_right` | 右側圖片 | IMAGE | 是 | - |
| `effect_scene` | 套用至影片生成的特殊效果場景類型 | COMBO | 是 | `"chat"`<br>`"dance"`<br>`"hug"`<br>`"kill"`<br>`"kiss"`<br>`"pat"`<br>`"punch"`<br>`"shrug"`<br>`"slap"`<br>`"tickle"` |
| `model_name` | 用於角色效果的模型（預設值："kling-v1"） | COMBO | 否 | `"kling-v1"`<br>`"kling-v1-5"`<br>`"kling-v1-6"` |
| `mode` | 影片生成模式（預設值："std"） | COMBO | 否 | `"std"`<br>`"pro"` |
| `時長` | 生成影片的持續時間（秒） | COMBO | 是 | `"5"`<br>`"10"` |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `時長` | 生成的雙角色效果影片 | VIDEO |
| `時長` | 生成影片的持續時間資訊 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingDualCharacterVideoEffectNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `4ee0c3cd834e1c70e41b40b66ac98d15a8b88993e7dc9d9df9fb4fadb868f079`
