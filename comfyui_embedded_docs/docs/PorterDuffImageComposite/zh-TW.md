> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PorterDuffImageComposite/zh-TW.md)

PorterDuffImageComposite 節點旨在使用 Porter-Duff 合成運算子執行影像合成。它允許根據各種混合模式組合來源影像與目標影像，透過操控影像透明度並以創意方式疊加影像，來建立複雜的視覺效果。

## 輸入

| 參數 | 資料類型 | 描述 |
| --------- | ------------ | ----------- |
| `source`  | `IMAGE`     | 要合成在目標影像之上的來源影像張量。根據所選的合成模式，它在決定最終視覺結果方面扮演關鍵角色。 |
| `source_alpha` | `MASK` | 來源影像的 Alpha 通道，指定來源影像中每個像素的透明度。它會影響來源影像與目標影像的混合方式。 |
| `destination` | `IMAGE` | 作為背景的目標影像張量，來源影像將合成於其上。根據混合模式，它會對最終合成影像產生貢獻。 |
| `destination_alpha` | `MASK` | 目標影像的 Alpha 通道，定義目標影像像素的透明度。它會影響來源影像與目標影像的混合。 |
| `mode` | COMBO[STRING] | 要套用的 Porter-Duff 合成模式，決定來源影像與目標影像如何混合在一起。每種模式都會產生不同的視覺效果。 |

## 輸出

| 參數 | 資料類型 | 描述 |
| --------- | ------------ | ----------- |
| `image`   | `IMAGE`     | 套用指定 Porter-Duff 模式後產生的合成影像。 |
| `mask`    | `MASK`      | 合成影像的 Alpha 通道，指示每個像素的透明度。 |