以下是繁體中文翻譯結果：

## 概述

Magnific Image Relight 節點可調整輸入影像的光線。它能根據文字提示套用風格化光線，或從可選的參考影像轉移光線特徵。此節點提供多種控制選項，用於微調最終輸出的亮度、對比度和整體氛圍。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `image` | 要重新打光的影像。需要剛好一張影像。最小尺寸為 160x160 像素。長寬比必須介於 1:3 到 3:1 之間。 | IMAGE | 是 | 不適用 |
| `prompt` | 光線的描述性指引。支援強調標記法 (1-1.4)。預設為空字串。 | STRING | 否 | 不適用 |
| `light_transfer_strength` | 光線轉移應用的強度。預設值：100。 | INT | 是 | 0 到 100 |
| `style` | 風格化輸出偏好。 | COMBO | 是 | `"standard"`<br>`"darker_but_realistic"`<br>`"clean"`<br>`"smooth"`<br>`"brighter"`<br>`"contrasted_n_hdr"`<br>`"just_composition"` |
| `interpolate_from_original` | 限制生成自由度以更貼近原始影像。預設值：False。 | BOOLEAN | 是 | 不適用 |
| `change_background` | 根據提示/參考影像修改背景。預設值：True。 | BOOLEAN | 是 | 不適用 |
| `preserve_details` | 保留原始影像的紋理和細節。預設值：True。 | BOOLEAN | 是 | 不適用 |
| `advanced_settings` | 進階光線控制的微調選項。設為 `"enabled"` 時，將啟用其他參數。 | DYNAMICCOMBO | 是 | `"disabled"`<br>`"enabled"` |
| `reference_image` | 可選的參考影像，用於從中轉移光線。若提供，需要剛好一張影像。最小尺寸為 160x160 像素。長寬比必須介於 1:3 到 3:1 之間。 | IMAGE | 否 | 不適用 |

**關於進階設定的說明：** 當 `advanced_settings` 設為 `"enabled"` 時，以下嵌套參數將啟用：

* `whites`：調整影像中最亮的色調。範圍：0 到 100。預設值：50。
* `blacks`：調整影像中最暗的色調。範圍：0 到 100。預設值：50。
* `brightness`：整體亮度調整。範圍：0 到 100。預設值：50。
* `contrast`：對比度調整。範圍：0 到 100。預設值：50。
* `saturation`：色彩飽和度調整。範圍：0 到 100。預設值：50。
* `engine`：處理引擎選擇。選項：`"automatic"`、`"balanced"`、`"cool"`、`"real"`、`"illusio"`、`"fairy"`、`"colorful_anime"`、`"hard_transform"`、`"softy"`。
* `transfer_light_a`：光線轉移的強度。選項：`"automatic"`、`"low"`、`"medium"`、`"normal"`、`"high"`、`"high_on_faces"`。
* `transfer_light_b`：也修改光線轉移強度。可與前一個控制項結合以產生多種效果。選項：`"automatic"`、`"composition"`、`"straight"`、`"smooth_in"`、`"smooth_out"`、`"smooth_both"`、`"reverse_both"`、`"soft_in"`、`"soft_out"`、`"soft_mid"`、`"style_shift"`、`"strong_shift"`。
* `fixed_generation`：確保使用相同設定時輸出一致。預設值：True。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `image` | 重新打光後的影像。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MagnificImageRelightNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `c260b7c88a267a20fdea7f436404fe96ede782bc522ab29da36e94c20f7330cd`
