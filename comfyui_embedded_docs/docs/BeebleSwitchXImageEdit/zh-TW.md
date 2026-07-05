# Beeble SwitchX 圖像編輯

## 概述

使用 Beeble SwitchX 編輯單張圖片。此節點可以切換場景中的任何元素（背景、光線、服裝），同時保留原始主體的像素。提供參考圖片和/或文字提示來描述新的外觀。最大解析度約為 277 萬像素。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `圖像` | 要編輯的來源圖片。 | IMAGE | 是 | - |
| `提示詞` | 所需新外觀的文字描述（例如：「身穿閃亮盔甲的騎士」）。 | STRING | 是 | - |
| `alpha 模式` | 處理 Alpha 遮罩的方式。「select」使用關鍵影格選取主體，「fill」直接取代整張圖片而不使用獨立遮罩，「custom」使用使用者提供的遮罩。 | COMBO | 是 | `"select"`<br>`"fill"`<br>`"custom"` |
| `最大解析度` | 輸出圖片的最高解析度。較高解析度會消耗更多點數。 | COMBO | 是 | `"1080p"`<br>`"720p"` |
| `種子` | 用於再現結果的種子值。 | INT | 是 | - |
| `參考圖像` | 可選的參考圖片，用於引導新場景元素的風格或外觀。 | IMAGE | 否 | - |

**關於 `alpha_mode` 的說明：** 當 `alpha_mode` 設定為 `"select"` 時，您也必須提供 `alpha_keyframe`（用於選取主體的關鍵影格圖片）。設定為 `"custom"` 時，您必須提供 `alpha_mask`（使用者建立的遮罩）。設定為 `"fill"` 時，則不需要 Alpha 輸入。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `圖像` | 已編輯的圖片，場景元素已被切換。 | IMAGE |
| `alpha` | Beeble 使用的 Alpha 遮罩。在「fill」模式下為空，因為該模式沒有獨立遮罩。 | MASK |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BeebleSwitchXImageEdit/zh-TW.md)

---
**Source fingerprint (SHA-256):** `41f23435686626e3ade28708fcb1da192ded347b210080ee9b17834ea8b727fb`
