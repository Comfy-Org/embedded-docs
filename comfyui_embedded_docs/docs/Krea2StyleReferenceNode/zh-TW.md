## 概述

Krea 2 風格參考節點可讓您添加參考影像來影響 Krea 2 影像生成的風格。您可以將多個風格參考串聯在一起（最多總共 10 個），並將合併後的結果輸入到 Krea 2 影像節點。您提供的每張影像都會上傳到 ComfyAPI 儲存空間，並以 URL 形式傳遞。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `參考圖像` | 影響生成風格的參考影像。 | IMAGE | 是 | - |
| `強度` | 參考強度；負值會反轉風格影響（預設值：1.0）。 | FLOAT | 是 | -2.0 到 2.0（步長：0.05） |
| `style_reference` | 可選的傳入風格參考鏈；此節點會再附加一個參考。 | STYLE_REF | 否 | - |

**限制說明：** 您最多總共可以串聯 10 個風格參考。如果嘗試添加第 11 個參考，節點將會引發錯誤。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `style_reference` | 風格參考條目的列表，每個條目包含 URL 和強度值。將此輸出輸入到 Krea 2 影像節點。 | STYLE_REF |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Krea2StyleReferenceNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `7f87568a1cd5038571f3188cfb1d71e15533ea19eee01d7826fe574a1a4dc88d`
